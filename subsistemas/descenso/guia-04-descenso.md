# 4. Control de descenso

> Pestaña 4 de la *PDR CanSat Universitario – Guía de desarrollo* (Google Docs), migrada al repo el 10/11/2026. Desde la migración se edita acá; ver la sección "La Guía de Drive y el repo" del README.

Cómo baja el CanSat en dos etapas: primero a 15 ± 3 m/s con paracaídas y, desde el 80 % de la altura máxima, a 5 ± 3 m/s con un segundo sistema. Lo mecánico del guardado y despliegue está en la pestaña 3 (3.7).

## 4.1 Visión general

Resumen de la configuración de descenso elegida para cada etapa.

**Qué pide:** C3, C4 · Scoresheet ítem 32 *Descent Control Subsystem Overview*.

**Decisión:** —

**Pendientes:** —

## 4.2 Paracaídas principal

Dos diseños de paracaídas para la primera etapa (forma, diámetro, material) y la selección.

**Qué pide:** C3 · Scoresheet ítems 33 y 34.

**Qué hay que entender:** —

**Opciones:**

| Diseño | Forma y diámetro | Cd estimado | Velocidad (m/s) | A favor | En contra |
| --- | --- | --- | --- | --- | --- |
| A |   |   |   |   |   |
| B |   |   |   |   |   |

**Decisión:** —

**Pendientes:** —

## 4.3 Segundo sistema de descenso

Lo que se libera al 80 % de la altura máxima para bajar a 5 m/s. La plantilla asume un para-glider con control de dirección; el Anexo A solo pide "otro sistema de descenso".

**Qué pide:** C4 · Scoresheet ítems 35 y 36, y *Descent speed control* *(sin diapositiva)*: dos estrategias de control de velocidad.

**Qué hay que entender:** —

**Opciones:**

| Sistema | Cómo funciona | Velocidad (m/s) | A favor | En contra |
| --- | --- | --- | --- | --- |
| A |   |   |   |   |
| B |   |   |   |   |

**Decisión:** —

**Pendientes:** ¿es obligatorio un para-glider? Ver pestaña 13.

## 4.4 Estabilidad: pasiva o activa

Si el CanSat se estabiliza solo por su forma o si hay un control que corrige (servos, superficies).

**Qué pide:** Scoresheet *Identify passive or active control* *(sin diapositiva)*.

**Decisión:** —

**Pendientes:** —

## 4.5 Cálculo de velocidades de descenso

La velocidad en cada etapa, calculada con la masa final de la pestaña 2. La velocidad terminal se estima con:

*v = √( 2·m·g / (ρ·Cd·A) )*

m = masa que desciende (kg), g = 9,81 m/s², ρ = densidad del aire en el sitio (kg/m³), Cd = coeficiente de arrastre, A = área proyectada (m²).

**Qué pide:** C3, C4 · Scoresheet *Descent Rate Estimates* *(sin diapositiva)*: velocidad en m/s con paracaídas y con el segundo sistema.

| Etapa | Masa (kg) | Cd | Área (m²) | Velocidad (m/s) | Objetivo (m/s) |
| --- | --- | --- | --- | --- | --- |
| Paracaídas |   |   |   |   | 15 ± 3 |
| Segundo sistema |   |   |   |   | 5 ± 3 |

**Pendientes:** densidad del aire a la altura del sitio de lanzamiento.
