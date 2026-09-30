"""Genera el sudoku del día (con solución única) como HTML para pegar en la edición.

Uso: python3 scripts/sudoku.py 2026-10-01 [facil|medio|dificil]
Imprime dos bloques: el tablero (sección Pasatiempo) y la solución (sección Soluciones).
El mismo día siempre da el mismo sudoku.
"""
import random
import sys

PISTAS = {"facil": 38, "medio": 32, "dificil": 27}


def candidatos(g, i):
    f, c = divmod(i, 9)
    usados = set(g[f * 9:f * 9 + 9]) | set(g[c::9])
    bf, bc = f // 3 * 3, c // 3 * 3
    for r in range(bf, bf + 3):
        usados |= set(g[r * 9 + bc:r * 9 + bc + 3])
    return [n for n in range(1, 10) if n not in usados]


def resolver(g, rnd=None, limite=2):
    """Cuenta soluciones (hasta `limite`). Si rnd, llena g con una solución al azar."""
    vacias = [i for i, v in enumerate(g) if v == 0]
    if not vacias:
        return 1
    i = min(vacias, key=lambda k: len(candidatos(g, k)))
    ops = candidatos(g, i)
    if rnd:
        rnd.shuffle(ops)
    total = 0
    for n in ops:
        g[i] = n
        total += resolver(g, rnd, limite)
        if rnd and total:
            return total
        if total >= limite:
            break
    g[i] = 0
    return total


def generar(semilla, nivel):
    rnd = random.Random(semilla)
    sol = [0] * 81
    resolver(sol, rnd)
    tablero = sol[:]
    orden = list(range(81))
    rnd.shuffle(orden)
    pistas = 81
    for i in orden:
        if pistas <= PISTAS[nivel]:
            break
        guardado = tablero[i]
        tablero[i] = 0
        if resolver(tablero[:]) != 1:
            tablero[i] = guardado
        else:
            pistas -= 1
    return tablero, sol


def html(tablero, sol, conInputs):
    celdas = []
    for i, v in enumerate(tablero):
        if v:
            celdas.append(f"<span class=\"dada\">{v}</span>")
        elif conInputs:
            celdas.append('<input inputmode="numeric" maxlength="1" aria-label="casilla">')
        else:
            celdas.append(f"<span>{sol[i]}</span>")
    return "".join(celdas)


if __name__ == "__main__":
    fecha = sys.argv[1]
    nivel = sys.argv[2] if len(sys.argv) > 2 else "medio"
    t, s = generar(fecha, nivel)
    solucion = "".join(map(str, s))
    print(f'<div class="sudoku" data-sol="{solucion}">{html(t, s, True)}</div>')
    print()
    print(f'<div class="sudoku chico">{html([0] * 81, s, False)}</div>')
