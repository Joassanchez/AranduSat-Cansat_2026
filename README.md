# AranduSat — CanSat Universitario 2026/27

Repositorio de trabajo del equipo AranduSat para el certamen CanSat Universitario de la CONAE. Acá vive todo el diseño en texto plano: la **Guía de desarrollo** del equipo, repartida en una carpeta por subsistema, más los requisitos, el scoresheet y las decisiones. Cada integrante es dueño de su carpeta y trabaja con agentes de IA en Antigravity (Gemini) para investigar, calcular, redactar y revisar.

**Entrega del PDR: del 17 al 21 de noviembre de 2026**, en PDF, por el Aula Virtual.

**Tres reglas:** el repo es la única fuente de verdad · los agentes proponen, las personas deciden · nada entra a `main` sin revisión.

## Estructura

Cada carpeta de `subsistemas/` es una pestaña de la Guía de desarrollo:

```
AranduSat-Cansat_2026/
├── README.md                 # esta guía
├── AGENTS.md                 # misión, plazo, supuestos y quién es quién, para los agentes
├── consultas-conae.md        # pestaña 13: dudas y contradicciones a consultar
├── .agent/
│   ├── rules/                # reglas que todo agente respeta
│   └── workflows/            # /empezar, /trade, /calcular, /critico, /cerrar
├── .github/                  # CODEOWNERS y plantillas de issue y PR
├── referencia/               # Bases, Anexo A, scoresheet, glosario (pestaña 14) + originales
├── requisitos/requisitos.yaml   # los 65 requisitos con subsistema, persona y estado
├── decisiones/               # pestaña 12: registro de decisiones y tabla de cumplimiento
├── subsistemas/
│   ├── sistema/              # pestañas 1, 2, 10 y 11: misión, arquitectura, pruebas, gestión
│   ├── mecanica/             # pestaña 3 · P2
│   ├── descenso/             # pestaña 4 · P1
│   ├── sensores/             # pestaña 5 · P3
│   ├── cdh/                  # pestaña 6 · P3 con P5 (procesador, memoria, radio, telemetría)
│   ├── eps/                  # pestaña 7 · P4 (potencia)
│   ├── fsw/                  # pestaña 8 · P5 (software de vuelo)
│   └── gcs/                  # pestaña 9 · P6 (estación terrena)
│       └── guia-NN-*.md  README.md  ESTADO.md  masa.yaml  trades/  figuras/  (cad/)
├── presupuestos/             # masa: asignación por subsistema y script que suma
└── pdr/                      # pestaña 0 (inicio), trazabilidad del scoresheet y ensamblado final
```

Los nombres de las carpetas son los de la plantilla PDR de la CONAE, los mismos que usa la Guía: C&DH es *Command and Data Handling* (procesamiento y comunicaciones), EPS es *Electrical Power Subsystem*, FSW es *Flight Software* y GCS es *Ground Control Station*.

## La Guía de Drive y el repo

La Guía de desarrollo (Google Docs) se migró al repo el 10/11/2026: cada pestaña quedó como un archivo `guia-NN-*.md` con el mismo formato (Qué pide · Qué hay que entender · Opciones · Decisión · Pendientes). Para no tener dos versiones que se contradigan:

- **Desde la migración se edita en el repo.** En la Guía de Drive conviene poner arriba un aviso "Migrada a GitHub, no editar" y dejarla como lectura.
- Quien no use Git puede editar los `.md` desde la web de GitHub: el lápiz de "Edit" crea la rama y el PR solo.
- Si alguien igual escribe en Drive, el dueño de esa pestaña pasa el cambio al repo en su próximo PR.
- La Sección 2 de mecánica y las investigaciones por persona son el respaldo detallado; la Guía es la versión resumida que va a las diapositivas.

## Puesta en marcha (una sola vez)

**El integrador:**

1. Crea el repo en GitHub (privado), sube esta carpeta y suma a los compañeros con permiso de escritura.
   ```bash
   cd AranduSat-Cansat_2026
   git init -b main
   git add .
   git commit -m "Estructura inicial del repo"
   git remote add origin https://github.com/Joassanchez/AranduSat-Cansat_2026.git
   git push -u origin main
   ```
2. Reemplaza los `@usuario-...` de `.github/CODEOWNERS` y la tabla de dueños de `AGENTS.md`.
3. Protege `main` en *Settings → Branches*: exigir Pull Request y 1 aprobación. En repos privados requiere GitHub Pro, gratis con el GitHub Student Developer Pack. Al principio, **sin** "Require review from Code Owners"; se activa cuando el equipo ya esté cómodo.
4. Crea las etiquetas de subsistema (`sistema`, `mecanica`, `sensores`, `descenso`, `cdh`, `eps`, `fsw`, `gcs`).

**Cada integrante:**

```bash
git clone https://github.com/Joassanchez/AranduSat-Cansat_2026.git
cd AranduSat-Cansat_2026
pip install -r requirements.txt
gh auth login        # para que el agente pueda comentar en issues
```

Abre la carpeta en Antigravity. El agente toma las reglas de `.agent/rules/` y los workflows de `.agent/workflows/`. Si tu versión de Antigravity usa otra ruta para reglas o workflows, movelas ahí y avisá al equipo.

## Cómo trabajamos

### Por dónde empezar

El orden de trabajo de la Guía: misión y requisitos (pestaña 1) → arquitectura y masa (2) → mecánica y descenso (3 y 4) → sensores, C&DH y potencia (5 a 7) → software de vuelo y estación terrena (8 y 9) → pruebas, operaciones y gestión (10 y 11).

La decisión que destraba a todos es la **configuración general** (pestaña 2: opción A separable o B cuerpo único), que depende de la respuesta de la CONAE sobre si manda el Anexo A o el scoresheet. Por eso, lo primero es mandar las consultas de `consultas-conae.md` por el Aula Virtual.

### Una tarea de punta a punta

Una tarea suele ser una subsección de la Guía (por ejemplo "3.2 Estructura de la carga útil").

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
| Redactor | Completa Opciones, Decisión y Pendientes en la pestaña de la Guía | `/trade` (paso 4) |
| Crítico | Revisa contra scoresheet, requisitos y fuentes, sin haber visto el trabajo | `/critico` |

Configuración inicial: un agente principal hace los cuatro primeros roles; el crítico siempre en una conversación aparte. Si la investigación se vuelve el cuello de botella, se separa el investigador y se corren búsquedas en paralelo desde el Agent Manager.

### Seguimiento

- **Issue** = qué hay que hacer y quién. El agente comenta solo al empezar, si se bloquea y al terminar, siempre con `🤖 Agente:`.
- **Draft PR** = cómo va: cada commit es avance.
- **`ESTADO.md`** de cada carpeta = resumen de hecho, falta y bloqueado.
- **`pdr/trazabilidad.md`** = qué ítems del scoresheet están cubiertos.
- **"Estado por pestaña"** en `pdr/guia-00-inicio.md` = el tablero general, igual que en la Guía de Drive.

## Reglas del equipo

- Nadie trabaja directo en `main`.
- No se modifican carpetas ajenas; si hace falta, se abre un PR que revisa el dueño.
- Ramas cortas, una por tarea: `<subsistema>/<tarea>`.
- Commits con prefijo: `mecanica: …`.
- La parte "Qué pide" de cada subsección no se toca.
- Cada decisión cita el requisito que cumple y se anota en el registro de `decisiones/` (pestaña 12).
- Cada contradicción o duda con la CONAE va a `consultas-conae.md` (pestaña 13).
- Unidades del SI: masas en gramos, energía en Wh, velocidades en m/s.
- Los ítems marcados *(sin diapositiva)* los puntúa el scoresheet pero la plantilla no los trae: hay que agregar esas diapositivas.
- CAD: en el repo solo exportaciones (STEP, STL, PNG); los nativos en Drive con el link en `cad/README.md`. GitHub rechaza archivos de más de 100 MB.
- Masa: cada subsistema en su `masa.yaml`; el total y la comparación con la asignación de cada subsistema, con `python presupuestos/calc/masa_total.py`.
- PRs chicos: idealmente un trade por PR.

## Dueños (CODEOWNERS)

`.github/CODEOWNERS` no limita quién puede editar: decide quién **revisa**. Cuando un PR toca una carpeta, GitHub agrega a su dueño como revisor. Gana la última regla que coincide. Para reasignar, se edita el archivo y se abre un PR. Si alguien deja el equipo, se reasigna su carpeta enseguida.

## Preguntas abiertas

- Para la organización: `consultas-conae.md` (pestaña 13). La Sección 2 de mecánica tiene además sus preguntas específicas.
- Para el equipo: **quién es el integrador del PDR** y los responsables de descenso, potencia, software de vuelo y estación terrena (ver `AGENTS.md`).
