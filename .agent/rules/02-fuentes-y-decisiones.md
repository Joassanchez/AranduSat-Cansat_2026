# Fuentes y decisiones

## Fuentes

- Toda especificación de un componente (masa, dimensiones, consumo, rango, precio) lleva el **link a su fuente**: datasheet o página oficial del fabricante. Sin fuente, el dato no entra.
- Si no encontrás un dato, escribilo como pregunta abierta (`TBD: …`). Nunca lo estimes en silencio. Si estimás, marcalo `estimado` y explicá cómo.
- Los requisitos del Anexo A (`referencia/anexo-a.md`) son límites duros. Citalos siempre por su ID (S1, C4, E5…).
- Ante una diferencia entre un `.md` de `referencia/` y su PDF en `referencia/originales/`, manda el PDF.
- Los conflictos conocidos entre Bases, Anexo y scoresheet están en `AGENTS.md`. No los resuelvas por tu cuenta: señalalos.

## Números

- Unidades del SI siempre, con la unidad escrita.
- Todo cálculo que entra al PDR queda reproducible: fórmula y valores en el texto, o un script en el repo.
- Las masas van en el `masa.yaml` del subsistema, con incertidumbre y fuente.

## Decisiones

- Toda selección de un trade genera un archivo en `decisiones/` con la plantilla `decisiones/_plantilla.md`.
- Nombre: `AAAA-MM-DD-<subsistema>-<tema>.md`. Nunca numeración correlativa.
- Se crean en estado `propuesto`. **Solo una persona las pasa a `aceptado`.**
- Una decisión `aceptada` no se reabre sin pedido de la persona. Si encontrás información que la contradice, avisá y proponé una nueva que la reemplace.
