# 1. Misión y requisitos (versión de Kiara)

> Pestaña 1 de la *PDR CanSat Universitario – Guía de desarrollo* (Google Docs), migrada al repo el 10/11/2026. Desde la migración se edita acá; ver la sección "La Guía de Drive y el repo" del README.

El plazo: los documentos de la PDR se entregan del 17 al 21 de noviembre. Hoy es 9, así que quedan entre 8 y 12 días. Si se entrega tarde o en otro formato que no sea PDF, el equipo queda eliminado.

## 1. Cómo se va a trabajar (método)

El equipo trabaja como en una misión espacial real, siguiendo este camino:

Requisito → asignación a un subsistema → requisito derivado (con número) → diseño → verificación

| Concepto | Qué significa | Ejemplo |
| --- | --- | --- |
| Requisito | Una frase con “debe” que se puede comprobar | S1: masa de 500 ± 10 g |
| Asignación | Quién responde por cada requisito | C4 → descenso + software + mecánica |
| Requisito derivado | Meta con número que sale de un requisito | “El barómetro debe muestrear a 10 Hz o más” |
| Trazabilidad | Poder seguir cada decisión hasta su requisito | “Elegimos FRAM porque F1, F2 y F5 piden sobrevivir a reinicios” |
| Verificación | Demostrar que se cumple | Pesar el CanSat para S1  |
| TBD / TBR | Dato a definir / dato propuesto sin confirmar | Apogeo de 600 m (TBR) |

*Cada requisito se verifica con uno o más de cuatro métodos:*

  - A (análisis): cálculo o simulación.
  - I (inspección): medir o revisar, sin hacerlo funcionar.
  - D (demostración): hacerlo funcionar y ver que anda.
  - E (ensayo): hacerlo funcionar en condiciones controladas y medir.

## Reglas del informe:

  - Citar el código del requisito en cada diapositiva, por ejemplo “(C4, SN1)”.
  - Usar siempre unidades del SI.
  - Todo número lleva su fuente: calculado, hoja de datos o medido.
  - Lo que falta se marca TBD o TBR. No se deja en blanco.

## 2. Cómo se puntúa

  - La plantilla tiene 89 diapositivas. Cada una lleva un número de ítem del scoresheet y un recuadro Expectations con lo que busca el jurado.
  - El scoresheet tiene 127 ítems. 126 valen 2 puntos y la calidad de la presentación vale 10, en total 262 puntos.
  - Una diapositiva linda que no responde el recuadro no suma. Hay que contestarlo punto por punto, con el mismo orden y las mismas palabras.
  - Puntos fáciles: índice con número de página (ítem 1) y lista de siglas (ítem 3).
  - Faltan diapositivas en la plantilla, y hay que agregarlas: la tabla de cumplimiento de requisitos (vale 2 ítems) y la secuencia de eventos del día de lanzamiento.

## 3. La misión (diapositiva 7)

Hay que bajar en dos etapas con un cambio automático de sistema de descenso, probarlo con telemetría y video, y recuperar el CanSat entero.

| Objetivo | Qué es |
| --- | --- |
| OP1 | Salir del cohete y bajar a 15 ± 3 m/s con paracaídas automático |
|   | Detectar el 80 % del apogeo en la bajada, liberar el segundo sistema y promediar 5 ± 3 m/s |
|   | Transmitir telemetría completa a 1 Hz |
|   | Filmar todo el descenso hacia cenit y hacia nadir |
|   | Estación terrena propia que recibe, muestra, grafica, guarda y envía comandos |
| OP6 | Sobrevivir al vuelo y ser recuperado |

Criterios de éxito propuestos (sirven para la PFR):

  - Mínimo: sale del cohete, baja con paracaídas, llega entero y la estación recibe telemetría.
  - Completo: se cumplen OP1 a OP6.
  - Extendido: lo anterior más los objetivos secundarios.

DECIDIR: ¿sumamos los objetivos secundarios?

  - OS1: calcular la velocidad de descenso en tiempo real.
  - OS2: reconstruir la trayectoria y sincronizar el video con la telemetría.

## 4. Requisitos de alto nivel (diapositiva 8)

De los 65 requisitos, unos 20 dicen qué pasa en el vuelo y cuándo. El resto dice cómo construirlo. Por eso en la diapositiva 8 se ordenan por fase del vuelo y no por código. Copiar los 65 es un error común.

Los grupos son:

| Grupo | Cant. | Lo esencial |
| --- | --- | --- |
| Operativos (C) | 9 | Ubicación, despliegue, dos etapas, 1 Hz, dos videos, baliza, costo |
| Estructurales (S) | 9 | Masa, diámetro, largo, 15 G y 30 G, pared de 2 mm |
| Mecanismos (M) | 4 | Sin pirotecnia ni químicos, sin resortes en baterías |
| Eléctricos (E) | 9 | Baterías permitidas, panel solar, interruptores, 2 h de autonomía |
| Comunicaciones (X) | 6 | Bandas autorizadas, sin broadcast, aviso de separación |
| Sensores (SN) | 8 | Altitud por presión, temperatura, GPS, video 640×480 |
| Estación terrena (G) | 15 | Una sola pantalla legible al sol, gráficos, comandos, portátil |
| Software de vuelo (F) | 5 | Contador, tiempo y estados que sobreviven reinicios |
|   |   |   |

## 5. Quién responde por qué (asignación)

| Subsistema | Persona | Responde por |
| --- | --- | --- |
| Control de descenso | P1 | C3, C4 |
| Mecánica | P2 | S1–S9, M1–M4, C1, C2, E5 |
| Sensores y cámaras | P3 | SN1–SN8, C6, C7 |
| Comunicaciones y datos (C&DH) | P3 con P5 | C5, X1, X2, X4–X6 |
| Potencia | P4 | E1–E4, E6–E9, C8 |
| Software de vuelo | P5 | F1–F5, X3 |
| Estación terrena | P6 | G1–G15 |
| Gestión | A definir | C9 (costo/presupuesto) |

DECIDIR: ¿quién es el responsable de gestión? Es el único rol sin dueño, y es el que controla el costo (C9).

Los números que se proponen:

  - Masa (500 g): estructura 230 g, descenso 60 g, electrónica y sensores 120 g, potencia 70 g, margen 20 g.
  - Tamaño: diámetro entre 89,5 y 90 mm, largo total 230 mm (TBR). Los dos sistemas de descenso plegados deben ocupar 60 mm o menos.
  - Paracaídas 1 (15 m/s): área de unos 0,05 m². Si es circular plano, mide unos 25 cm de diámetro.
  - Paracaídas 2 (4,5 m/s): área de unos 0,55 m². Si es circular plano, mide unos 84 cm de diámetro.
  - Resistencia: las líneas y el anclaje del segundo sistema deben aguantar un tirón de 100 N o más.
  - Barómetro: 10 Hz o más en vuelo y resolución de 1 m o mejor.
  - Detección del 80 %: el software activa el segundo sistema tras 3 lecturas seguidas por debajo de 0,8 × apogeo.
  - Mecanismo: libera en 1 s o menos y se mantiene trabado con 30 G.
  - Acelerómetro: el MPU-6050 llega a ±16 g y el choque es de 30 G, así que hace falta otro de mayor rango (±32 g o más).
  - Telemetría: paquete de unos 118 bytes con 20 campos, que incluye contador, identificador de equipo y CRC.
  - Radio: banda de 915–928 MHz, con margen de enlace de 15 dB o más (alcance de unos 850 m con apogeo de 600 m y unos 1,8 km con 1.000 m).
  - Batería: capacidad de 1,5 × consumo medio × 2,5 h o más.
  - Memoria: FRAM con CRC, más un watchdog para sobrevivir a reinicios.
  - Reloj: DS3231 con batería propia.
  - Cámaras: empiezan a grabar al detectar el despegue y siguen hasta el aterrizaje.

## 6. El vuelo en 8 fases (diapositiva 16)

| Fase | Altura / velocidad | Qué pasa |
| --- | --- | --- |
| 1. Rampa | 0 m, hasta 2 h | Se enciende, se ve el LED y suena la baliza. La estación fija la hora y calibra la altitud a cero. |
| 2. Ascenso | 0 → ≈600 m | Detecta el despegue por aceleración y arrancan el video y la telemetría completa. |
| 3. Eyección | ≈600 m | La carga de eyección lo expulsa. El panel solar pasa de oscuridad a luz, se avisa la separación y se abre el paracaídas 1. |
| 4. Etapa 1 | 600 → 480 m a 15 m/s (≈8 s) | Guarda la altitud máxima en la FRAM. |
| 5. Cambio | 480 m (80 %) | Con 3 lecturas seguidas activa el mecanismo y se despliega el segundo sistema, que filman las cámaras. |
| 6. Etapa 2 | 480 → 0 m a 4,5 m/s (≈107 s) | Sigue midiendo y transmitiendo. |
| 7. Aterrizaje | 0 m | Detiene el video, sigue enviando el GPS y suena la baliza. |
| 8. Recuperación | — | Se localiza con GPS y baliza y se comparan los CSV principal y de respaldo. |

La fase 5 es la crítica, porque el CanSat decide solo cuándo cambiar de sistema. Si el procesador se reinicia en vuelo, retoma el estado guardado en memoria (F5).

Por qué 4,5 m/s y no 5: hay dos lecturas posibles de “5 m/s de promedio durante todo el descenso”. Con 4,5 m/s en la etapa 2, el promedio da 4,5 m/s si se mide desde el 80 % y unos 5,2 m/s si se mide desde el apogeo. Las dos lecturas quedan dentro de 5 ± 3 m/s.

## 7. Matriz de verificación

Es una tabla con los 65 requisitos, con responsable, método y diapositiva. Va al final del informe como la diapositiva de cumplimiento, y vale dos veces: una por la tabla y otra por estar completa. Cuando las diapositivas estén armadas hay que reemplazar los números de ítem por los números de diapositiva reales. Ejemplos de cómo se verifican algunos:

S1 (masa): presupuesto de masa y balanza.

S4 y S5 (15 G y 30 G): ensayo de vibración y ensayo de caída con cordón.

C3 y C4 (descenso): cálculo de área, ensayo de vacío y caída desde altura (dron).

E7 (2 h): presupuesto de energía y ensayo con el CanSat cerrado, de 3 h o más.

G12 (legible al sol): prueba al sol con la notebook real.

## 8. Ambigüedades: lo que hay que consultar

La regla propuesta es elegir la lectura que cumpla todas las interpretaciones a la vez y consultar el resto. Mostrar la lectura elegida en la PDR demuestra que entendemos los requisitos. Las más importantes:

| Tema | Duda | Cómo lo leemos mientras tanto |
| --- | --- | --- |
| “80 %” de C4 | ¿En subida o bajada? | En la bajada, a 0,8 × apogeo. |
| “5 m/s promedio” | ¿Desde el apogeo o desde el 80 %? | Etapa 2 a 4,5 m/s, que cumple ambas. |
| Contenedor y carga útil | El Anexo habla de ambos y no dice si se separan. | Un solo cuerpo con descenso en dos etapas. |
| Medidas | Anexo: Ø 90 mm. Bases: 95 × 200 mm. | 90 mm de diámetro y 230 mm de largo. |
| “Enviar un comando” (X3) | El CanSat no recibe la orden, la envía. | Informar la separación como evento en la telemetría. |
| Cuándo transmitir | Las Bases dicen “separación”, pero G5 pide ver el ascenso. | Transmitir desde el despegue. |
| Tiempo de misión | ¿UTC o transcurrido? | Enviar ambos. |
| Rotaciones | G6 pide SI (rad/s), pero °/s es habitual. | rad/s hasta que la CONAE acepte °/s. |
| Broadcast (X2) | ¿Un enlace LoRa con identificador de equipo cumple? | Identificador de equipo en el paquete. |
| Telemetría en las 2 h de espera | ¿Qué transmitir en STAND-BY? | Bajo consumo y telemetría reducida. |
| Panel solar | ¿Alimenta algo o solo emite una señal? | Solo se mide su tensión. |

## 9. Diferencias entre las investigaciones del equipo

Coinciden en lo principal: ESP32, máquina de estados, FRAM con CRC y watchdog, reloj DS3231, celdas 18650, INA219, GPS NEO-M8N, servo con pasador y simulaciones previas. Estas son las 13 diferencias:

| N.º | Tema | Conflicto | Propuesta | Decide |
| --- | --- | --- | --- | --- |
| 1 | Banda de radio | El presupuesto lista un XBee de 2,4 GHz y P6 propone 915 MHz. | 915 MHz, que pierde 8,5 dB menos. | P3 y P6 |
| 2 | Formato de telemetría | P5 tiene 15 campos y P6 tiene 20. | El de P6, que P5 revisa y firma. | P5 y P6 |
| 3 | Comandos | Los nombres son distintos. | Una lista con el formato de P6, a la que P5 suma STATUS. | P5 y P6 |
| 4 | Cámaras | No están en el presupuesto y P3 propone dos ESP32-CAM. | Sumarlas a masa y energía, y definir la señal de arranque. | P3, P4 y P5 |
| 5 | Batería | P3 menciona una LiPo. | Corregir, porque está prohibida (E1). | P3 y P4 |
| 6 | Servos | El presupuesto trae dos servos y C3 dice que la etapa 1 es pasiva. | Etapa 1 pasiva, un servo para la etapa 2 y el otro de repuesto. | P1 y P2 |
| 7 | Barómetro | BMP280 o BMP388. | Compararlos en el trade y elegir con RD-08. | P3 |
| 8 | Temperatura | Sensor del barómetro o DS18B20 aparte. | Trade con las dos opciones. | P3 |
| 9 | Acelerómetro | MPU-6050 llega a ±16 g. | Sumar uno de mayor rango. | P3 |
| 10 | Apogeo supuesto | 600 m contra 1.000 m. | Los dos: 600 m nominal y 1.000 m como peor caso. | P1 y P6 |
| 11 | Velocidad de etapa 2 | 5 m/s contra 4,5 m/s. | 4,5 m/s. | P1 |
| 12 | Segundo sistema | P1 compara paracaídas, parapente y rotor, pero el scoresheet espera un parapente. | Paracaídas como base y parapente documentado. | P1 |
| 13 | Detección del apogeo | Máximo de altitud (Sección 1) contra cambio de signo de la velocidad (P5). | La de P5, que es más robusta frente al ruido. | P5 |

Las cuatro primeras son las urgentesss

## 10. Riesgos que ya se ven

Masa: dos celdas 18650 pesan ≈ 94 g (≈ 47 g cada una) y el presupuesto asigna 70 g a potencia. Si se suman dos cámaras ESP32-CAM, el reparto de masa tiene que rehacerse.

Volumen: el paracaídas de 84 cm de diámetro tiene que plegarse en 60 mm de largo junto con el otro. Es justo.

Falta información: el presupuesto de energía en Wh de P4 y el presupuesto en pesos contra C9 todavía no están. La planilla del presupuesto provisorio tampoco se revisó contra masa y costo.

## 11. Checklist de decisiones para la reunión

Cerrar si o si ahora

  - Banda de radio (915 MHz o 2,4 GHz).
  - Formato de telemetría y lista de comandos.
  - Cámaras: modelo y señal de arranque.
  - Rehacer el reparto de masa con los componentes reales.

Cerrar esta semana:

  -  Apogeo de diseño (600 m nominal y 1.000 m peor caso).
  -  Barómetro, sensor de temperatura y acelerómetro adicional.
  -  Servos y etapa 1 pasiva.
  -  Responsable de gestión y presupuesto en pesos.
  -  Presupuesto de energía (P4).
  -  Objetivos secundarios OS1 y OS2.
  -  Quién arma las diapositivas 7, 8, 16 y la de cumplimiento.
