# 5. Sensores

> Pestaña 5 de la *PDR CanSat Universitario – Guía de desarrollo* (Google Docs), migrada al repo el 10/11/2026. Desde la migración se edita acá; ver la sección "La Guía de Drive y el repo" del README.

Qué mide el CanSat y con qué. Para cada sensor el jurado pide al menos dos opciones con especificaciones y una selección justificada: son 2 diapositivas por sensor.

Columnas sugeridas para todas las tablas: rango, precisión, interfaz (I2C, SPI, UART, analógica), consumo, masa y precio.

## 5.1 Visión general

Lista breve de todos los sensores elegidos y para qué se usa cada uno.

**Qué pide:** Scoresheet ítem 15 *Sensor Subsystem Overview*.

**Decisión:**

| sensor elegido | Que mide | Requisitos |
| --- | --- | --- |
| BMP280 | Presión (de la que se calcula la altitud) y temperatura interna | SN1, SN2, C4, G1 |
| INA219 | Tensión y corriente de la batería | SN3, SN8, X6 |
| GPS NEO-M8N | Latitud, longitud, altitud y satélites rastreados | SN4, X5 |
| IMU MPU-6050 | Aceleración y rotación en tres ejes | SN4, X5 |
|   |   |   |
|   |   |   |
|   |   |   |

## 5.2 Presión y altitud

Sensor barométrico para calcular la altitud. Es el que dispara el evento del 80 % de la altura máxima.

**Qué pide:** SN1, C4, G1 · Scoresheet ítems 16 y 17.

**Qué hay que entender:** —

| Sensor | Rango | Precisión | Interfaz | Consumo | Masa (g) | Precio |
| --- | --- | --- | --- | --- | --- | --- |
| A- BMP280 | 300 a 1100 hPa | ±1 hPa absoluta (≈ ±8 m); ±0,12 hPa relativa (≈ ±1 m) | I2C / SPI | ≈ 4 µA a 1 Hz | ≈ 1,5 | $7.199 |
| B |   |   |   |   |   |   |

**Decisión:** BMP280. Su rango cubre las presiones de un vuelo a más de 500 m sobre el terreno, la resolución sobra para detectar el 80 % de la altura máxima, y es el mismo desempeño de presión que el BME280 sin pagar por la humedad, que no se necesita

**Pendientes:**

  - Definir el filtro y el criterio de detección del apogeo para disparar el evento del 80 %.
  - Dejar un orificio pequeño de venteo en la carcasa para que el sensor mida la presión exterior.
  - Confirmar la dirección I2C (0x76 o 0x77) para evitar conflictos con los otros módulos.

## 5.3 Temperatura interna

**Qué pide:** SN2 · Scoresheet ítems 18 y 19.

| Sensor | Rango | Precisión | Interfaz | Consumo | Masa (g) | Precio |
| --- | --- | --- | --- | --- | --- | --- |
| A- BMP280 | −40 a +85 °C | ±1 °C | I2C | ≈ 4 µA a 1 Hz | ≈ 1,5 | $7.199 |
| B- DS18B20 | −55 a +125 °C | ±0,5 °C (de −10 a +85 °C) | 1-Wire | ≈ 1 mA al medir | ≈ 2 | $4.000 (estimado) |

**Decisión:** BMP280. Ya está en la placa por la presión, no suma componentes, masa ni consumo, y los ±1 °C alcanzan para informar la temperatura interna. El DS18B20 es más preciso, pero agrega una pieza y una entrada más.

**Pendientes:**

  - Ubicar el BMP280 lejos del ESP32, del regulador y de los servos, para que el calor de esos componentes no distorsione la medición.
  - Si el jurado pide más precisión, reevaluar el DS18B20.

## 5.4 Voltaje y corriente de la batería

Se pueden medir con un divisor resistivo más una resistencia shunt o con un integrado que mida ambos.

**Qué pide:** SN3, SN8, X6 · Scoresheet ítems 20 y 21.

| Diseño | Rango | Precisión | Interfaz | Consumo | Masa (g) | Precio |
| --- | --- | --- | --- | --- | --- | --- |
| A-INA219 con shunt de 0,1 Ω | Tensión de 0 a 26 V; corriente ±3,2 A | Resolución de 4 mV y ≈ 0,1 mA; error máximo ≈ 0,5 % | I2C (dirección 0x40) | ≈ 1 mA | ≈ 2 |   |
| B-Divisor resistivo + ACS712 de 5 A | Tensión según el divisor; corriente ±5 A | Ruido de ≈ 100 mA, malo para corrientes chicas | Analógica (ADC del ESP32) | ≈ 10 mA | ≈ 4 | ≈ $5.000 |

**Decisión:** INA219. Mide tensión y corriente con un solo módulo digital, con mejor resolución que el ACS712 en los valores bajos que tiene este sistema. El ADC del ESP32 no es lineal, así que medir con un divisor sumaría error. Las medidas se envían por telecomando (X6).

**Pendientes:**

  - Cotizar el INA219, que figura en el presupuesto sin precio.
  - Coordinar con la persona 4 (energía) dónde va el shunt, de modo que mida la corriente total de la batería, incluyendo los picos de los servos.
  - Confirmar que la tensión de la batería queda dentro del rango del integrado.

## 5.5 GPS

Tiene que dar latitud, longitud, altitud y cantidad de satélites.

**Qué pide:** SN4, X5 · Scoresheet ítems 22 y 23.

| Sensor | Precisión | Actualización | Interfaz | Consumo | Masa (g) | Precio |
| --- | --- | --- | --- | --- | --- | --- |
| A. NEO-M8N (módulo GY-GPSV3) | 2,5 m CEP | Hasta 10 Hz (usamos 1 Hz); arranque en frío ≈ 26 s | UART (también I2C) | ≈ 25 a 30 mA | ≈ 12 con antena | $21.824,21 |
| B. NEO-6M | 2,5 m CEP | Hasta 5 Hz; arranque en frío ≈ 27 s | UART | ≈ 45 mA | ≈ 12 con antena | $9.000 estimado |

**Decisión:** NEO-M8N. Rastrea varias constelaciones a la vez, lo que da más satélites y un enganche más rápido y estable, consume menos que el NEO-6M y entrega los cuatro datos pedidos por UART. La diferencia de precio es el costo de esa robustez.

**Pendientes:**

  - Ubicar la antena con vista al cielo, sin que la tape el panel solar ni piezas metálicas.
  - Calcular cuánto antes del lanzamiento hay que encender el GPS para que ya esté enganchado (la espera por E7 es de dos horas, así que hay margen).
  - Configurar el módulo a 1 Hz y verificar que la altitud y el número de satélites salgan en el paquete de telemetría.

## 5.6 Aceleración y rotación

Acelerómetro y giróscopo en los tres ejes. Pueden ser un solo integrado (IMU), pero el scoresheet los puntúa por separado.

**Qué pide:** SN5, X5 · Scoresheet ítems 24 a 27.

| Sensor | Rango acel. (g) | Rango giro (°/s) | Interfaz | Consumo | Masa (g) | Precio |
| --- | --- | --- | --- | --- | --- | --- |
| A. MPU-6050 | ±2, ±4, ±8 o ±16 | ±250 a ±2000 | I2C  | ≈ 3,8 mA  | ≈ 2,5 | $6.682 |
| B. MPU-9250 + ADXL375 | ±16 (MPU) y ±200 (ADXL375) | ±250 a ±2000 | I2C / SPI | ≈ 3,6 mA + 0,15 mA | ≈ 4 | ≈ $39.000 (est.) |

**Decisión:** MPU-6050, que es el que está en el presupuesto. Reúne acelerómetro y giróscopo en un chip económico, con muchas librerías y 16 bits de resolución.

**Pendientes:**

  - Rango de aceleración. El MPU-6050 llega a ±16 g y el impacto de diseño es de 30 G (S5). Para telemetría del descenso alcanza, pero se satura en el golpe. Hay que decidir si se agrega un ADXL375 (±200 g, unos $30.000) para medir el impacto.
  - Dirección I2C. El MPU-6050 y el DS3231 comparten la dirección 0x68. Se resuelve poniendo el pin AD0 del MPU en alto (0x69).
  - Definir la calibración (reposo en la plataforma) y la frecuencia de muestreo, y convertir a unidades SI en el paquete (G6).

## 5.7 Cámara de despliegue (cenit)

Apunta hacia arriba y graba la apertura de los sistemas de descenso.

**Qué pide:** C6, SN6, SN7 · Scoresheet ítems 28 y 29.

| Cámara | Resolución | Cuadros/s | Almacenamiento | Consumo | Masa (g) | Precio |
| --- | --- | --- | --- | --- | --- | --- |
| A |   |   |   |   |   |   |
| B |   |   |   |   |   |   |

**Decisión:** —

**Pendientes:** —

## 5.8 Cámara a tierra (nadir)

Apunta hacia abajo durante todo el descenso.

**Qué pide:** C7, SN7 · Scoresheet ítems 30 y 31.

| Cámara | Resolución | Cuadros/s | Almacenamiento | Consumo | Masa (g) | Precio |
| --- | --- | --- | --- | --- | --- | --- |
| A |   |   |   |   |   |   |
| B |   |   |   |   |   |   |

**Decisión:** —

**Pendientes:** —

## 5.9 Panel solar

Uno o más paneles que emiten una señal cuando reciben radiación; el valor se pide por telecomando.

**Qué pide:** E3, X6 · el scoresheet no lo puntúa, pero es un requisito del Anexo A.

**Opciones:** —

**Decisión:** —

**Pendientes:** dónde se presenta en las diapositivas (pestaña 13).

## 5.10 Detección de separación

Cómo detecta el CanSat que se separó del cohete para enviar el aviso de comienzo de misión.

**Qué pide:** X3 · Scoresheet *Instrument Release Sensor* *(sin diapositiva)*: dos sensores y selección.

| Sensor | Principio | Confiabilidad | A favor | En contra |
| --- | --- | --- | --- | --- |
| A. Sensor de luz (fotorresistor o el panel solar) | Dentro del cohete hay oscuridad; al salir, la luz sube de golpe | Media a alta | Sin partes móviles, sin piezas salientes, reutiliza el panel solar | Depende de la luz ambiente y de que el interior del cohete sea oscuro |
| B. Microinterruptor de contacto | Una palanca apoyada contra la pared del cohete se suelta al salir | Media  | Respuesta directa, no depende de la luz | La palanca saliente puede trabar el deslizamiento (S7) y falsear con las vibraciones (S4) |

**Decisión:** sensor de luz como disparador principal, con confirmación por el IMU, que registra el pico de aceleración de la expulsión del motor (C2). Así se evita agregar una pieza móvil que pueda trabar la salida del CanSat.

**Pendientes:**

  - Confirmar con la CONAE cómo va montado el CanSat dentro del fuselaje y si el interior queda a oscuras.
  - Definir el umbral de luz y el tiempo de confirmación para evitar falsos disparos, por ejemplo al manipular el CanSat con linterna durante las pruebas.
