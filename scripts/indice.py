"""Actualiza la lista de ediciones en index.html (entre los marcadores EDICIONES)."""
import html
import re
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
         "septiembre", "octubre", "noviembre", "diciembre"]


def meta(texto, nombre):
    m = re.search(rf'<meta name="{re.escape(nombre)}" content="([^"]*)"', texto)
    return html.unescape(m.group(1)) if m else ""


items = []
for f in sorted((RAIZ / "ediciones").glob("????-??-??.html"), reverse=True):
    t = f.read_text(encoding="utf-8")
    d = date.fromisoformat(f.stem)
    fecha = f"{DIAS[d.weekday()].capitalize()} {d.day} de {MESES[d.month - 1]} de {d.year}"
    pdf = f'<a class="pildora" href="ediciones/{f.stem}.pdf">PDF</a>' if f.with_suffix(".pdf").exists() else ""
    items.append(
        f'  <li><h3><a href="ediciones/{f.name}">{fecha}</a></h3>'
        f'<span class="num">Nº {html.escape(meta(t, "lula:numero"))} {pdf}</span>'
        f'<p>{html.escape(meta(t, "description"))}</p></li>'
    )

indice = RAIZ / "index.html"
s = indice.read_text(encoding="utf-8")
s = re.sub(r"(<!-- EDICIONES -->).*?(<!-- /EDICIONES -->)",
           lambda m: m.group(1) + "\n" + "\n".join(items) + "\n  " + m.group(2), s, flags=re.S)
indice.write_text(s, encoding="utf-8")
print(f"{len(items)} ediciones en index.html")

# hoy.html: link fijo que siempre lleva a la última edición
ultima = max((RAIZ / "ediciones").glob("????-??-??.html"), default=None)
if ultima:
    (RAIZ / "hoy.html").write_text(
        '<!doctype html><meta charset="utf-8"><title>Lula · hoy</title>'
        f'<meta http-equiv="refresh" content="0; url=ediciones/{ultima.name}">'
        f'<a href="ediciones/{ultima.name}">Ir a la edición de hoy</a>\n', encoding="utf-8")
    print("hoy.html ->", ultima.name)
