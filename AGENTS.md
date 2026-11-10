# AGENTS.md — Contexto para los agentes del proyecto CanSat 2026

Este archivo lo leen todos los agentes que trabajan en el repo. Las reglas obligatorias están en `.agent/rules/`; los procedimientos, en `.agent/workflows/`.

## La misión

Equipo universitario (Universidad de la Cuenca del Plata, Posadas) en el certamen **CanSat Universitario 2026/2027 de la CONAE**. Estamos en la **Etapa 2: Revisión Preliminar de Diseño (PDR)**: un paquete de diapositivas en PDF, hecho con la plantilla de la CONAE y evaluado con el scoresheet.

Resumen de la misión (fuente: `referencia/`):

- CanSat cilíndrico (S2: 90 mm de diámetro; S3: 200–250 mm de largo), 500 g ± 10 g (S1).
- Va dentro del fuselaje de un cohete que sube a más de 500 m (Bases §4) y sale con la carga de eyección (C1, C2).
- Desciende a 15 ± 3 m/s con un paracaídas automático (C3); al 80% de la altitud máxima libera otro sistema de descenso para bajar a 5 ± 3 m/s (C4).
- Transmite telemetría a 1 Hz (C5, X4), graba video a cenit y a nadir (C6, C7) y lleva una baliza audible independiente (C8).

## Dónde está cada cosa

| Qué | Dónde |
| --- | --- |
| Bases, Anexo A y scoresheet (texto para leer) | `referencia/*.md` |
| Documentos oficiales originales (mandan ante cualquier duda) | `referencia/originales/` |
| Requisitos con estado y responsable | `requisitos/requisitos.yaml` |
| Ítems del scoresheet y dónde se cubre cada uno | `pdr/trazabilidad.md` |
| Trabajo de cada subsistema | `subsistemas/<subsistema>/` |
| Decisiones de diseño | `decisiones/` |
| Presupuesto de masa total | `python presupuestos/calc/masa_total.py` |

## Dueños de carpetas

| Carpeta | Dueño |
| --- | --- |
| `subsistemas/sistema/`, `requisitos/`, `pdr/` | _(integrador: completar)_ |
| `subsistemas/mecanica/` | Joaquín |
| `subsistemas/sensores/` | _(completar)_ |
| `subsistemas/descenso/` | _(completar)_ |
| `subsistemas/cdh/` | _(completar)_ |
| `subsistemas/eps/` | _(completar)_ |
| `subsistemas/fsw/` | _(completar)_ |
| `subsistemas/gcs/` | _(completar)_ |

La fuente oficial de dueños es `.github/CODEOWNERS`; mantener esta tabla igual.

## Conflictos conocidos entre documentos

No los resuelvas por tu cuenta: señalalos y respetá la lectura de trabajo.

- **Diámetro:** Bases §4 dice 95 mm; S2 dice 90 mm. Lectura de trabajo: 95 mm es el espacio del cohete y 90 mm el máximo del CanSat (TBR).
- **Largo:** Bases §4 dice 200 mm; S3 dice 200–250 mm (TBR).
- **Scoresheet vs. Anexo A:** el scoresheet está adaptado de CanSat USA y pide ojiva, huevo, cáncamo sobre disco de madera, parapente y separación de la carga útil, que el Anexo A no menciona. Pendiente de consulta a la organización.
- **Cantidad de requisitos:** el scoresheet habla de 55; el Anexo A v2 tiene 65.

## Roles de agente

- **Orquestador:** recibe la tarea, la divide, reparte, comenta en el issue y actualiza `ESTADO.md`.
- **Investigador:** busca alternativas con su fuente oficial (datasheet, fabricante).
- **Ingeniero:** verifica números (masa, consumo, dimensiones, velocidades) con scripts o cálculos explícitos.
- **Redactor:** escribe el trade en `trades/` y la decisión en `decisiones/`.
- **Crítico:** revisa en una conversación nueva, con el workflow `/critico`. Nunca revisa trabajo que él mismo produjo.

En la configuración inicial, un solo agente cumple los cuatro primeros roles. El crítico siempre es una sesión aparte.

## Idioma y estilo

Todo en español rioplatense neutro, frases cortas, números con unidades y fuente. Decimales con coma en el texto (2,5 mm) y con punto en YAML y código.
