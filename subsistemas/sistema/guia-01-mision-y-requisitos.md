# 1. Misión y requisitos

> Pestaña 1 de la *PDR CanSat Universitario – Guía de desarrollo* (Google Docs), migrada al repo el 10/11/2026. Desde la migración se edita acá; ver la sección "La Guía de Drive y el repo" del README.

*Documento de trabajo del equipo · actualizado el 6 de noviembre de 2026*

## Alcance

Esta sección define **qué tiene que lograr el CanSat y cómo se organizan sus 65 requisitos**, antes de diseñar nada. Es la base de todo el informe: cada decisión de las otras secciones tiene que poder rastrearse hasta un requisito de acá. Es un **documento de trabajo**: lo que dice "propuesta" está abierto a discusión.

Cubre lo que las Bases (§6) piden demostrar en primer lugar: comprensión de los requisitos de la misión, asignación y derivación de los requisitos a los subsistemas, y definición del concepto de operaciones.

Esta versión se ajustó con las investigaciones del equipo: descenso (P1), sensores (P3), software de vuelo y telemetría (P5), estación terrena (P6) y el presupuesto provisorio de componentes, además de la Sección 2 de mecánica (P2). Donde esas investigaciones no coinciden entre sí, la diferencia y una propuesta para cerrarla están en 1.7.

| Tema | Qué produce | Diapositivas PDR | Ítems del scoresheet |
| --- | --- | --- | --- |
| Cómo trabajar | Método común para todo el equipo | — | — |
| Cómo debe ser el informe | Qué se entrega y cómo se puntúa | Todas | Calidad (10 puntos) |
| 1.1 Resumen de la misión | Objetivos y texto de la misión | 7 | 4 *Mission Summary* |
| 1.2 Requisitos de alto nivel | Tabla de requisitos por evento de vuelo | 8 | 5 *System Requirement Summary* |
| 1.3 Asignación y derivación | Requisito → subsistema y persona → meta numérica | 8 y cada subsistema | Bases §6 |
| 1.4 CONOPS | Fases del vuelo con alturas, velocidades, eventos y estados del software | 16 | 13 *System Concept of Operations* |
| 1.5 Matriz de verificación | Los 65 requisitos con responsable y método de verificación | Sin diapositiva (agregar) | *Requirements Compliance* (2 ítems) |
| 1.6 Ambigüedades | Lo que hay que consultar y cómo lo resolvemos mientras tanto | — | — |
| 1.7 Coherencia entre las investigaciones | Diferencias entre las investigaciones del equipo y cómo cerrarlas | — | — |

### Resumen: propuestas iniciales

| Tema | Propuesta inicial | Qué puede cambiarla |
| --- | --- | --- |
| Objetivo principal | Bajar en dos etapas (15 y 5 m/s) con cambio automático al 80 % del apogeo, transmitiendo telemetría a 1 Hz y filmando ambos sistemas | Nada: es la misión del Anexo A |
| Apogeo de diseño | 600 m para los tiempos de descenso; 1.000 m como peor caso para el enlace y la memoria de video (el valor que usó P6). Las Bases solo dicen "más de 500 m" | Los datos del cohete |
| Velocidad de la etapa 2 | 4,5 m/s: cumple las dos lecturas del promedio de C4 | Respuesta de la CONAE |
| Duración del descenso | ≈ 115 s con apogeo de 600 m: 8 s a 15 m/s y ≈ 107 s a 4,5 m/s | Apogeo real |
| Presupuesto de masa por subsistema | Estructura 230 g, descenso 60 g, electrónica y sensores 120 g, potencia 70 g, margen 20 g | Componentes reales: dos celdas 18650 ya pesan ≈ 94 g |
| Procesador | ESP32, con FreeRTOS o bucle con máquina de estados | Pruebas de tiempos de ejecución (P5) |
| Radio | Banda de 915–928 MHz, con XBee-PRO 900HP o LoRa SX1276 | Decisión de P3 y P6: el presupuesto lista un XBee S2C de 2,4 GHz |
| Verificación | Cada requisito con un método: análisis, inspección, demostración o ensayo | Pruebas disponibles |
| Requisitos en conflicto | Diseñar según el Anexo A; adaptar las diapositivas del scoresheet que no coinciden | Respuesta de la CONAE |

## Cómo trabajar: de requisito a diseño verificado

Se trabaja como en una misión espacial real: **cada requisito se asigna a un subsistema, se traduce en metas con número, se diseña para cumplirlas y se planea cómo verificarlo**. La PDR es justamente la revisión que comprueba que ese camino está armado. Es el mismo enfoque del manual de ingeniería de sistemas de la NASA, del que las Bases toman la definición de PDR ([NASA SE Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf)).

### Conceptos

| Término | Qué es | Ejemplo nuestro |
| --- | --- | --- |
| Requisito | Una frase con "debe" que dice qué tiene que cumplir el sistema, una sola idea, que se puede comprobar | S1: masa de 500 ± 10 g |
| Requisito de sistema | El que aplica al CanSat entero; los nuestros vienen dados por el Anexo A | C4: segundo sistema al 80 % del apogeo |
| Asignación | Decidir qué subsistema responde por cada requisito | C4 → control de descenso + software de vuelo + mecánica |
| Requisito derivado | Meta concreta de un subsistema que sale de un requisito de sistema | "El barómetro debe muestrear a 10 Hz o más" (de C4 y SN1) |
| Trazabilidad | Poder seguir cada decisión hasta el requisito que la origina, y al revés | "Elegimos FRAM porque F1, F2 y F5 piden guardar datos ante reinicios" |
| Verificación | Demostrar que el diseño cumple el requisito | Pesar el CanSat en balanza para S1 |
| Validación | Demostrar que el sistema cumple la misión, no solo la letra | Un vuelo de prueba completo con datos y video |
| TBD / TBR | Dato a definir / dato propuesto que falta confirmar | Apogeo de 600 m (TBR) |
| Margen | Diferencia entre lo exigido y lo que da el diseño | Batería para 3 h cuando se piden 2 h |

### Cómo se escribe un requisito derivado

Tiene que tener **número y unidad, un origen y una forma de verificarlo**. Si no se puede medir, no sirve para decidir.

| Mal escrito | Bien escrito |
| --- | --- |
| "El CanSat debe ser liviano" | "La estructura impresa debe pesar 230 g o menos (deriva de S1; se verifica pesando)" |
| "La radio debe tener buen alcance" | "El enlace debe funcionar a 1,5 km o más con antena de mesa (deriva de C5 y G11; se verifica con ensayo de alcance)" |
| "El software detecta el 80 %" | "El software debe activar el segundo sistema dentro de 1 s de cruzar el 80 % del apogeo, en descenso (deriva de C4; se verifica por simulación y ensayo de vacío)" |

### Métodos de verificación

Cada requisito se verifica con uno o más de estos cuatro métodos (NASA SE Handbook, §2.4). La matriz de 1.5 asigna uno a cada requisito.

| Método | Qué es | Ejemplo nuestro |
| --- | --- | --- |
| A – Análisis | Cálculo, simulación o modelo | Tamaño del paracaídas para 15 m/s; presupuesto de energía para 2 h |
| I – Inspección | Mirar, medir o revisar documentos, sin hacerlo funcionar | Medir el diámetro con calibre; comprobar que no hay LiPo |
| D – Demostración | Hacerlo funcionar y ver que anda, sin medir desempeño | Enviar el comando de calibración y ver la altitud en cero |
| E – Ensayo | Hacerlo funcionar bajo condiciones controladas y medir | Prueba de caída a 30 G; prueba de batería de 2 h |

### Flujo de trabajo del equipo

1.  Cada responsable toma los requisitos de su subsistema de la tabla de asignación (1.3).
2.  Escribe sus requisitos derivados con número, origen y verificación.
3.  Compara dos o más opciones con criterios que salen de esos números (el *trade* que pide el scoresheet).
4.  Elige, y anota la decisión con el requisito que la justifica en el registro de decisiones (pestaña 12 del Google Doc).
5.  Define cómo se verifica y lo suma al plan de pruebas (pestaña 10).
6.  Actualiza el estado del requisito en la matriz: Pendiente, En análisis, Definido o Verificado.

### Convenciones para todo el informe

  - Citar el código del requisito entre paréntesis en cada diapositiva donde se cumple, por ejemplo "(C4, SN1)". Facilita la tabla de cumplimiento y que el jurado lo encuentre.
  - Unidades del Sistema Internacional siempre (lo exige G6 para la estación terrena; conviene usarlo en todo).
  - Todo número lleva su fuente: calculado, hoja de datos o medido.
  - Lo que no está definido se marca TBD o TBR, no se deja en blanco. La CDR exige resolverlos (Bases §6).

## Cómo debe ser el informe

El informe de la PDR **no es un documento de texto: es la plantilla de diapositivas de la CONAE, completa y exportada a PDF**, subida al Aula Virtual antes de la fecha límite (Bases §3, Etapa 2). Si llega tarde o en otro formato, el equipo queda afuera. Documentos como este son el trabajo previo; después se condensan en las diapositivas.

### Cómo se puntúa

  - La plantilla tiene 89 diapositivas. Cada una lleva el número de un ítem del scoresheet y un recuadro *Expectations* con lo que el jurado va a buscar.
  - El scoresheet tiene 127 ítems: 126 valen 2 puntos y la calidad de la presentación vale 10, en total 262. La nota es el promedio de los jueces dividido por 262.
  - El jurado revisa ítem por ítem si está lo que pide el recuadro. Una diapositiva linda que no responde la expectativa no suma.
  - El scoresheet tiene ítems sin diapositiva en la plantilla. De esta sección: la tabla de cumplimiento de requisitos (*Requirements Compliance*, 2 ítems) y la secuencia de eventos de la misión. Hay que agregar esas diapositivas.
  - Se pasa a la CDR si se está entre los 20 mejores equipos (Bases §3).

### Las diapositivas de esta sección

| Diapositiva | Qué pide el jurado | Qué poner | Error común |
| --- | --- | --- | --- |
| 7 – *Mission Summary* (ítem 4) | Descripción de la misión; se puede copiar de la guía | Objetivo en 2 o 3 líneas, la lista de objetivos de 1.1 y un esquema simple del vuelo | Ponerse a explicar el diseño; acá va qué se pide, no cómo lo hacemos |
| 8 – *System Requirement Summary* (ítem 5) | Requisitos de alto nivel: despliegue, eventos a alturas específicas, modo de descenso | La tabla de 1.2: código, requisito resumido y en qué fase aplica | Copiar los 65 requisitos; acá van solo los de alto nivel |
| 16 – *System Concept of Operations* (ítem 13) | Operación de vuelo desde el lanzamiento hasta el aterrizaje, con todos los pasos | El diagrama de fases de 1.4 con alturas, velocidades y eventos | Dejar fuera la preparación en rampa o la recuperación |
| Nueva – Cumplimiento de requisitos | Tabla con número, descripción y diapositiva donde se cumple cada requisito, completa | La matriz de 1.5, con la columna de diapositivas llena al final | Dejar requisitos sin diapositiva, o poner "Sí" sin decir dónde |

### Reglas prácticas para todas las diapositivas

  - Responder el recuadro *Expectations* punto por punto, con el mismo orden y las mismas palabras.
  - Una idea por diapositiva; tablas y diagramas antes que párrafos.
  - Letra legible en PDF (la calidad vale 10 puntos, el ítem más pesado).
  - Índice con número de página (ítem 1) y lista de siglas (ítem 3): son 4 puntos fáciles.
  - La plantilla está en inglés; falta confirmar si se puede presentar en español (pestaña 13 del Google Doc).

## 1.1 Resumen de la misión

La misión es **bajar en dos etapas con un cambio automático de sistema de descenso, probarlo con telemetría y video, y recuperar el CanSat entero**. Todo lo demás (masa, medidas, baterías, radio) son las condiciones para lograrlo de forma segura.

### Qué dicen las fuentes

  - **Bases §4**: carga útil cilíndrica lanzada por un cohete de la CONAE a más de 500 m sobre el terreno, que debe descender por sus propios medios de forma segura y transmitir los datos que permitan verificar el cumplimiento de los requisitos.
  - **Bases §1**: el certamen busca que el equipo recorra a escala todas las etapas de una misión: diseño, construcción, integración, prueba, lanzamiento y operación.
  - **Anexo A**: define la misión concreta en 65 requisitos (resumen en 1.2).
  - **Scoresheet ítem 4**: "Descripción de la misión. Se puede copiar de la guía".

### Texto propuesto para la diapositiva 7

En español:

*Diseñar, construir y operar un CanSat de 500 g y 90 mm de diámetro que, lanzado por un cohete de la CONAE a más de 500 m, sale del cohete con la carga de eyección y desciende a 15 m/s con un paracaídas. Al pasar por el 80 % de la altitud máxima, libera por sí solo un segundo sistema de descenso que lo baja a 5 m/s hasta el suelo. Durante todo el vuelo mide altitud, presión, temperatura, aceleraciones, rotaciones, posición GPS y estado de la batería, y transmite esa telemetría una vez por segundo a una estación terrena propia que la muestra en tiempo real y la guarda en CSV. Dos cámaras filman el descenso hacia arriba y hacia abajo para evidenciar la activación de los sistemas de descenso, y una baliza sonora independiente facilita su recuperación.*

En inglés, si la plantilla se presenta en ese idioma:

*Design, build and operate a 500 g, 90 mm diameter CanSat that is launched by a CONAE rocket above 500 m, deployed by the motor ejection charge, and descends at 15 m/s under a parachute. When it passes 80% of the maximum altitude, it autonomously releases a second descent system that slows it to 5 m/s until landing. Throughout the flight it measures altitude, air pressure, temperature, acceleration, rotation rates, GPS position and battery status, and transmits this telemetry at 1 Hz to a team-built ground station that displays it in real time and saves it to CSV. Two cameras record the descent toward zenith and nadir to show the activation of the descent systems, and an independent audio beacon aids recovery.*

### Objetivos de la misión

Los objetivos principales salen del Anexo A y son obligatorios. Los secundarios son propuestas propias: suman valor en la PFR, pero solo si no cuestan masa ni riesgo.

| Código | Objetivo | Requisitos |
| --- | --- | --- |
| OP1 | Desplegarse del cohete y bajar a 15 ± 3 m/s con paracaídas automático | C1, C2, C3, S7 |
| OP2 | Detectar el 80 % del apogeo en la bajada y liberar el segundo sistema, con 5 ± 3 m/s promedio | C4, SN1, M1–M3 |
| OP3 | Transmitir telemetría completa a 1 Hz desde la separación hasta el aterrizaje | C5, X1–X6, SN1–SN5, SN8, F1–F5 |
| OP4 | Filmar todo el descenso hacia cenit y hacia nadir, en color y a 640×480 o más | C6, C7, SN6, SN7 |
| OP5 | Recibir, mostrar, graficar y guardar la telemetría en una estación terrena propia, y enviar comandos | G1–G15 |
| OP6 | Sobrevivir al vuelo y ser recuperado | S4, S5, S8, C8, E8, E9 |
| Restricciones | Masa, medidas, costo, seguridad y baterías permitidas | S1–S3, S6, S9, C9, E1–E7 |
| OS1 (propuesta) | Calcular la velocidad de descenso en tiempo real a partir de la altitud y mostrarla en la estación | Refuerza C3 y C4 |
| OS2 (propuesta) | Reconstruir la trayectoria con GPS y presión y sincronizar el video con la telemetría por tiempo de misión | Refuerza la PFR (Bases §6) |

### Criterios de éxito (propuesta)

Sirven para la PFR, que pide comparar lo planeado con lo real y analizar fallas (Bases §6).

| Nivel | Se cumple si… |
| --- | --- |
| Mínimo | El CanSat sale del cohete, baja con paracaídas, llega entero y la estación recibe telemetría |
| Completo | Se cumplen OP1 a OP6: ambas velocidades dentro de ± 3 m/s, cambio al 80 % registrado en video y telemetría, CSV completo y CanSat recuperado |
| Extendido | Completo más OS1 y OS2 |

### Pendientes

  - Confirmar el idioma de la presentación.
  - Decidir si sumamos objetivos secundarios, y cuáles.

## 1.2 Requisitos de alto nivel

De los 65 requisitos, **unos 20 definen qué tiene que pasar en el vuelo y cuándo**; el resto dice cómo construirlo. El scoresheet pide para la diapositiva 8 justamente los primeros: despliegue, eventos a alturas específicas y modo de descenso. Por eso se ordenan por fase del vuelo, no por código.

### Tabla propuesta para la diapositiva 8

| Fase | Altura | Requisito | Qué exige |
| --- | --- | --- | --- |
| Rampa | 0 m | G1, F3 | Calibrar la altitud a cero y fijar la hora UTC (± 1 s) por comando desde la estación |
| Rampa | 0 m | E4, E7 | Encendido en STAND-BY por un interruptor accesible; funcionar 2 h o más dentro del cohete |
| Ascenso | 0 m → apogeo | C1, S4 | Viajar en la parte superior del fuselaje y soportar 15 G de vibración |
| Eyección | Cerca del apogeo, más de 500 m | C2, S5, S7 | Salir del cohete empujado por la carga de eyección, deslizando libre y soportando 30 G de choque |
| Eyección | Cerca del apogeo | X3 | Enviar un aviso automático de separación (comienzo de misión) |
| Etapa 1 | Apogeo → 80 % | C3 | Paracaídas de despliegue automático: 15 ± 3 m/s |
| Cambio | 80 % del apogeo, en bajada | C4 | Liberar el segundo sistema de descenso, sin pirotecnia ni químicos (M1) |
| Etapa 2 | 80 % → suelo | C4 | Bajar a 5 ± 3 m/s promedio |
| Todo el vuelo | — | C5, X4, X5 | Telemetría a 1 Hz con altitud, presión, temperatura, aceleración y rotación en 3 ejes y GPS |
| Todo el descenso | — | C6, C7 | Video continuo hacia cenit y hacia nadir |
| Aterrizaje | 0 m | C8, G2 | Baliza sonora independiente; datos guardados en CSV con respaldo |
| Restricciones | — | S1, S2, S3, C9 | 500 ± 10 g; Ø 90 mm; largo de 200 a 250 mm; costo menor a $1.000.000 |
| Restricciones | — | X1, X2, E1 | Radio en 915–928 MHz o 2400–2483,5 MHz, sin broadcast; sin baterías LiPo |

### Los 65 requisitos por grupo

El detalle de cada uno, con responsable y método de verificación, está en 1.5.

| Grupo | Códigos | Cantidad | Lo esencial |
| --- | --- | --- | --- |
| Operativos | C1–C9 | 9 | Ubicación en el cohete, despliegue, dos etapas de descenso, telemetría a 1 Hz, dos videos, baliza, costo |
| Estructurales | S1–S9 | 9 | Masa, diámetro, largo, 15 G y 30 G, pared de 2 mm, salida libre, fijación, materiales no contaminantes |
| Mecanismos | M1–M4 | 4 | Sin pirotecnia ni químicos, calor encerrado, estados que se mantienen, sin resortes en baterías |
| Eléctricos | E1–E9 | 9 | Baterías permitidas, panel solar, interruptores y orificios, indicador de encendido, 2 h de autonomía, baliza propia |
| Comunicaciones | X1–X6 | 6 | Bandas autorizadas, sin broadcast, aviso de separación, 1 Hz, contenido de la telemetría, estado de batería y panel por comando |
| Sensores | SN1–SN8 | 8 | Altitud por presión, temperatura, voltaje y corriente, GPS, aceleración y rotación, video color 640×480 |
| Estación terrena | G1–G15 | 15 | Calibración, CSV, tiempo de misión, desarrollo propio, pantalla única legible al sol, gráficos, conteo de paquetes, comandos, portable |
| Software de vuelo | F1–F5 | 5 | Contador de paquetes, tiempo de misión y estados que sobreviven reinicios, hora UTC, comandos documentados |

El scoresheet habla de 55 requisitos y el Anexo A trae 65; la tabla de cumplimiento se arma con los 65 (ver 1.6).

## 1.3 Asignación y requisitos derivados

Cada requisito tiene **un subsistema responsable**, aunque otros colaboren. Los requisitos del Anexo dicen qué lograr; los derivados lo convierten en números que cada área puede diseñar y probar. Es lo que las Bases (§6) llaman "asignación y derivación de los requisitos del sistema y de los subsistemas".

### Asignación a subsistemas

Los subsistemas son los de la plantilla PDR.

| Subsistema | Persona | Responde por | Colabora en | Ítems del scoresheet |
| --- | --- | --- | --- | --- |
| Control de descenso | P1 | C3, C4 | S1 (masa), S3 (volumen plegado), S5 (tirón de apertura) | 32–36 |
| Mecánica | P2 | S1–S9, M1–M4, C1, C2, E5 | C4 (mecanismo), C6, C7 (montaje de cámaras), E3, E4, E9 (accesos), ubicación de la antena | 9–14, 37–46 |
| Sensores y cámaras | P3 | SN1–SN8, C6, C7 | X5 (datos), E3 (lectura del panel), integración de la radio | 15–31 |
| C&DH (procesador, memoria, radio) | P3 con P5 | C5, X1, X2, X4, X5, X6 | F1–F3 (memoria y reloj), X3 | 47–56 |
| Potencia (EPS) | P4 | E1–E4, E6–E9, C8 | SN3, SN8 (medición de batería), E5 | 57–65 |
| Software de vuelo (FSW) | P5 | F1–F5, X3 | C4 (detección del 80 %), C5, G1, G15 (comandos), formato del paquete | 66–68 |
| Estación terrena (GCS) | P6 | G1–G15 | X1, X2 (enlace y antenas), X6, F3, F4 (comandos) | 69–74 |
| Gestión | A definir | C9 | Todos (costo de cada componente) | 80–85 |

### Requisitos derivados (propuesta)

Números iniciales para discutir y ajustar en cada sección, tomados de las investigaciones del equipo cuando las hay. Supuestos comunes: masa 0,5 kg; densidad del aire 1,1 kg/m³ (TBR, según la altura del sitio con el modelo ISA); apogeo de 600 m nominal y 1.000 m como peor caso (TBR).

| ID | Requisito derivado | Origen | Persona | Verificación |
| --- | --- | --- | --- | --- |
| RD-01 | Presupuesto de masa: estructura y mecanismo 230 g o menos; descenso 60 g; electrónica, sensores y cámaras 120 g; potencia 70 g; margen y lastre 20 g | S1 | Todos | A, luego I (balanza) |
| RD-02 | Diámetro exterior entre 89,5 y 90,0 mm; interior 86 mm o menos con pared de 2 mm | S2, S6 | P2 | I |
| RD-03 | Largo total 230 mm (TBR); los dos sistemas de descenso plegados ocupan 60 mm de largo o menos (P1: 40–60 mm, 20–25 % del volumen) | S3 | P2, P1 | I |
| RD-04 | Paracaídas de etapa 1 para 15 m/s (admisible 12–18): ≈ 0,050 m² si es circular plano (Cd 0,8, Ø ≈ 25 cm) o ≈ 0,028 m² si es hemisférico (Cd 1,4, Ø ≈ 19 cm). Se abre solo al salir del cohete, sin actuador | C3 | P1 | A, E (caída desde dron) |
| RD-05 | Segundo sistema para 4,5 m/s (admisible 2–8): ≈ 0,55 m² si es circular plano (Ø ≈ 84 cm) o ≈ 0,31 m² si es hemisférico (Ø ≈ 63 cm) | C4 | P1 | A, E |
| RD-06 | Las dos velocidades se mantienen dentro de ± 3 m/s con ± 10 % de dispersión de Cd y la densidad del aire del sitio | C3, C4 | P1 | A, E (5 caídas o más con masa equivalente) |
| RD-07 | Anclaje y líneas del segundo sistema resisten el tirón de apertura (100 N o más), con línea elástica o amortiguador | C4, S5 | P1, P2 | A, E (tirón con balanza) |
| RD-08 | Barómetro muestreado a 10 Hz o más en vuelo y a 50 Hz o más al registrar ensayos de descenso; resolución de 1 m o mejor | C4, SN1 | P3 | A, E (cámara de vacío) |
| RD-09 | El software detecta el apogeo cuando la velocidad vertical estimada pasa de positiva a negativa en varias lecturas seguidas, y activa el segundo sistema con altitud de 0,8 × apogeo o menos en 3 lecturas seguidas | C4, F5 | P5 | A (simulación SILS), E |
| RD-10 | El mecanismo libera dentro de 1 s de recibir la orden (15 m de caída a 15 m/s) y se mantiene trabado con 30 G | C4, M3, S5 | P2 | E |
| RD-11 | Ventilación del barómetro hacia afuera: al menos 2 orificios de 6 mm | SN1 | P2 | I |
| RD-12 | Aceleración medida hasta ± 32 g o más para registrar el choque de 30 G: el MPU-6050 llega a ± 16 g, así que se suma un acelerómetro de mayor rango | SN5, S5 | P3 | I |
| RD-13 | Paquete de ≈ 118 bytes con 20 campos (contrato v0 de P6), con contador, identificador de equipo y CRC; tiempo en el aire menor a 500 ms | C5, X2, X4, X5 | P5, P6 | A, D |
| RD-14 | Radio en 915–928 MHz (pierde 8,5 dB menos que 2,4 GHz): XBee con máscara de canales limitada a 915–928 MHz, o LoRa con identificador de equipo en el paquete | X1, X2 | P3, P6 | I, D |
| RD-15 | Margen de enlace de 15 dB o más en el peor caso (distancia máxima, elevación alta por el nulo de la antena, polarización): ≈ 850 m con apogeo de 600 m y ≈ 1,8 km con 1.000 m | C5, G11 | P6 | A, E (pruebas de campo) |
| RD-16 | Potencia radiada de la estación de 36 dBm o menos (Res. 581/2018): con una Yagi de 11,1 dBi, 24,9 dBm o menos al transmisor | X1 | P6 | A |
| RD-17 | Aviso de separación dentro de 2 s de salir del cohete. Propuesta: usar el panel solar como sensor (oscuro dentro del cohete, luz al salir) combinado con la aceleración, como sugiere P5 | X3, E3 | P5, P3 | E |
| RD-18 | Batería con capacidad de 1,5 × consumo medio × 2,5 h o más; solo la radio XBee-PRO 900HP suma ≈ 60–93 mAh en 2 h (P6) | E7 | P4 | A, E (3 h o más cerrado) |
| RD-19 | Memoria FRAM con CRC por registro y watchdog que solo se alimenta si las tareas esenciales responden; al arrancar se lee la causa del reinicio | F1, F2, F5 | P5 | A, D (reinicio forzado) |
| RD-20 | Reloj de tiempo real DS3231 con batería propia; la hora se envía compensando el tiempo en el aire, desde una notebook sincronizada con desvío de 0,5 s o menos | F2, F3, G3 | P3, P5, P6 | D |
| RD-21 | Cámaras que empiezan a grabar al detectar el despegue y siguen hasta el aterrizaje, con memoria para el peor caso de 1.000 m. Si son ESP32-CAM (P3), cada una lleva su microSD y recibe la señal de arranque del procesador principal | C6, C7, SN6, SN7 | P3, P5 | A, D |
| RD-22 | Orificios de interruptores de 8 mm (menos de los 10 mm permitidos) | E4, E5, E9 | P2, P4 | I |
| RD-23 | Estación en una sola ventana, letra de 14 pt o más, contraste de 7:1 o más; notebook con autonomía medida de 3 h o más con radio, disco y brillo de uso al sol | G5, G9, G12, G13 | P6 | I, E |
| RD-24 | Costo de los componentes de vuelo de $800.000 o menos (20 % de margen bajo el límite) | C9 | Gestión | A |

De dónde salen los números:

  - **RD-04 y RD-05**: área = 2 × m × g / (ρ × Cd × v²), la fórmula de P1. Con 15 m/s da 0,0396 / Cd m²; con 4,5 m/s, 0,440 / Cd m². Los Cd son los de P1: circular plano 0,75–0,80, hemisférico 1,4–1,5, cruciforme 0,65–0,75.
  - **RD-05 a 4,5 m/s y no a 5**: cumple las dos lecturas de C4 (ver 1.6). P1 lee el promedio desde la activación del segundo sistema; con 4,5 m/s se cumple eso y también el promedio desde el apogeo.
  - **RD-15**: con viento de 5 m/s durante ≈ 120 s de descenso, la deriva es ≈ 600 m; con apogeo de 600 m la distancia a la estación es √(600² + 600²) ≈ 850 m. Con 1.000 m de altura y 1.500 m de distancia horizontal, P6 calcula 1.803 m.
  - **RD-19**: escribir a 1 Hz durante 2,5 h son 9.000 escrituras por vuelo. La EEPROM de un ATmega328P tolera 100.000 ciclos por celda ([hoja de datos, §12.4](https://fab.cba.mit.edu/classes/863.17/EECS/people/akaspar/project/atmega328p-datasheet.pdf)); por eso P5 propone FRAM.
  - **RD-21**: si las cámaras arrancan recién con la separación pueden perder la apertura del paracaídas de etapa 1; si graban desde el encendido necesitan memoria para más de 2 h.

## 1.4 Concepto de operaciones (CONOPS)

El vuelo tiene **8 fases, y el descenso completo dura ≈ 115 s** con un apogeo de 600 m: 8 s a 15 m/s y ≈ 107 s a 4,5 m/s. Los estados del software son los que propone P5. El momento crítico es la fase 5, donde el CanSat decide solo cuándo cambiar de sistema de descenso.

*Figura 1.1 – Perfil de vuelo (CONOPS):* [*abrir la imagen en Drive*](https://drive.google.com/file/d/1fLEWGdRl0rS9dtWzYY3-nnsVHtoCbZuU/view)

El número de cada fase del diagrama coincide con la tabla.

| Fase | Altura y velocidad | Duración | Estado del software (P5) | Qué pasa | Requisitos |
| --- | --- | --- | --- | --- | --- |
| 1 Rampa | 0 m | Hasta 2 h | STARTUP → STAND-BY | Se enciende por el orificio y se ve el LED; se enciende la baliza. La estación fija la hora UTC (SET_TIME) y calibra la altitud a cero (CAL_ALT). Se integra al cohete | G1, F3, E4, E6, E7, E9 |
| 2 Despegue y ascenso | 0 → ≈ 600 m | Segundos (TBD) | ASCENT | Detecta el despegue por aceleración; arrancan el video y la telemetría completa a 1 Hz, que la estación muestra también en el ascenso (G5) | C1, C5, G5, S4 |
| 3 Eyección | ≈ 600 m (TBR) | Instante | APOGEE | La carga de eyección lo expulsa; el panel solar pasa de oscuridad a luz y se envía el aviso de separación; el paracaídas de etapa 1 se abre solo. El apogeo se confirma cuando la velocidad vertical cambia de signo | C2, C3, S5, S7, X3 |
| 4 Etapa 1 | 600 → 480 m a 15 ± 3 m/s | ≈ 8 s | DESCENT 1 | Guarda la altitud máxima en FRAM; mide y transmite | C3, C5, C6, C7 |
| 5 Cambio | 480 m (80 %) | 1 s o menos | Transición a DESCENT 2 | Con 3 lecturas seguidas bajo 0,8 × apogeo activa el mecanismo; se despliega el segundo sistema y lo filman las dos cámaras | C4, M1–M3, SN6 |
| 6 Etapa 2 | 480 → 0 m a ≈ 4,5 m/s | ≈ 107 s | DESCENT 2 | Sigue midiendo y transmitiendo a 1 Hz | C4, C5 |
| 7 Aterrizaje | 0 m | — | LANDED | Con altitud y aceleración estables unos segundos, detiene el video y sigue transmitiendo la posición GPS; suena la baliza | C8, SN4 |
| 8 Recuperación | — | — | — | Se localiza con la última posición GPS y la baliza; se comparan los CSV principal y de respaldo y se guardan los videos para los jueces | G2, C8 |

Puntos de diseño que salen de la tabla:

  - El estado del software se guarda en memoria no volátil: si el procesador se reinicia en vuelo, retoma el estado en que estaba (F5, RD-19).
  - Qué hace el CanSat después de aterrizar es una propuesta: el scoresheet pregunta cómo termina la transmisión al aterrizar (ítem 54).
  - Para la diapositiva 16 alcanzan el diagrama y una línea por fase. La secuencia de eventos del día de lanzamiento (desde la llegada al sitio hasta el análisis de datos) es otra diapositiva del scoresheet y se arma con la pestaña 10.

## 1.5 Matriz de verificación

Los 65 requisitos con **quién responde, cómo se verifica y en qué ítem del scoresheet se muestra**. Es la base de la diapositiva de cumplimiento, que el scoresheet puntúa dos veces: una por la tabla y otra por que esté completa. Métodos: A análisis, I inspección, D demostración, E ensayo.

En la plantilla, el ítem *n* está en la diapositiva *n* + 3. Al final, con las diapositivas agregadas, la columna de ítems se reemplaza por los números de diapositiva reales. El estado de cada requisito se lleva en la pestaña 12 del Google Doc.

| Req. | Resumen | Responsable | Método | Cómo se verifica | Ítems |
| --- | --- | --- | --- | --- | --- |
| C1 | Va en la parte superior del fuselaje | Mecánica | I | Plano de integración y fit check | 11, 14 |
| C2 | Se despliega con la carga de eyección | Mecánica | A, E | Análisis de salida; expulsión simulada desde un tubo | 13, 14 |
| C3 | Paracaídas automático a 15 ± 3 m/s | Descenso | A, E | Cálculo de área; caída desde altura midiendo velocidad con el barómetro | 32–34 |
| C4 | Segundo sistema al 80 % del apogeo, 5 ± 3 m/s promedio | Descenso | A, E | Simulación con perfil de altitud; ensayo de vacío; caída desde altura | 35, 36, 40, 67 |
| C5 | Telemetría a 1 Hz | C&DH | D | 10 min de registro en la estación con un paquete por segundo | 54, 55 |
| C6 | Video del descenso hacia cenit | Sensores | D | Video del ensayo de caída con el despliegue visible | 28, 29 |
| C7 | Video del descenso hacia nadir | Sensores | D | Ídem, cámara inferior | 30, 31 |
| C8 | Baliza audible independiente | EPS | I, D | Circuito separado; se oye a distancia con la electrónica apagada | 57, 58 y baliza |
| C9 | Costo menor a $1.000.000 | Gestión | A | Tabla de presupuesto | 80 |
| S1 | Masa 500 ± 10 g | Mecánica | A, I | Presupuesto de masa; balanza | 42–46 |
| S2 | Diámetro de 90 mm | Mecánica | I | Calibre | 9, 14 |
| S3 | Largo de 200 a 250 mm | Mecánica | I | Medición con los sistemas plegados | 9, 14 |
| S4 | Soporta 15 G de vibración | Mecánica | E | Ensayo de vibración | 78 |
| S5 | Soporta 30 G de choque | Mecánica | E | Ensayo de caída con cordón | 78 |
| S6 | Pared de 2 mm o más, sin deformarse | Mecánica | I, A | Calibre; cálculo de tensiones; ensayo térmico | 38, 78 |
| S7 | Sale libre de la sección del cohete | Mecánica | E | Fit check en ambas orientaciones | 14 |
| S8 | Todo montado de forma fija | Mecánica | I | Revisión después del ensayo de vibración | 39 |
| S9 | Materiales no contaminantes | Mecánica | I | Lista de materiales | 37 |
| M1 | Sin actuadores pirotécnicos ni químicos | Mecánica | I | Revisión del diseño | 40 |
| M2 | Mecanismos por calor no expuestos | Mecánica | I | Revisión del diseño | 40 |
| M3 | Mecanismos mantienen su estado bajo carga | Mecánica | E | Activación después de vibración y caída | 40, 78 |
| M4 | Sin contactos de resorte en baterías | Mecánica | I | Revisión de la conexión de baterías | 39, 59 |
| E1 | Sin baterías LiPo | EPS | I | Hoja de datos | 59 |
| E2 | Solo tipos de batería permitidos | EPS | I | Hoja de datos | 59 |
| E3 | Panel solar que emite una señal con luz | EPS | D | Valor al sol y a la sombra, leído por telecomando | 57 |
| E4 | Interruptor accesible para STAND-BY | EPS | D | Encender con el CanSat cerrado | 10, 58 |
| E5 | Orificios de acceso de 10 mm o menos | Mecánica | I | Calibre | 9, 10 |
| E6 | Indicador de encendido | EPS | I, D | LED visible desde afuera | 58 |
| E7 | Funciona 2 h o más integrado | EPS | A, E | Presupuesto de energía; ensayo de autonomía cerrado | 65 |
| E8 | Baliza con batería propia | EPS | I | Esquema eléctrico | 58 |
| E9 | Interruptor de la baliza accesible | EPS | D | Encender con el CanSat cerrado | 10 |
| X1 | Bandas 915–928 MHz o 2400–2483,5 MHz | C&DH | I | Hoja de datos y configuración | 53 |
| X2 | Sin modo broadcast | C&DH | I, D | Unicast (XBee) o identificador de equipo en el paquete (LoRa); un segundo receptor no la acepta; respuesta de la CONAE | 53 |
| X3 | Aviso automático al separarse | FSW | E | Separación simulada | 54, 67 |
| X4 | Un paquete por segundo | C&DH | D | 60 paquetes por minuto en la prueba de enlace completo | 54 |
| X5 | Contenido mínimo de la telemetría | C&DH | I, D | Ejemplo de paquete real | 55 |
| X6 | Batería y panel solar por telecomando | C&DH | D | Enviar el comando y ver la respuesta | 56 |
| SN1 | Altitud por presión | Sensores | E | Cámara de vacío o altura conocida | 16, 17 |
| SN2 | Temperatura interna | Sensores | D | Lectura frente a un termómetro | 18, 19 |
| SN3 | Voltaje de la batería | Sensores | E | Comparación con multímetro | 20, 21 |
| SN4 | Posición por GPS | Sensores | D | Posición válida al aire libre | 22, 23 |
| SN5 | Aceleración y rotación | Sensores | D | Lecturas al mover y girar el CanSat | 24–27 |
| SN6 | Video del despliegue | Sensores | D | Video del ensayo de caída | 28, 29 |
| SN7 | Video color de 640×480 o más | Sensores | I | Propiedades del archivo | 28–31 |
| SN8 | Corriente de la batería | Sensores | E | Comparación con multímetro | 20, 21 |
| G1 | Comando de calibración de altitud cero | GCS | D | Enviar CAL_ALT y ver menos de ± 1 m en los paquetes siguientes | 74 |
| G2 | CSV en la notebook y en respaldo | GCS | D | CSV principal y de respaldo con suma de verificación idéntica | 74 |
| G3 | Tiempo de misión con resolución de 1 s | GCS | I, D | Columna en el paquete y en pantalla | 55, 74 |
| G4 | Estación desarrollada por el equipo | GCS | I | Código propio | 69, 70 |
| G5 | Telemetría en texto en tiempo real | GCS | D | Pantalla durante un ensayo | 74 |
| G6 | Unidades del SI en pantalla | GCS | I | Revisión de la pantalla | 74 |
| G7 | Gráficos en tiempo real | GCS | D | Pantalla durante un ensayo | 74 |
| G8 | Tiempo, temperatura, GPS, paquetes y estado en pantalla | GCS | D | Pantalla durante un ensayo | 74 |
| G9 | Notebook con 2 h de batería, radio y antena | GCS | I, E | Autonomía medida de 3 h o más con radio, disco y brillo al sol | 70 |
| G10 | Portátil, sin corriente alterna | GCS | D | Operación completa a batería | 70, 72 |
| G11 | Antena de mesa o de mano | GCS | I | Diseño del soporte | 71–73 |
| G12 | Legible al sol | GCS | I | Prueba al sol con la notebook real; contraste de 7:1 o más | 74 |
| G13 | Todo en una pantalla, sin pestañas | GCS | I | Revisión de la pantalla | 74 |
| G14 | Conteo de paquetes recibidos | GCS | D | Caso de prueba con pérdidas conocidas, usando el contador de F1 | 74 |
| G15 | Envío de telecomandos | GCS | D | Enviar cada comando | 56, 74 |
| F1 | Contador de paquetes que sobrevive reinicios | FSW | D | Reinicio forzado en plena transmisión (prueba 4 de P5) | 66, 67 |
| F2 | Tiempo de misión que sobrevive reinicios y cortes | FSW | D | Reinicio y corte de energía | 67 |
| F3 | Hora UTC por comando, ± 1 s | FSW | D | SET_TIME desde una notebook sincronizada (desvío de 0,5 s o menos) y comparar | 56, 67 |
| F4 | Comandos documentados en el manual | FSW | I | Manual de misión | 56 |
| F5 | Estados de configuración que sobreviven reinicios | FSW | D | Reinicio en cada estado del software | 67 |

El ítem de la baliza (*Cansat beacon Information*) y la secuencia de eventos no tienen número ni diapositiva en la plantilla.

## 1.6 Ambigüedades y preguntas abiertas

Varios requisitos admiten más de una lectura. La regla propuesta: **elegir la lectura que cumple todas las interpretaciones a la vez cuando se puede, y consultar el resto**. En la PDR conviene mostrar la lectura elegida: demuestra comprensión de los requisitos, que es lo primero que piden las Bases (§6).

| Tema | Qué dicen las fuentes | Cómo lo leemos mientras tanto | ¿Consultar? |
| --- | --- | --- | --- |
| Cuándo es "80 % de la altitud máxima" (C4) | No dice si en subida o bajada. P1 señala otra lectura: haber bajado el 80 % del trayecto (0,2 × apogeo) | En la bajada y a 0,8 × apogeo: el texto dice "al alcanzar el 80 % de la altitud máxima", y en la subida el CanSat está dentro del cohete | Sí, para confirmar |
| Promedio de 5 m/s "durante todo el descenso" (C4) | No dice si se promedia desde el apogeo o desde el 80 %. P1 lo lee desde la activación del segundo sistema | Diseñar la etapa 2 a ≈ 4,5 m/s cumple las dos lecturas: 4,5 m/s desde el 80 % y ≈ 5,2 m/s promediando desde el apogeo (con 600 m) | Sí, para confirmar |
| Contenedor y carga útil (C2, S1, S7) | Hablan de ambos; ninguno dice que se separen. El scoresheet asume que sí | Un solo cuerpo con descenso en dos etapas (Sección 2, opción B) | Sí |
| Medidas (S2, S3, Bases §4) | Anexo: Ø 90 mm y 200–250 mm. Bases: cilindro de 95 × 200 mm | 90 mm de diámetro máximo; 95 mm sería el tubo del cohete; largo de 230 mm | Sí |
| Apogeo | Bases: "más de 500 m" | 600 m para tiempos de descenso y 1.000 m como peor caso de enlace y memoria (P6 usó 1.000 m) | Sí |
| "Enviar un comando" al separarse (X3) | El CanSat no recibe la orden, la envía | Al detectar la separación, el software lo informa en la telemetría como un evento con su hora; la estación lo registra y lo muestra (P6) | Sí, para confirmar |
| Desde cuándo se transmite (X3, G5) | X3 marca el comienzo de misión en la separación; G5 pide mostrar la telemetría durante el ascenso y el descenso | Transmitir desde el despegue, dentro del cohete; la separación marca el comienzo de misión | Sí (P6) |
| Tiempo de misión (G3, F2) | No dice si es hora UTC o tiempo transcurrido | Enviar ambos: hora UTC y segundos desde el inicio de misión | Sí (P6) |
| Estado de batería: ¿siempre o por comando? (X6, G7) | X6: por telecomando. G7: graficar voltaje y corriente en tiempo real | Voltaje y corriente en todos los paquetes (campos 8 y 9 del contrato v0) y respuesta completa a GET_BATT_SOL | No |
| Panel solar que "emite una señal" (E3, X6) | No dice si alimenta algo | Medir la tensión del panel con el ADC del ESP32 y enviarla por telecomando; no alimenta nada. Sirve además para detectar la separación (RD-17) | Sí, para confirmar |
| Unidades de rotación (G6) | G6 pide SI; la unidad coherente es rad/s, y °/s es aceptada para uso con el SI | Mostrar en rad/s hasta que la CONAE acepte °/s | Sí (P6) |
| Cuándo empieza el video (C6, C7, E7) | "Toda la secuencia de descenso", con 2 h de espera en el cohete | Empezar a grabar al detectar el despegue (RD-21) | No |
| Telemetría durante las 2 h de espera (E4, E7) | E4 habla de STAND-BY, sin definirlo | En STAND-BY: bajo consumo y telemetría reducida; al detectar el despegue, telemetría completa | Sí |
| Formato de telemetría | El scoresheet remite a la sección 3.3 de un *Mission Guide* que no está publicado | Contrato v0 de P6: texto separado por comas, 20 campos | Sí |
| Canales entre equipos (X1) | Varios equipos en la misma banda, sin protección contra interferencias (Res. 581/2018) | Canal e identificador de equipo propios | Sí (P6) |
| 55 o 65 requisitos | Scoresheet: 55. Anexo A: 65 | Tabla de cumplimiento con los 65 | Sí |
| Ítems del scoresheet sin requisito (huevo, ojiva, cáncamo, parapente) | Están en el scoresheet y no en el Anexo A | Presentar esas diapositivas como "No aplica", citando el Anexo A, o adaptadas | Sí |

### Preguntas para la CONAE

Las Bases (§2) solo aceptan consultas por mail durante la inscripción; para la PDR, canalizarlas por el Aula Virtual o el docente responsable. Están también en la pestaña 13 del Google Doc.

  - ¿Qué apogeo se espera, y qué cohete se usa?
  - En C4, ¿el 80 % es 0,8 × altitud máxima? ¿El promedio de 5 m/s se calcula desde el apogeo o desde el 80 %?
  - ¿C4 exige separar físicamente la carga útil del contenedor?
  - En X3, ¿alcanza con informar la separación como un evento en la telemetría?
  - ¿La telemetría debe empezar en el despegue o en la separación? ¿Qué debe transmitir el CanSat durante las 2 h de espera?
  - ¿El tiempo de misión (G3) es hora UTC o tiempo transcurrido? ¿Se admiten °/s para las rotaciones (G6)?
  - ¿Satisface X2 un enlace LoRa con identificador de equipo en el paquete? ¿Cómo se reparten los canales entre equipos? ¿Se exige homologación de ENACOM a los módulos?
  - ¿Hay un formato de telemetría obligatorio?
  - ¿La tabla de cumplimiento es de 55 o de 65 requisitos, y cómo se presentan los ítems del scoresheet que no están en el Anexo?
  - ¿Se puede presentar la PDR en español?

### Preguntas para el equipo

  - ¿Aceptamos el apogeo de diseño de 600 m y el presupuesto de masa por subsistema (RD-01)?
  - ¿Quién arma las diapositivas 7, 8 y 16 y la de cumplimiento?
  - ¿Sumamos los objetivos secundarios OS1 y OS2?
  - ¿Cada responsable revisa sus requisitos derivados antes de la próxima reunión?

## 1.7 Coherencia entre las investigaciones

Las investigaciones coinciden en lo principal: ESP32 como procesador, máquina de estados, FRAM con CRC y watchdog, reloj DS3231, celdas 18650, INA219, GPS NEO-M8N, servo con pasador para el mecanismo y pruebas de simulación antes del vuelo. **Hay 13 diferencias que conviene cerrar antes de comprar más componentes o escribir código.** Las cuatro primeras de la tabla son las más urgentes.

| Tema | Qué dice cada investigación | Propuesta | Quién decide | Requisitos |
| --- | --- | --- | --- | --- |
| Banda de radio | Presupuesto: XBee S2C de 2,4 GHz. P6: 915–928 MHz con XBee-PRO 900HP o LoRa SX1276, porque 2,4 GHz pierde 8,5 dB más | 915 MHz, decidido antes de comprar la radio. Si se mantiene el S2C, P6 rehace el presupuesto de enlace a 2,4 GHz | P3 y P6 | X1, X2, C5 |
| Formato de telemetría | P5: 15 campos, sin rotaciones, corriente ni identificador de equipo. P6: contrato v0 de 20 campos | Adoptar el contrato v0 de P6, que cubre X5, G7, G8 y X2; P5 lo revisa y lo firma | P5 y P6 | X5, G7, G8, X2 |
| Comandos | P5: $CMD,STATUS, CAL_ZERO, TIME, POLL_PWR. P6: CMD,<equipo>,<nombre>,<parámetro> con CAL_ALT, SET_TIME, GET_BATT_SOL y respuesta ACK o NACK | Una sola lista con el formato y los nombres de P6 (el identificador de equipo ayuda con X2); P5 suma STATUS. Los dos firman el manual de comandos (F4) | P5 y P6 | G1, G15, F3, F4, X6 |
| Cámaras | Presupuesto: sin definir. P3: dos ESP32-CAM, cada una con su microSD | Si son ESP32-CAM, sumar dos placas al presupuesto de masa y de energía y definir la señal de arranque desde el ESP32 principal (RD-21) | P3, P4 y P5 | C6, C7, SN7, E7 |
| Batería | P3 menciona una "batería LiPo" al hablar del voltaje. Presupuesto: celdas 18650 | Corregir el texto de P3: LiPo está prohibida (E1). La cantidad de celdas define si la potencia entra en sus 70 g: cada 18650 pesa ≈ 47 g | P3 y P4 | E1, E2, S1 |
| Servos y etapa 1 | Presupuesto: dos MG90S, uno para soltar el paracaídas de la etapa 1. C3 dice que la etapa 1 se despliega sola con la eyección; la Sección 2 y P1 prevén un solo mecanismo | Etapa 1 pasiva (sale con la eyección o por arrastre de la tapa, como propone P1); un servo para la etapa 2 y el segundo como repuesto | P1 y P2 | C3, C4, M3 |
| Barómetro | Presupuesto: BMP280. P3: BMP388, con resolución de ≈ 13 cm | Presentar los dos en el trade de los ítems 16 y 17, que pide dos opciones, y elegir con RD-08 | P3 | SN1, C4 |
| Temperatura | Presupuesto: la del propio barómetro. P3: un DS18B20 aparte | Trade de los ítems 18 y 19 con las dos opciones; si alcanza el sensor del barómetro, es un componente menos | P3 | SN2 |
| Acelerómetro | El MPU-6050 llega a ± 16 g y el choque es de 30 G (lo advierte el propio presupuesto) | Sumar un acelerómetro de mayor rango (RD-12) | P3 | SN5, S5 |
| Apogeo supuesto | Sección 1: 600 m. P6: 1.000 m | Usar los dos: 600 m nominal y 1.000 m como peor caso (RD-15, RD-21) | P1 y P6 | C4, C5 |
| Velocidad de la etapa 2 | P1: 5 m/s desde la activación del segundo sistema. Sección 1: 4,5 m/s | 4,5 m/s, que cumple las dos lecturas de C4 y queda dentro de 2–8 m/s | P1 | C4 |
| Segundo sistema de descenso | P1 compara paracaídas, parapente y rotor; el scoresheet espera un parapente | Paracaídas como línea base, por menor complejidad y volumen; el parapente queda documentado para el trade de los ítems 35 y 36 | P1 | C4 |
| Detección del apogeo | Sección 1: máximo de la altitud. P5: cambio de signo de la velocidad vertical en varias lecturas | La de P5, más robusta frente al ruido; se guarda igual la altitud máxima para calcular el 80 % | P5 | C4 |

### Lo que falta

  - Investigación de potencia (P4): presupuesto de energía en Wh para las 2 h de E7, con el consumo de radio, cámaras y servos (RD-18).
  - Responsable de gestión: presupuesto en pesos contra C9 y cronograma.
  - Revisar la planilla del presupuesto provisorio contra RD-01 (masa) y RD-24 (costo); en esta versión solo se leyó la lista de componentes.

## Fuentes

  - Bases y Condiciones CanSat Universitario 2026/2027 (CONAE), archivo del proyecto
  - Anexo A v2, Requisitos de misión (CONAE), archivo del proyecto
  - Scoresheet V2 de la PDR, archivo del proyecto
  - PDR Template V2, plantilla de diapositivas de la CONAE, archivo del proyecto
  - Investigaciones del equipo (Etapa 2, Revisión Preliminar de Diseño): descenso (P1), presupuesto provisorio de componentes, sensores y payload (P3), software de vuelo y telemetría (P5) y estación terrena (P6)
  - Sección 2 – Mecánica y estructura (P2), documento del equipo
  - [NASA Systems Engineering Handbook (NASA/SP-2016-6105 Rev2)](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf)
  - [Hoja de datos ATmega328P (Atmel)
    ](https://fab.cba.mit.edu/classes/863.17/EECS/people/akaspar/project/atmega328p-datasheet.pdf)
