---
description: Cerrar una tarea después de que el crítico la aprobó (rol orquestador)
---

# /cerrar — cerrar la tarea

Rol: **orquestador**. Solo después de un veredicto "Aprobado" o "Aprobado con cambios menores" del crítico (con los cambios hechos).

1. Actualizá `subsistemas/<subsistema>/ESTADO.md` con lo hecho y la fecha.
2. Prepará para la persona la actualización de `pdr/trazabilidad.md`: qué filas P.. pasan a `borrador` o `listo` y la ruta donde se cubre cada una. Aplicala solo si la persona lo pide.
3. Hacé el último commit: `<subsistema>: cierra <tarea>`.
4. Comentá en el issue: `🤖 Agente: terminado. Cubre P.. Decisiones propuestas: … Falta que una persona las acepte. PR #..`.
5. Recordale a la persona: push, pasar el PR de Draft a "Ready for review", pegar el informe del crítico y pedir la revisión de un compañero.
