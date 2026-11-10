# CanSat Universitario 2026/27 — Repo del equipo

Repositorio de trabajo para el certamen CanSat Universitario de la CONAE. Acá vive todo el diseño en texto plano: cada integrante es dueño de su carpeta y trabaja con agentes de IA en Antigravity (Gemini) para investigar, calcular, redactar y revisar.

**Tres reglas:** el repo es la única fuente de verdad · los agentes proponen, las personas deciden · nada entra a `main` sin revisión.

## Estructura

```
cansat-2026/
├── README.md                 # esta guía
├── AGENTS.md                 # contexto de la misión para los agentes
├── .agent/
│   ├── rules/                # reglas que todo agente respeta
│   └── workflows/            # /empezar, /trade, /calcular, /critico, /cerrar
├── .github/                  # CODEOWNERS y plantillas de issue y PR
├── referencia/               # Bases, Anexo A y scoresheet en Markdown (+ originales)
├── requisitos/requisitos.yaml   # los 65 requisitos con estado y responsable
├── decisiones/               # una decisión de diseño por archivo
├── subsistemas/
│   ├── sistema/              # transversal: CONOPS, layout, I&T, gestión
│   ├── sensores/  descenso/  mecanica/  cdh/  eps/  fsw/  gcs/
│   │   ├── README.md  ESTADO.md  masa.yaml
│   │   ├── trades/  figuras/  (cad/)
├── presupuestos/calc/        # masa_total.py: suma los masa.yaml
└── pdr/                      # trazabilidad.md y ensamblado final
```

Los subsistemas siguen la división de la plantilla PDR de la CONAE (ver el anexo de `subsistemas/mecanica/seccion-2-mecanica.md`).

## Puesta en marcha (una sola vez)

**El integrador:**

1. Crea el repo en GitHub (privado), sube esta carpeta y suma a los compañeros con permiso de escritura.
   ```bash
   cd cansat-2026
   git init -b main
   git add .
   git commit -m "Estructura inicial del repo"
   git remote add origin https://github.com/<usuario>/cansat-2026.git
   git push -u origin main
   ```
2. Reemplaza los `@usuario-...` de `.github/CODEOWNERS` y la tabla de dueños de `AGENTS.md`.
3. Protege `main` en *Settings → Branches*: exigir Pull Request y 1 aprobación. En repos privados requiere GitHub Pro, gratis con el GitHub Student Developer Pack. Al principio, **sin** "Require review from Code Owners"; se activa cuando el equipo ya esté cómodo.
4. Crea las etiquetas de subsistema (`sistema`, `mecanica`, `sensores`, `descenso`, `cdh`, `eps`, `fsw`, `gcs`).

**Cada integrante:**

```bash
git clone https://github.com/<usuario>/cansat-2026.git
cd cansat-2026
pip install -r requirements.txt
gh auth login        # para que el agente pueda comentar en issues
```

Abre la carpeta en Antigravity. El agente toma las reglas de `.agent/rules/` y los workflows de `.agent/workflows/`. Si tu versión de Antigravity usa otra ruta para reglas o workflows, movelas ahí y avisá al equipo.

## Cómo trabajamos

### Una tarea de punta a punta

1. **Issue:** creá un issue con la plantilla "Tarea", asignado a vos, con la etiqueta de tu subsistema y los ítems P.. de `pdr/trazabilidad.md` que cubre.
2. **Rama y Draft PR:**
   ```bash
   git switch main && git pull
   git switch -c mecanica/trade-cono
   git push -u origin mecanica/trade-cono
   ```
   En GitHub, abrí el PR como **Draft** con `Closes #<issue>`.
3. **Agente:** en Antigravity, `/empezar` con el número de issue. El orquestador arma un plan, te lo muestra y comenta en el issue.
4. **Trabajo:** el agente usa `/trade` y `/calcular` y hace commits. Vos revisás y hacés `git push` seguido.
5. **Crítico:** abrí una **conversación nueva** y corré `/critico`. Pegá el informe en el PR. Si hay bloqueantes, se corrige y se repite.
6. **Cierre:** `/cerrar`, pasá el PR a *Ready for review* y pedí la revisión de un compañero. Después del merge, borrá la rama.

Si mientras trabajás necesitás lo que otros mergearon: `git pull origin main`.

### Los agentes

| Rol | Qué hace | Workflow |
| --- | --- | --- |
| Orquestador | Planifica, reparte, comenta en el issue, actualiza `ESTADO.md` | `/empezar`, `/cerrar` |
| Investigador | Busca alternativas con su datasheet | `/trade` (paso 2) |
| Ingeniero | Verifica masa, consumo, dimensiones, velocidades | `/trade` (paso 3), `/calcular` |
| Redactor | Escribe el trade y la decisión | `/trade` (paso 4) |
| Crítico | Revisa contra scoresheet, requisitos y fuentes, sin haber visto el trabajo | `/critico` |

Configuración inicial: un agente principal hace los cuatro primeros roles; el crítico siempre en una conversación aparte. Si la investigación se vuelve el cuello de botella, se separa el investigador y se corren búsquedas en paralelo desde el Agent Manager.

### Seguimiento

- **Issue** = qué hay que hacer y quién. El agente comenta solo al empezar, si se bloquea y al terminar, siempre con `🤖 Agente:`.
- **Draft PR** = cómo va: cada commit es avance.
- **`ESTADO.md`** de cada carpeta = resumen de hecho, falta y bloqueado.
- **`pdr/trazabilidad.md`** = qué ítems del scoresheet están cubiertos.

## Reglas del equipo

- Nadie trabaja directo en `main`.
- No se modifican carpetas ajenas; si hace falta, se abre un PR que revisa el dueño.
- Ramas cortas, una por tarea: `<subsistema>/<tarea>`.
- Commits con prefijo: `mecanica: …`.
- Decisiones con fecha y tema en el nombre, nunca con número correlativo.
- CAD: en el repo solo exportaciones (STEP, STL, PNG); los nativos en Drive con el link en `cad/README.md`. GitHub rechaza archivos de más de 100 MB.
- Masa: cada subsistema en su `masa.yaml`; el total con `python presupuestos/calc/masa_total.py`.
- PRs chicos: idealmente un trade por PR.

## Dueños (CODEOWNERS)

`.github/CODEOWNERS` no limita quién puede editar: decide quién **revisa**. Cuando un PR toca una carpeta, GitHub agrega a su dueño como revisor. Gana la última regla que coincide. Para reasignar, se edita el archivo y se abre un PR. Si alguien deja el equipo, se reasigna su carpeta enseguida.

## Preguntas abiertas para la organización

Las principales están en `subsistemas/mecanica/seccion-2-mecanica.md` (sección "Preguntas abiertas para la organización") y los conflictos entre documentos, en `AGENTS.md`. Pendiente: **quién es el integrador del PDR**.
