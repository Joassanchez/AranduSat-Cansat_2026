# Alcance y Git

Contexto completo del proyecto: leé `AGENTS.md` en la raíz antes de empezar.

## Alcance

- Al empezar cada sesión, confirmá con la persona en qué **rama** y en qué **carpeta de subsistema** vas a trabajar. Si no lo sabés, preguntá antes de tocar archivos.
- Solo modificás archivos dentro de `subsistemas/<tu-subsistema>/` y `decisiones/`. Cualquier otro archivo (requisitos, trazabilidad, carpetas de otros, configuración) solo con pedido explícito de la persona.
- `referencia/` es de solo lectura.

## Git

- Nunca trabajás en `main`, nunca hacés merge ni rebase de `main`, nunca usás `push --force`.
- La rama se llama `<subsistema>/<tarea-corta>` (por ejemplo `mecanica/trade-cono`).
- Commits chicos y frecuentes, con el prefijo del subsistema: `mecanica: agrega trade de cono con 2 alternativas`.
- Hacés commits; el `push` y el cambio del PR a "listo para revisión" los hace la persona, salvo que te lo pida.
- No subas archivos de más de 50 MB ni archivos nativos de CAD (van en Drive con el link en `cad/README.md`).
