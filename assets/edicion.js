// Lula — lo interactivo de cada edición (en pantalla; el PDF no lo necesita).
(function () {
  const clave = "lula:" + location.pathname;
  const leer = (k) => { try { return JSON.parse(localStorage.getItem(clave + k)); } catch { return null; } };
  const guardar = (k, v) => { try { localStorage.setItem(clave + k, JSON.stringify(v)); } catch {} };

  // Tema claro / oscuro
  const raiz = document.documentElement;
  try { const t = localStorage.getItem("lula:tema"); if (t) raiz.dataset.theme = t; } catch {}
  document.querySelectorAll("[data-tema]").forEach((b) => b.addEventListener("click", () => {
    const oscuro = raiz.dataset.theme ? raiz.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
    raiz.dataset.theme = oscuro ? "light" : "dark";
    try { localStorage.setItem("lula:tema", raiz.dataset.theme); } catch {}
  }));

  // Lo que escribís queda guardado en este navegador
  document.querySelectorAll("textarea[id]").forEach((t) => {
    const v = leer(":t:" + t.id); if (v) t.value = v;
    t.addEventListener("input", () => guardar(":t:" + t.id, t.value));
  });
  document.querySelectorAll('input[type="checkbox"][id]').forEach((c) => {
    c.checked = !!leer(":c:" + c.id);
    c.addEventListener("change", () => guardar(":c:" + c.id, c.checked));
  });

  // Escuchar en voz alta (francés o inglés)
  document.querySelectorAll(".oir").forEach((b) => b.addEventListener("click", () => {
    if (!("speechSynthesis" in window)) return;
    const txt = document.getElementById(b.dataset.texto)?.innerText || "";
    speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(txt);
    u.lang = b.dataset.idioma || "fr-FR";
    u.rate = parseFloat(b.dataset.velocidad || "0.85");
    speechSynthesis.speak(u);
  }));

  // Quiz: tocás una opción y te dice si está bien
  const quiz = document.querySelector(".quiz");
  const marcador = document.querySelector(".puntaje");
  let bien = 0, hechas = 0;
  document.querySelectorAll(".quiz > li[data-ok]").forEach((q) => {
    const ok = Number(q.dataset.ok);
    const botones = [...q.querySelectorAll(".opciones button")];
    botones.forEach((b, i) => b.addEventListener("click", () => {
      if (q.dataset.hecha) return;
      q.dataset.hecha = "1"; hechas++;
      if (i === ok) bien++;
      botones[ok].classList.add("bien");
      if (i !== ok) botones[i].classList.add("mal");
      if (marcador) marcador.textContent = `${bien} de ${hechas} bien`;
    }));
  });
  if (quiz && marcador) marcador.textContent = "Tocá una opción en cada pregunta.";

  // Soluciones tapadas hasta que las tocás
  document.querySelectorAll(".tapado").forEach((s) => s.addEventListener("click", () => s.classList.add("visto")));
})();
