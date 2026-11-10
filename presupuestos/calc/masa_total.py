#!/usr/bin/env python3
"""Suma los masa.yaml de todos los subsistemas y compara con S1 (500 g ± 10 g).

Uso (desde la raíz del repo):
    python presupuestos/calc/masa_total.py
    python presupuestos/calc/masa_total.py --markdown > presupuestos/masa.md

Sale con código 1 si algún archivo tiene errores de formato.
"""
import argparse
import math
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Falta PyYAML: pip install -r requirements.txt")

OBJETIVO_G = 500.0
TOLERANCIA_G = 10.0
FUENTES = {"calculado", "hoja_de_datos", "modelo_3d", "medido", "estimado"}

RAIZ = Path(__file__).resolve().parents[2]


def cargar():
    filas, errores = [], []
    for archivo in sorted(RAIZ.glob("subsistemas/*/masa.yaml")):
        rel = archivo.relative_to(RAIZ)
        try:
            datos = yaml.safe_load(archivo.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as e:
            errores.append(f"{rel}: YAML inválido ({e})")
            continue
        sub = datos.get("subsistema") or archivo.parent.name
        for i, c in enumerate(datos.get("componentes") or [], 1):
            nombre = c.get("nombre") or f"(componente {i} sin nombre)"
            masa, inc, fuente = c.get("masa_g"), c.get("incertidumbre_g"), c.get("fuente")
            if fuente not in FUENTES:
                errores.append(f"{rel}: '{nombre}' tiene fuente '{fuente}' (válidas: {', '.join(sorted(FUENTES))})")
            for campo, valor in (("masa_g", masa), ("incertidumbre_g", inc)):
                if valor is not None and not isinstance(valor, (int, float)):
                    errores.append(f"{rel}: '{nombre}' tiene {campo} no numérico ({valor!r})")
            if isinstance(masa, (int, float)) and not c.get("referencia"):
                errores.append(f"{rel}: '{nombre}' tiene masa pero no referencia")
            filas.append({"sub": sub, "nombre": nombre, "masa": masa, "inc": inc, "fuente": fuente})
    return filas, errores


def cargar_asignacion():
    archivo = RAIZ / "presupuestos" / "asignacion-masa.yaml"
    if not archivo.exists():
        return []
    try:
        return (yaml.safe_load(archivo.read_text(encoding="utf-8")) or {}).get("asignacion") or []
    except yaml.YAMLError:
        return []


def resumir(filas):
    definidas = [f for f in filas if isinstance(f["masa"], (int, float))]
    pendientes = [f for f in filas if not isinstance(f["masa"], (int, float))]
    total = sum(f["masa"] for f in definidas)
    incs = [f["inc"] for f in definidas if isinstance(f["inc"], (int, float))]
    sin_inc = [f for f in definidas if not isinstance(f["inc"], (int, float))]
    rss = math.sqrt(sum(x * x for x in incs))
    peor = sum(incs)
    por_sub = {}
    for f in definidas:
        por_sub[f["sub"]] = por_sub.get(f["sub"], 0) + f["masa"]
    return definidas, pendientes, sin_inc, total, rss, peor, por_sub


def texto(filas, errores, md=False):
    definidas, pendientes, sin_inc, total, rss, peor, por_sub = resumir(filas)
    lo, hi = OBJETIVO_G - TOLERANCIA_G, OBJETIVO_G + TOLERANCIA_G
    out = []
    if md:
        out += ["# Presupuesto de masa", "", "Generado con `python presupuestos/calc/masa_total.py --markdown`. No editar a mano.", "",
                "| Subsistema | Componente | Masa (g) | Incertidumbre (g) | Fuente |", "| --- | --- | --- | --- | --- |"]
        for f in filas:
            m = f"{f['masa']:.1f}" if isinstance(f["masa"], (int, float)) else "TBD"
            i = f"± {f['inc']:.1f}" if isinstance(f["inc"], (int, float)) else "—"
            out.append(f"| {f['sub']} | {f['nombre']} | {m} | {i} | {f['fuente'] or '—'} |")
        out.append("")
    else:
        out.append(f"{'Subsistema':<11} {'Componente':<48} {'Masa (g)':>9} {'± (g)':>7}  Fuente")
        out.append("-" * 92)
        for f in filas:
            m = f"{f['masa']:.1f}" if isinstance(f["masa"], (int, float)) else "TBD"
            i = f"{f['inc']:.1f}" if isinstance(f["inc"], (int, float)) else "—"
            out.append(f"{f['sub']:<11} {f['nombre'][:48]:<48} {m:>9} {i:>7}  {f['fuente'] or '—'}")
        out.append("-" * 92)

    b = "**" if md else ""
    out.append(f"{b}Total definido:{b} {total:.1f} g ± {rss:.1f} g (RSS) · peor caso ± {peor:.1f} g")
    out.append("Por subsistema: " + ", ".join(f"{k} {v:.1f} g" for k, v in sorted(por_sub.items())))
    out.append(f"Requisito S1: {lo:.0f}–{hi:.0f} g")
    falta_lo, falta_hi = lo - total, hi - total
    if pendientes:
        out.append(f"Componentes pendientes (TBD): {len(pendientes)} → "
                   + ", ".join(sorted({f['sub'] for f in pendientes})))
        out.append(f"Quedan entre {max(falta_lo, 0):.1f} y {falta_hi:.1f} g para lo pendiente.")
    else:
        if lo <= total <= hi:
            out.append(f"Dentro de la ventana. Margen: {falta_hi:.1f} g hacia arriba, {total - lo:.1f} g hacia abajo.")
        elif total < lo:
            out.append(f"Faltan {falta_lo:.1f} g: agregar lastre (acero, no plomo).")
        else:
            out.append(f"Sobran {-falta_hi:.1f} g: hay que bajar masa.")
    if total + rss > hi:
        out.append("ATENCIÓN: con la incertidumbre (RSS), el total ya podría superar el máximo.")
    if sin_inc:
        out.append(f"Sin incertidumbre cargada: {len(sin_inc)} componente(s).")

    asig = cargar_asignacion()
    if asig:
        out.append("")
        out.append(f"{b}Contra la asignación por subsistema{b} (presupuestos/asignacion-masa.yaml):")
        if md:
            out += ["", "| Grupo | Asignado (g) | Cargado (g) | Pendientes | Estado |", "| --- | --- | --- | --- | --- |"]
        for g in asig:
            subs = g.get("subsistemas") or []
            if not subs:
                continue
            cargado = sum(por_sub.get(s, 0) for s in subs)
            pend = sum(1 for f in pendientes if f["sub"] in subs)
            asignado = g.get("masa_g") or 0
            if cargado > asignado:
                estado = f"EXCEDIDO por {cargado - asignado:.1f} g"
            else:
                estado = f"queda {asignado - cargado:.1f} g"
            if md:
                out.append(f"| {g['grupo']} | {asignado:.0f} | {cargado:.1f} | {pend} | {estado} |")
            else:
                out.append(f"  {g['grupo']:<24} asignado {asignado:>5.0f} g · cargado {cargado:>6.1f} g · "
                           f"{pend} pendiente(s) · {estado}")
    if errores:
        out.append("")
        out.append("Errores de formato:")
        out += [f"  - {e}" for e in errores]
    return "\n".join(out)


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--markdown", action="store_true", help="salida en Markdown")
    a = p.parse_args()
    filas, errores = cargar()
    print(texto(filas, errores, md=a.markdown))
    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()
