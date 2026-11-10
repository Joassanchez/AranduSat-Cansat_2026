# 8. Software de vuelo

> Pestaña 8 de la *PDR CanSat Universitario – Guía de desarrollo* (Google Docs), migrada al repo el 10/11/2026. Desde la migración se edita acá; ver la sección "La Guía de Drive y el repo" del README.

El programa que corre en el CanSat: lee sensores, decide en qué fase está, activa mecanismos, guarda y transmite. Tiene que recuperarse solo si el procesador se reinicia en pleno vuelo.

## 8.1 Arquitectura

Tareas del software, diagrama de flujo general, lenguaje y entorno de desarrollo.

**Qué pide:** Scoresheet ítem 66 *FSW Overview*.

**Qué hay que entender:** —

**Decisión:** lenguaje, entorno y diagrama de flujo —

**Pendientes:** —

## 8.2 Diagrama de estados

Los estados del software (por ejemplo: espera en rampa, ascenso, primer descenso, segundo descenso, aterrizado) y la condición que dispara cada transición. Incluye frecuencia de muestreo de cada sensor, comunicaciones, almacenamiento, activación de mecanismos y manejo de energía.

**Qué pide:** C3, C4, X3 · Scoresheet ítem 67 *Payload FSW State Diagram*.

**Qué hay que entender:** —

| Estado | Qué hace | Condición para pasar al siguiente |
| --- | --- | --- |
|   |   |   |

**Pendientes:** —

## 8.3 Recuperación ante reinicios

Qué datos se guardan en memoria no volátil y cómo vuelve el software al estado correcto después de un reinicio.

**Qué pide:** F1, F2, F5 · parte del ítem 67.

**Decisión:** —

**Pendientes:** —

## 8.4 Modo simulación

Un modo en el que el CanSat usa datos de presión enviados desde tierra en lugar del sensor real, para probar toda la secuencia sin volar.

**Qué pide:** Scoresheet *Simulation Mode Software* *(sin diapositiva)*.

**Decisión:** —

**Pendientes:** —

## 8.5 Plan de desarrollo

Prototipos, orden en que se desarrollan los módulos, quién programa cada parte y cómo se prueba.

**Qué pide:** Scoresheet ítem 68 *Software Development Plan*.

**Decisión:** —

**Pendientes:** —
