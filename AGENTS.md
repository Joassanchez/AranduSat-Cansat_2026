# AGENTS.md — Contexto para los agentes del proyecto AranduSat (CanSat 2026)

Este archivo lo leen todos los agentes que trabajan en el repo. Las reglas obligatorias están en `.agent/rules/`; los procedimientos, en `.agent/workflows/`.

## La misión y el plazo

Equipo AranduSat (Universidad de la Cuenca del Plata, Posadas) en el certamen **CanSat Universitario 2026/2027 de la CONAE**. Estamos en la **Etapa 2: Revisión Preliminar de Diseño (PDR)**.

- **Entrega del PDR: del 17 al 21 de noviembre de 2026**, solo en PDF, por el Aula Virtual, sobre la plantilla de la CONAE. Fuera de término o en otro formato, el equipo queda eliminado.
- Se puntúa con el Scoresheet V2: 127 ítems, 262 puntos (2 por ítem, 10 por la calidad de la presentación).
- La diapositiva 3 pide el link a un video de presentación.

Con el plazo tan corto, priorizá lo que suma puntos en el scoresheet: cada ítem de trade necesita 2+ opciones comparadas y una selección con criterios.

Resumen de la misión (fuente: `referencia/`):

- CanSat cilíndrico (S2: 90 mm de diámetro; S3: 200–250 mm de largo), 500 g ± 10 g (S1).
- Va dentro del fuselaje de un cohete que sube a más de 500 m (Bases §4) y sale con la carga de eyección (C1, C2).
- Desciende a 15 ± 3 m/s con un paracaídas automático (C3); al 80% de la altitud máxima libera otro sistema de descenso para bajar a 5 ± 3 m/s (C4).
- Transmite telemetría a 1 Hz (C5, X4), graba video a cenit y a nadir (C6, C7) y lleva una baliza audible independiente (C8).

## Supuestos de diseño vigentes

Vienen de la Guía (pestaña 1, "Resumen: propuestas iniciales"). Son propuestas del equipo, no requisitos: usalos para calcular y señalá cuando algo dependa de ellos.

| Tema | Supuesto | Qué puede cambiarlo |
| --- | --- | --- |
| Apogeo de diseño | 600 m para tiempos de descenso; 1.000 m como peor caso para enlace y memoria | Datos del cohete |
| Velocidad de la etapa 2 | 4,5 m/s (cumple las dos lecturas del promedio de C4) | Respuesta de la CONAE |
| Duración del descenso | ≈ 115 s (8 s a 15 m/s + ≈ 107 s a 4,5 m/s) | Apogeo real |
| Asignación de masa | Estructura 230 g, descenso 60 g, electrónica y sensores 120 g, potencia 70 g, margen 20 g | Componentes reales |
| Procesador | ESP32, con FreeRTOS o bucle con máquina de estados | Pruebas de tiempos (P5) |
| Radio | Banda 915–928 MHz, XBee-PRO 900HP o LoRa SX1276 | Decisión de P3 y P6 |
| Requisitos en conflicto | Diseñar según el Anexo A; adaptar las diapositivas del scoresheet que no coinciden | Respuesta de la CONAE |

## Quién es quién

Asignación según la Guía, §1.3. Cada carpeta de `subsistemas/` corresponde a una pestaña de la Guía.

| Carpeta | Pestaña de la Guía | Persona | Responsable | Responde por |
| --- | --- | --- | --- | --- |
| `subsistemas/sistema/` | 1, 2, 10, 11 | Integrador | _(a definir)_; gestión: Tabarez y Bojanovich | C9, misión, CONOPS, arquitectura, pruebas, gestión |
| `subsistemas/descenso/` | 4 | P1 | _(completar)_ | C3, C4 |
| `subsistemas/mecanica/` | 3 | P2 | Joaquín Sánchez | S1–S9, M1–M4, C1, C2, E5 |
| `subsistemas/sensores/` | 5 | P3 | Tabarez | SN1–SN8, C6, C7 |
| `subsistemas/cdh/` | 6 | P3 con P5 | Tabarez | C5, X1, X2, X4, X5, X6 |
| `subsistemas/eps/` | 7 | P4 | _(completar)_ | E1–E4, E6–E9, C8 |
| `subsistemas/fsw/` | 8 | P5 | _(completar)_ | F1–F5, X3 |
| `subsistemas/gcs/` | 9 | P6 | _(completar)_ | G1–G15 |

Los revisores oficiales están en `.github/CODEOWNERS`.

## Dónde está cada cosa

| Qué | Dónde |
| --- | --- |
| Inicio de la Guía: entregable, fechas, orden de trabajo | `pdr/guia-00-inicio.md` |
| Pestaña de la Guía de cada subsistema | `subsistemas/<subsistema>/guia-NN-*.md` |
| Bases, Anexo A y scoresheet (texto para leer) | `referencia/*.md` (originales en `referencia/originales/`) |
| Glosario y fuentes del equipo | `referencia/glosario-y-fuentes.md` |
| Requisitos con responsable y estado | `requisitos/requisitos.yaml` |
| Ítems del scoresheet y dónde se cubre cada uno | `pdr/trazabilidad.md` |
| Decisiones: registro y tabla de cumplimiento (pestaña 12) | `decisiones/` |
| Dudas y consultas a la CONAE (pestaña 13) | `consultas-conae.md` |
| Presupuesto de masa total | `python presupuestos/calc/masa_total.py` |

## Cómo se escribe cada subsección (formato de la Guía)

Todas las pestañas usan las mismas cinco partes. Respetalas al escribir:

1. **Qué pide:** requisitos del Anexo A e ítems del scoresheet. Ya está cargado: no se toca.
2. **Qué hay que entender:** conceptos, fórmulas, cálculos y links de donde sale cada dato.
3. **Opciones:** al menos dos alternativas con sus datos, en tabla. Es lo que el jurado puntúa como trade.
4. **Decisión:** la opción elegida en una o dos líneas, citando el requisito que cumple. Esa frase se registra en `decisiones/` y pasa casi igual a la diapositiva de selección.
5. **Pendientes:** lo que falta resolver o verificar. Cuando se resuelve, se borra o pasa a Decisión.

Orden de trabajo del equipo: misión y requisitos → arquitectura y masa → mecánica y descenso → sensores, C&DH y potencia → software de vuelo y estación terrena → pruebas, operaciones y gestión.

## Conflictos conocidos entre documentos

No los resuelvas por tu cuenta: la lista completa y su estado está en `consultas-conae.md`. Los principales:

- **Diámetro:** Bases §4 dice 95 mm; S2 dice 90 mm; el scoresheet habla de 136–140 mm (TBR).
- **Largo:** Bases §4 dice 200 mm; S3 dice 200–250 mm (TBR).
- **Scoresheet vs. Anexo A:** el scoresheet viene de CanSat USA y pide ojiva, huevo, cáncamo sobre disco de madera, parapente y separación de la carga útil, que el Anexo A no menciona.
- **Cantidad de requisitos:** el scoresheet habla de 55; el Anexo A v2 tiene 65.

## Roles de agente

- **Orquestador:** recibe la tarea, la divide, reparte, comenta en el issue y actualiza `ESTADO.md`.
- **Investigador:** busca alternativas con su fuente oficial (datasheet, fabricante).
- **Ingeniero:** verifica números (masa, consumo, dimensiones, velocidades) con scripts o cálculos explícitos.
- **Redactor:** completa Opciones, Decisión y Pendientes en la pestaña de la Guía y registra la decisión.
- **Crítico:** revisa en una conversación nueva, con el workflow `/critico`. Nunca revisa trabajo que él mismo produjo.

En la configuración inicial, un solo agente cumple los cuatro primeros roles. El crítico siempre es una sesión aparte.

## Idioma y estilo

Español rioplatense neutro, frases cortas, números con unidades y fuente. Unidades del SI: masas en gramos, energía en Wh, velocidades en m/s. Decimales con coma en el texto (2,5 mm) y con punto en YAML, paquetes, código y CSV.
