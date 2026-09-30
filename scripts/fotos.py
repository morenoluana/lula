"""Baja las fotos de cada edición desde Wikimedia Commons y completa los créditos.

En la edición, cada foto se marca así:

  <figure class="foto" data-buscar="Handroanthus impetiginosus" data-id="lapacho">
    <img alt="Un lapacho rosado en flor">
    <figcaption>Texto del epígrafe. <span class="credito"></span></figcaption>
  </figure>

- data-buscar: búsqueda en Commons (se usa el primer resultado con buena resolución), o
- data-archivo: el nombre exacto del archivo en Commons ("Franz Kafka, 1923.jpg").

El script guarda la imagen en assets/img/<fecha>/<id>.jpg, le pone el src al <img>,
escribe el crédito (autor · licencia) y marca la figura con data-lista para no repetirla.
Corre en GitHub Actions, que tiene acceso a Wikimedia (el entorno de Claude no).

Uso: python3 scripts/fotos.py [ediciones/AAAA-MM-DD.html ...]   (sin argumentos: todas)
Imprime las ediciones que cambiaron.
"""
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
API = "https://commons.wikimedia.org/w/api.php"
UA = "LulaDiario/1.0 (https://github.com/morenoluana/lula; diario personal)"
ANCHO = 1200


def pedir(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for intento in range(4):
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                return r.read()
        except Exception as e:  # red inestable o 429
            if intento == 3:
                raise
            time.sleep(2 ** intento * 2)


def consultar(params):
    base = {"action": "query", "format": "json", "prop": "imageinfo",
            "iiprop": "url|extmetadata|size|mime", "iiurlwidth": str(ANCHO)}
    base.update(params)
    datos = json.loads(pedir(API + "?" + urllib.parse.urlencode(base)))
    paginas = list(datos.get("query", {}).get("pages", {}).values())
    paginas.sort(key=lambda p: p.get("index", 0))
    for p in paginas:
        info = (p.get("imageinfo") or [None])[0]
        if not info or info.get("mime") not in ("image/jpeg", "image/png"):
            continue
        if info.get("width", 0) < 450:
            continue
        return p["title"], info
    return None


def limpio(texto):
    texto = re.sub(r"<[^>]+>", "", texto or "")
    return re.sub(r"\s+", " ", html.unescape(texto)).strip()


def credito(titulo, info):
    meta = info.get("extmetadata", {})
    autor = limpio(meta.get("Artist", {}).get("value")) or "autor desconocido"
    if len(autor) > 60:
        autor = autor[:57] + "…"
    licencia = limpio(meta.get("LicenseShortName", {}).get("value")) or "ver licencia"
    url = info.get("descriptionurl", "https://commons.wikimedia.org/wiki/" + urllib.parse.quote(titulo))
    return (f'Foto: {html.escape(autor)} · {html.escape(licencia)} · '
            f'<a href="{html.escape(url)}">Wikimedia Commons</a>')


def procesar(ruta):
    texto = ruta.read_text(encoding="utf-8")
    fecha = ruta.stem
    carpeta = RAIZ / "assets" / "img" / fecha
    cambios = 0

    def figura(m):
        nonlocal cambios
        bloque = m.group(0)
        if "data-lista" in bloque:
            return bloque
        ident = re.search(r'data-id="([^"]+)"', bloque)
        archivo = re.search(r'data-archivo="([^"]+)"', bloque)
        buscar = re.search(r'data-buscar="([^"]+)"', bloque)
        if not ident or not (archivo or buscar):
            return bloque
        try:
            res = None
            if archivo:
                res = consultar({"titles": "File:" + html.unescape(archivo.group(1))})
            if not res and buscar:
                res = consultar({"generator": "search", "gsrnamespace": "6", "gsrlimit": "8",
                                 "gsrsearch": html.unescape(buscar.group(1)) + " filetype:bitmap"})
            if not res:
                print(f"  sin resultado: {ident.group(1)}", file=sys.stderr)
                return bloque
            titulo, info = res
            carpeta.mkdir(parents=True, exist_ok=True)
            ext = ".png" if info["mime"] == "image/png" else ".jpg"
            destino = carpeta / (ident.group(1) + ext)
            destino.write_bytes(pedir(info.get("thumburl") or info["url"]))
        except Exception as e:
            print(f"  error con {ident.group(1)}: {e}", file=sys.stderr)
            return bloque
        rel = f"../assets/img/{fecha}/{destino.name}"
        bloque = bloque.replace("<figure", "<figure data-lista", 1)
        bloque = re.sub(r"<img(?![^>]*\bsrc=)", f'<img src="{rel}" loading="lazy"', bloque, count=1)
        bloque = re.sub(r'<span class="credito">.*?</span>',
                        f'<span class="credito">{credito(titulo, info)}</span>', bloque, count=1, flags=re.S)
        print(f"  {ident.group(1)} ← {titulo}", file=sys.stderr)
        cambios += 1
        time.sleep(0.5)
        return bloque

    nuevo = re.sub(r"<figure\b[^>]*class=\"[^\"]*\bfoto\b[^\"]*\"[^>]*>.*?</figure>", figura, texto, flags=re.S)
    if cambios:
        ruta.write_text(nuevo, encoding="utf-8")
    return cambios


if __name__ == "__main__":
    rutas = [Path(a).resolve() for a in sys.argv[1:]] or sorted((RAIZ / "ediciones").glob("????-??-??.html"))
    for r in rutas:
        if procesar(r):
            print(r.relative_to(RAIZ))
