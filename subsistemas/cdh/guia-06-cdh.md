# 6. Procesamiento y comunicaciones

> Pestaña 6 de la *PDR CanSat Universitario – Guía de desarrollo* (Google Docs), migrada al repo el 10/11/2026. Desde la migración se edita acá; ver la sección "La Guía de Drive y el repo" del README.

El cerebro del CanSat: qué procesador lee los sensores, dónde se guardan los datos y cómo se transmiten a la estación terrena.

## 6.1 Visión general

Resumen de los componentes elegidos y cómo se conectan.

**Qué pide:** Scoresheet ítem 47 *CDH Overview*.

**Decisión:** —

## 6.2 Procesador

Dos configuraciones de procesador, con velocidad y tiempo de arranque (importa para recuperarse de un reinicio en vuelo).

**Qué pide:** Scoresheet ítems 48, 51 y 52.

**Qué hay que entender:** —

| Procesador | Velocidad (MHz) | Arranque | RAM / Flash | Pines | Consumo | Precio |
| --- | --- | --- | --- | --- | --- | --- |
| A |   |   |   |   |   |   |
| B |   |   |   |   |   |   |

**Decisión:** —

**Pendientes:** —

## 6.3 Memoria y almacenamiento

Dónde se guardan telemetría y estados, cuánto espacio hace falta y cómo se guarda lo que debe sobrevivir a un reinicio.

**Qué pide:** F1, F2, F5 · Scoresheet ítem 49 *Memory selections*.

| Opción | Capacidad | Persistencia | Interfaz | A favor | En contra |
| --- | --- | --- | --- | --- | --- |
| A |   |   |   |   |   |
| B |   |   |   |   |   |

**Decisión:** —

**Pendientes:** —

## 6.4 Interfaces de datos

Qué tipo de pin usa cada componente (GPIO, analógico, I2C, SPI, UART), si es entrada o salida, y cuántos quedan libres.

**Qué pide:** Scoresheet ítem 50 *Data Interfaces*.

| Componente | Interfaz | Entrada / salida | Pines usados |
| --- | --- | --- | --- |
|   |   |   |   |

**Pendientes:** —

## 6.5 Reloj de tiempo real (RTC)

Mantiene la hora y el tiempo de misión aunque el procesador se reinicie o se corte la energía un instante.

**Qué pide:** F2, F3 · Scoresheet *Payload Real-Time Clock* *(sin diapositiva)*: dos opciones y selección.

| RTC | Precisión | Respaldo de energía | Interfaz | A favor | En contra |
| --- | --- | --- | --- | --- | --- |
| A |   |   |   |   |   |
| B |   |   |   |   |   |

**Decisión:** —

**Pendientes:** —

## 6.6 Antena de la carga útil

**Qué pide:** Scoresheet *Payload Antenna* *(sin diapositiva)*: dos opciones con alcance y patrón de radiación.

| Antena | Tipo | Ganancia | Alcance | Patrón | A favor | En contra |
| --- | --- | --- | --- | --- | --- | --- |
| A |   |   |   |   |   |   |
| B |   |   |   |   |   |   |

**Decisión:** —

**Pendientes:** —

## 6.7 Radio

El módulo de radio, dentro de las bandas autorizadas por ENACOM y sin modo broadcast.

**Qué pide:** X1, X2 · Scoresheet ítem 53 *Radio Selection*.

| Radio | Banda | Potencia | Alcance | Consumo | Precio |
| --- | --- | --- | --- | --- | --- |
| A |   |   |   |   |   |
| B |   |   |   |   |   |

**Decisión:** —

**Pendientes:** —

## 6.8 Control de transmisión

Cada cuánto se transmite, qué dispara el inicio de la misión y qué pasa al aterrizar.

**Qué pide:** C5, X3, X4 · Scoresheet ítem 54 *Discussion of Transmission Control*.

**Decisión:** —

**Pendientes:** —

## 6.9 Formato de telemetría

El paquete que se envía cada segundo, campo por campo, con un ejemplo real.

**Qué pide:** X5, G3, F1 · Scoresheet ítem 55 *Payload Telemetry Format*.

| Campo | Unidad | Formato | Ejemplo |
| --- | --- | --- | --- |
| Tiempo de misión | s |   |   |
| Contador de paquetes | — |   |   |
| Altitud | m |   |   |
| Presión | Pa |   |   |
| Temperatura | °C |   |   |
| Aceleración X, Y, Z | m/s² |   |   |
| Rotación X, Y, Z | °/s |   |   |
| GPS: latitud, longitud, altitud, satélites | °, m, — |   |   |
| Estado del software | — |   |   |

**Pendientes:** el scoresheet pide seguir la sección 3.3 de un *Mission Guide* que no tenemos (pestaña 13).

## 6.10 Comandos

Lista de telecomandos y su formato.

**Qué pide:** G1, X6, F3, F4 · Scoresheet ítem 56 *Payload Command Formats*.

| Comando | Formato | Qué hace |
| --- | --- | --- |
| Calibrar altitud a cero |   |   |
| Fijar hora UTC |   |   |
| Pedir estado de batería y panel solar |   |   |

**Pendientes:** —
