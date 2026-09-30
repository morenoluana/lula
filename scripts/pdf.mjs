// Genera el PDF A4 de una edición (o de todas las que no tengan PDF).
// Uso: node scripts/pdf.mjs ediciones/2026-10-01.html
//      node scripts/pdf.mjs            -> todas las que falten
import { createRequire } from "node:module";
import { execSync } from "node:child_process";
import { existsSync, readdirSync } from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";

// Playwright está instalado de forma global en el entorno; si no, `npm i -g playwright`.
const globalRoot = execSync("npm root -g").toString().trim();
const { chromium } = createRequire(path.join(globalRoot, "noop.js"))("playwright");

const raiz = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const carpeta = path.join(raiz, "ediciones");
let archivos = process.argv.slice(2).map((a) => path.resolve(a));
if (!archivos.length) {
  archivos = readdirSync(carpeta)
    .filter((f) => /^\d{4}-\d{2}-\d{2}\.html$/.test(f))
    .map((f) => path.join(carpeta, f))
    .filter((f) => !existsSync(f.replace(/\.html$/, ".pdf")));
}

const exe = process.env.CHROMIUM_PATH || (existsSync("/opt/pw-browsers/chromium") ? "/opt/pw-browsers/chromium" : undefined);
const browser = await chromium.launch(exe ? { executablePath: exe } : {});
for (const html of archivos) {
  const page = await browser.newPage();
  await page.goto(pathToFileURL(html).href, { waitUntil: "networkidle" });
  // Las fotos tienen loading="lazy": forzar que carguen todas antes de imprimir
  await page.evaluate(async () => {
    const imgs = [...document.images];
    imgs.forEach((i) => { i.loading = "eager"; });
    await Promise.all(imgs.map((i) => i.complete ? null : new Promise((ok) => { i.onload = i.onerror = ok; })));
    await document.fonts.ready;
  });
  await page.emulateMedia({ media: "print" });
  const salida = html.replace(/\.html$/, ".pdf");
  await page.pdf({ path: salida, format: "A4", printBackground: true, preferCSSPageSize: true });
  console.log("PDF:", path.relative(raiz, salida));
  await page.close();
}
await browser.close();
