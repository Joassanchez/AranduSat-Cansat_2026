# Comunicación y seguimiento

## Issues

Cada tarea tiene un issue en GitHub asignado a una persona. Comentás en el issue solo en tres momentos:

1. **Al empezar:** qué vas a hacer, en qué rama y qué ítems del scoresheet cubre.
2. **Si te bloqueás:** qué falta y qué necesitás de una persona.
3. **Al terminar:** resumen de lo hecho y link al PR.

Cada comentario empieza con `🤖 Agente:`, porque se publica con el usuario de GitHub de la persona y el equipo tiene que distinguirlo.

Para comentar usás el CLI `gh` autenticado (`gh issue comment <número> --body "..."`) o el servidor MCP de GitHub, si está configurado. Si no tenés acceso, dejale el texto del comentario a la persona para que lo pegue.

## Pull Requests

- La persona abre el PR como **Draft** apenas crea la rama, con `Closes #<issue>` en la descripción.
- El informe del crítico se pega como comentario en el PR.

## Estado

Al cerrar cada tarea, actualizá `subsistemas/<tu-subsistema>/ESTADO.md` (hecho, en curso, falta, bloqueado) con la fecha. Si cambia el estado de la pestaña, proponé también el cambio en la tabla "Estado por pestaña" de `pdr/guia-00-inicio.md`.

Si la tarea cubre ítems del scoresheet, proponé a la persona la actualización de sus filas en `pdr/trazabilidad.md` (estado y ruta). Ese archivo es del integrador: no lo edites sin que te lo pidan.
