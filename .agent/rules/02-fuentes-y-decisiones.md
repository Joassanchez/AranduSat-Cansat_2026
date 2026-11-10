# Fuentes y decisiones

## Fuentes

- Toda especificación de un componente (masa, dimensiones, consumo, rango, precio) lleva el **link a su fuente**: datasheet o página oficial del fabricante. Sin fuente, el dato no entra.
- Si no encontrás un dato, escribilo en **Pendientes** como `TBD: …`. Nunca lo estimes en silencio. Si estimás, marcalo `estimado` y explicá cómo.
- Los requisitos del Anexo A (`referencia/anexo-a.md`) son límites duros. Citalos siempre por su ID (S1, C4, E5…).
- Ante una diferencia entre un `.md` de `referencia/` y su PDF en `referencia/originales/`, manda el PDF.
- Los supuestos de diseño vigentes están en `AGENTS.md`. Si un cálculo depende de uno, decilo.
- Los conflictos entre Bases, Anexo y scoresheet están en `consultas-conae.md`. No los resuelvas por tu cuenta: señalalos y, si encontrás uno nuevo, agregalo ahí.

## Números

- Unidades del SI siempre, con la unidad escrita: masas en gramos, energía en Wh, velocidades en m/s.
- Todo cálculo que entra al PDR queda reproducible: fórmula y valores en el texto, o un script en el repo.
- Las masas van en el `masa.yaml` del subsistema, con incertidumbre y fuente.

## Decisiones

- La sección **Qué pide** de cada subsección de la Guía no se modifica.
- Toda decisión se escribe en la subsección (**Decisión**, una o dos líneas citando el requisito) y se agrega al **Registro de decisiones** de `decisiones/guia-12-decisiones-y-cumplimiento.md`.
- Las decisiones de mucho impacto (las que afectan a otros subsistemas, como la configuración general, el material del tubo o la radio) además llevan un archivo propio en `decisiones/` con `_plantilla.md`, nombrado `AAAA-MM-DD-<subsistema>-<tema>.md`.
- Toda decisión que escribe un agente queda como **propuesta**. Solo una persona la acepta.
- Una decisión aceptada no se reabre sin pedido de la persona. Si encontrás información que la contradice, avisá y proponé una nueva.
