---
description: Completar una subsección de la Guía con un trade (2+ opciones comparadas y una decisión)
---

# /trade — opciones y decisión de una subsección

Roles: **investigador → ingeniero → redactor**. Entrada: la subsección de la Guía (por ejemplo `3.2 Estructura de la carga útil`) y los ítems del scoresheet (P..) que cubre.

Se trabaja sobre la pestaña de la Guía del subsistema (`subsistemas/<subsistema>/guia-NN-*.md`), respetando sus cinco partes: Qué pide · Qué hay que entender · Opciones · Decisión · Pendientes.

## 1. Entender qué pide el jurado

- Leé el **Qué pide** de la subsección (no se modifica).
- Leé la fila del ítem en `referencia/scoresheet.md` (columna "Qué espera el jurado") y los requisitos en `referencia/anexo-a.md`.
- Revisá los supuestos de diseño de `AGENTS.md` y si hay una consulta abierta en `consultas-conae.md` que afecte la subsección.
- Anotá los criterios de selección y su peso **antes** de buscar opciones, para no ajustarlos a una opción favorita.

## 2. Investigar (investigador) → "Qué hay que entender"

- Conceptos, fórmulas y datos que hacen falta para comparar, cada uno con su link.
- Buscá **al menos 3 alternativas** reales que se consigan en Argentina o por courier: modelo, specs relevantes al ítem, masa, dimensiones, consumo si aplica, precio aproximado y **link al datasheet**.
- Descartá las que violen un requisito, diciendo cuál (por ejemplo, LiPo → E1).

## 3. Verificar (ingeniero)

- Comprobá con números que cada alternativa cumpla los requisitos: rango, masa, consumo, interfaz.
- Si el cálculo es repetible, dejalo como script en `subsistemas/<subsistema>/` o en `presupuestos/calc/`.

## 4. Escribir (redactor) → "Opciones", "Decisión", "Pendientes"

- **Opciones:** completá la tabla de la subsección (mínimo 2 filas) con datos y fuente. Si la comparación es larga, agregá una matriz de decisión ponderada (criterio, peso, puntaje 1–5, total). Si no entra cómoda en la Guía, ponela en `subsistemas/<subsistema>/trades/AAAA-MM-DD-<tema>.md` y enlazala desde la subsección.
- **Decisión:** una o dos líneas con la opción elegida y por qué, citando el requisito que cumple. Ejemplo de formato: "Paracaídas hemisférico de 30 cm de nylon: con 500 g da 14 m/s, dentro de C3 (15 ± 3 m/s), y es el más fácil de plegar."
- **Pendientes:** lo que queda por verificar (pruebas, datos de otro subsistema, respuesta de la CONAE). Si surge una duda para la organización, agregala a `consultas-conae.md`.

Después:

- Agregá la decisión al **Registro de decisiones** de `decisiones/guia-12-decisiones-y-cumplimiento.md` (fecha, decisión, alternativas descartadas, requisitos, "propuesto por <persona> + agente").
- Si la opción elegida suma masa, cargala en el `masa.yaml` del subsistema y corré `/calcular`.
- Commit: `<subsistema>: completa <subsección>`.
