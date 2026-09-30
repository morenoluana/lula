# Lula — guía editorial

Cómo se arma cada edición del diario de la mañana. La edición la escribe Claude todos los días, temprano, y tiene que estar lista (web + PDF + mail) a las **8:00 de Buenos Aires**.

## Para quién es

Para Lula: vive en Buenos Aires, estudia biotecnología, lee en inglés y está aprendiendo francés desde cero (A1). Quiere enterarse de lo que pasa en el mundo sin la mirada centrada en Estados Unidos, conocer su ciudad (árboles, flores, aves, barrios, historia), leer clásicos universales y argentinos, y tener cosas para practicar en GoodNotes. Le encantan la moda y su historia, el arte, los museos, el cine viejo y la música clásica (el Cascanueces, el Lago de los cisnes, Vivaldi).

Tiene que sentirse como una revista hecha a mano para una sola persona: cálida, curiosa, precisa. Nada de relleno.

## Tono y lengua

- Castellano rioplatense con voseo («mirá», «tenés»), claro y directo. Frases cortas.
- Nada de exageraciones ni frases de marketing. Si algo es incierto, se dice.
- Cada noticia explica **por qué importa** o **qué tiene que ver con vos**.
- Ciencia con ojo crítico: tamaño de muestra, quién financia y si es en humanos, ratones o células.

## Estructura de cada edición

Tiempo de lectura total: 20 a 30 minutos. En PDF A4, entre 10 y 14 páginas.

| Sección | Contenido | Clase CSS |
|---|---|---|
| Portada | Saludo con el tema del día (efemérides, días internacionales), clima de BA para hoy, índice | `saludo`, `clima`, `indice` |
| El mundo en cinco minutos | 4 o 5 noticias de las últimas 24 h. **Como mucho una** centrada en EE.UU. Priorizar Europa, América Latina, África, Asia y Medio Oriente. Cada una con «Por qué importa». | `mundo` |
| Argentina y Buenos Aires | 3 o 4 noticias del país y la ciudad + caja «Para hacer en la ciudad» (muestras, cine, conciertos, ferias de esta semana, con dirección y horario). | `pais` |
| Ciencia | Un descubrimiento reciente, con caja «La conexión con lo que estudiás» (biotecnología, biología molecular, química) + 1 o 2 notas de «Ciencia en la vida cotidiana» (química de la cocina, del cuerpo, de la casa, de la ciudad). | `ciencia` |
| Mirá a tu alrededor | Un árbol, una flor o un ave de Buenos Aires **que se pueda ver esta semana** (temporada de floración, migración, nidos), con ficha y cómo reconocerlo. Misión con checkboxes + cuadro para dibujar. | `naturaleza` |
| Un clásico en cinco minutos | Fragmento de un clásico universal (dominio público, traducción propia si hace falta), contexto y un puente con Argentina, el cine o hoy. Una pregunta para escribir. | `letras` |
| Le français du matin | Texto corto en francés al nivel que toque (ver progresión), glosario, una mini gramática y 3 o 4 preguntas para responder por escrito. Botón `▶ écouter`. | `frances` |
| English corner | 250–350 palabras en inglés (B2–C1) sobre una noticia o tema no estadounidense, glosario y 3 preguntas. Botón `▶ listen`. | `ingles` |
| Sección del día | Rota según el día de la semana (ver abajo). | `cultura` |
| Hoy en la historia · un lugar | Una efeméride (universal o argentina) + ficha de un lugar del mapa vinculado a una noticia, con cuadro para dibujar el mapa. | `historia` |
| Lo que me asombra hoy | Un dato asombroso y verificable, contado en dos párrafos. | `asombro` |
| Cuaderno | Quiz de 6 a 8 preguntas de opción múltiple sobre la edición + escritura libre. | `cuaderno` |
| Soluciones y fuentes | Respuestas del quiz, francés e inglés. Lista de fuentes con links. Cierre con adelanto de mañana. | `soluciones` |

### Sección del día

- **Lunes — Arte y museos:** una obra (preferentemente visible en un museo de BA: Bellas Artes, MALBA, Moderno, Fortabat, Sívori, Decorativo) o un movimiento; cómo mirarla.
- **Martes — Moda:** historia de una gran casa (Chanel, Dior, Balenciaga, Schiaparelli, Saint Laurent, Givenchy…), un desfile histórico que marcó época, una prenda con historia, o una tendencia actual explicada con su genealogía. También moda argentina (Paco Jamandreu, Pablo Ramírez, Gino Bogani…).
- **Miércoles — Letras argentinas:** Borges, Cortázar, Ocampo, Pizarnik, Arlt, Storni, Walsh, Saer, Aira, Piñeiro… Fragmento corto (cita breve si no es de dominio público) y contexto.
- **Jueves — Cine clásico:** una película vieja, un actor o una actriz, un director. Si hay un ciclo en BA (Sala Lugones, MALBA, Cineteca), usarlo.
- **Viernes — Música clásica:** una obra con guía de escucha por movimientos, su historia y dónde escucharla en BA (Colón, Usina del Arte, CCK). Más un plan para el fin de semana.
- **Sábado — Historia argentina:** un episodio, un personaje o un lugar de la ciudad con historia (una esquina, un edificio, un barrio).
- **Domingo — Edición lenta:** un texto clásico más largo, repaso de las palabras en francés e inglés de la semana, y el «asombro de la semana».

### Progresión del francés

Arrancó en A1 (presente de *être*, *avoir*, verbos en -er, clima, rutina). Subir de a poco: cada semana, un tema gramatical nuevo, en el orden del cuaderno (`frances/index.html`): presentarse → rutina → artículos → negación → *aller* y *faire* → futuro próximo → pasado compuesto → imperfecto. Textos de 4 a 8 frases al principio; recién después de un mes, párrafos de 10 a 12. Anotar en el registro qué se vio.

## Reglas de contenido

1. **Todo verificado.** Cada noticia sale de una búsqueda web del día, y cada dato se chequea con al menos una fuente. Si no se puede verificar, no va. Nada inventado: ni citas, ni cifras, ni horarios.
2. **Fuentes al final**, con links reales.
3. **Sin repetir:** antes de elegir el árbol o el ave, el clásico, la obra, la casa de moda y el lugar, leer `ediciones/registro.md` y no repetir nada de los últimos 60 días. Después, agregar lo de hoy al registro.
4. Textos literarios: solo dominio público completos, o citas breves con atribución. Las traducciones, propias.
5. Nada de noticias policiales morbosas ni chimentos.
6. Hilar las secciones cuando se pueda (la noticia de Marruecos → el inglés → el mapa), sin forzarlo.

## Cómo se arma (paso a paso)

1. Fecha de hoy en Buenos Aires (`TZ=America/Argentina/Buenos_Aires date +%F`). El número de edición es el de la última + 1.
2. Leer `ediciones/registro.md` y la última edición.
3. Investigar con búsqueda web: noticias del mundo y de Argentina de las últimas 24 h, pronóstico de BA para hoy, agenda cultural de la semana, un estudio científico reciente, efemérides del día.
4. Copiar la última edición como plantilla a `ediciones/AAAA-MM-DD.html` y reemplazar todo el contenido. Mantener la estructura HTML, las clases y los `id` (los `textarea` y `checkbox` necesitan `id` únicos). Actualizar `<title>`, `description`, `lula:numero`, `lula:fecha`, el link al PDF y el quiz (`data-ok` = índice desde 0 de la opción correcta).
5. Generar el PDF: `node scripts/pdf.mjs ediciones/AAAA-MM-DD.html`. Revisarlo: entre 10 y 14 páginas, sin títulos huérfanos al final de una página.
6. Actualizar la portada: `python3 scripts/indice.py`.
7. Agregar lo de hoy a `ediciones/registro.md`.
8. Commit («Edición Nº N — AAAA-MM-DD») y push a la rama por defecto del repo. GitHub Pages publica solo.
9. Mandar el mail (ver abajo).

## El mail

- Asunto: `Lula Nº N · Jueves 1 de octubre — <titular principal>`
- Cuerpo en HTML, corto: saludo, clima, las 3 o 4 cosas más importantes en una línea cada una, y dos botones/links:
  - Leer en la web: `https://morenoluana.github.io/lula/ediciones/AAAA-MM-DD.html`
  - PDF para GoodNotes: `https://morenoluana.github.io/lula/ediciones/AAAA-MM-DD.pdf`
  - Si GitHub Pages no está activo todavía, usar `https://github.com/morenoluana/lula/blob/<rama-por-defecto>/ediciones/AAAA-MM-DD.pdf`.
