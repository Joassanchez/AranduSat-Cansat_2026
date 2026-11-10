# Decisiones de diseño

Una decisión por archivo, con la plantilla [`_plantilla.md`](_plantilla.md).

- **Nombre:** `AAAA-MM-DD-<subsistema>-<tema>.md` (por ejemplo `2026-11-10-mecanica-material-tubo.md`). Nunca numeración correlativa: así dos personas no chocan.
- **Estados:** `propuesto` → `aceptado` (solo una persona) → eventualmente `reemplazado por <archivo>`.
- Una decisión aceptada no se edita: si cambia, se crea una nueva y la vieja pasa a `reemplazado`.
- Cualquiera puede crear decisiones de su subsistema; las que afectan a otros subsistemas las aprueba también el dueño afectado en el PR.

Estas decisiones son las que alimentan las diapositivas de "Selection (with criteria)" del PDR.
