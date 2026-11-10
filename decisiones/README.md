# Decisiones de diseño

Es la pestaña 12 de la Guía.

- [`guia-12-decisiones-y-cumplimiento.md`](guia-12-decisiones-y-cumplimiento.md): la **tabla de cumplimiento** y el **registro de decisiones**. Toda decisión, chica o grande, tiene una fila en el registro.
- Las decisiones de mucho impacto (las que afectan a otros subsistemas) llevan además un archivo propio con la plantilla [`_plantilla.md`](_plantilla.md), nombrado `AAAA-MM-DD-<subsistema>-<tema>.md`. Nunca numeración correlativa: así dos personas no chocan.

Estados de un archivo de decisión: `propuesto` → `aceptado` (solo una persona) → eventualmente `reemplazado por <archivo>`. Una decisión aceptada no se edita: si cambia, se crea una nueva y la vieja pasa a `reemplazado`.

Estas decisiones alimentan las diapositivas de "Selection (with criteria)" del PDR.
