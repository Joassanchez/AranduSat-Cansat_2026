---
description: Arrancar una tarea nueva desde un issue (rol orquestador)
---

# /empezar — arrancar una tarea

Rol: **orquestador**. La persona te pasa el número de issue.

1. Leé el issue (`gh issue view <número>`) y `AGENTS.md`.
2. Confirmá con la persona la rama y la carpeta de subsistema. Verificá con `git branch --show-current` que no estés en `main`.
3. Buscá en `pdr/trazabilidad.md` qué ítems del scoresheet cubre la tarea, y en `requisitos/requisitos.yaml` qué requisitos toca.
4. Leé `subsistemas/<subsistema>/ESTADO.md` y las decisiones de `decisiones/` del subsistema, para no repetir trabajo ni reabrir decisiones aceptadas.
5. Armá un plan de 3 a 7 pasos: qué investigar, qué calcular, qué escribir. Mostráselo a la persona y esperá su visto bueno.
6. Comentá en el issue: `🤖 Agente: empiezo. Rama <rama>. Cubre <ítems P..>. Plan: …`.
7. Ejecutá el plan. Para trades usá `/trade`; para números, `/calcular`.
8. Al terminar, pedile a la persona que corra `/critico` en una **conversación nueva** y, cuando esté aprobado, usá `/cerrar`.
