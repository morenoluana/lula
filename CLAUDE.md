# Lula

Diario personal de la mañana (web + PDF para GoodNotes) y un cuaderno de francés.

- Para armar una edición, seguí **EDITORIAL.md** al pie de la letra.
- Ediciones: `ediciones/AAAA-MM-DD.html` (+ `.pdf`). Estilos y JS compartidos en `assets/`. Fuentes locales en `assets/fuentes/` (no volver a Google Fonts: el PDF se genera sin acceso a ellas).
- PDF: `node scripts/pdf.mjs ediciones/AAAA-MM-DD.html` (usa el Playwright global y Chromium en `/opt/pw-browsers`).
- Portada: `python3 scripts/indice.py` regenera la lista de ediciones en `index.html`.
- Cuaderno de francés: `frances/index.html`.
