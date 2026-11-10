# Anexo A v2 — Requisitos de misión

Transcripción del PDF oficial (`originales/anexo-a-v2.pdf`) para que los agentes puedan leerla. Ante cualquier diferencia, manda el PDF.

## Operativos

| ID | Requisito |
| --- | --- |
| C1 | El contenedor del CanSat estará montado dentro del fuselaje del cohete, en la parte superior del cohete. |
| C2 | La carga útil y el contenedor del CanSat se desplegarán del cohete cuando se active la carga de expulsión del motor del cohete. |
| C3 | Después del despliegue, el CanSat SE ACTIVARÁ y descenderá a 15 metros/segundo utilizando un paracaídas que se despliega automáticamente. El error permitido es de +/- 3 m/s. |
| C4 | Al alcanzar el 80% de la altitud máxima de vuelo, el CanSat liberará otro sistema de descenso que asegurará que descenderá a un promedio de 5 metros/segundo durante todo el descenso, con un margen de +/- 3 metros/seg. |
| C5 | La telemetría de los sensores se transmitirá a una frecuencia de 1 Hz. |
| C6 | La carga útil grabará en video toda la secuencia de descenso, apuntando a cenit, para evidenciar la corriente activación de los sistemas de descenso. |
| C7 | La carga útil grabará en video toda la secuencia de descenso, apuntando a nadir, para evidenciar la corriente activación de los sistemas de descenso. |
| C8 | La carga útil del CanSat incluirá una baliza audible que se encienda por separado y sea independiente de la batería y la electrónica del CanSat. |
| C9 | El costo del CanSat debe ser inferior a $1.000.000. Las herramientas de análisis y soporte en tierra no están incluidas en el costo del CanSat. |

## Estructurales

| ID | Requisito |
| --- | --- |
| S1 | La masa combinada del CanSat y el contenedor debe ser de 500 gramos +/- 10 gramos. |
| S2 | El diámetro del CanSat debe ser de 90 mm. |
| S3 | La longitud total, incluidos los sistemas de descenso, debe encontrarse en el rango de 200 mm a 250 mm. |
| S4 | La estructura del CanSat debe soportar vibraciones de 15 Gs. |
| S5 | El CanSat debe soportar un impacto de choque de 30 Gs. |
| S6 | El grosor de la pared del exterior debe ser de al menos 2 mm cuando se imprima en 3D y no debe flexionarse ni deformarse bajo tensión. |
| S7 | El cilindro del CanSat puede utilizarse para sujetar cualquier pieza desplegable de la carga útil, pero debe permitir que se deslice libremente fuera de la sección del cohete. |
| S8 | Todos los componentes electrónicos y mecánicos deben estar montados de forma fija utilizando soportes adecuados, tales como separadores, tornillos o adhesivos de alto rendimiento. |
| S9 | Los materiales del contenedor del CanSat no deberán ser contaminantes ni perjudiciales para el ambiente. |

## Mecanismos

| ID | Requisito |
| --- | --- |
| M1 | No se permiten actuadores pirotécnicos ni químicos. |
| M2 | Los mecanismos que utilicen calor (p. ej., hilo de nicrom) no deben estar expuestos al entorno exterior para reducir el riesgo potencial de incendiar la vegetación. |
| M3 | Todos los mecanismos deben ser capaces de mantener su configuración o estados bajo todas las fuerzas aplicadas. |
| M4 | No se deben utilizar contactos de resorte para realizar conexiones eléctricas a las baterías. Las fuerzas de choque pueden provocar desconexiones momentáneas. |

## Eléctricos

| ID | Requisito |
| --- | --- |
| E1 | No se permiten baterías de polímero de litio. |
| E2 | La fuente de batería puede ser alcalina, Ni-Cad, Ni-MH o Litio. Las celdas de litio deben estar fabricadas con un empaque metálico similar a las celdas 18650. Se permiten baterías de botón. |
| E3 | Se deberá colocar uno o más paneles solares que reciban la radiación solar a fines de emitir una señal cuando reciban radiación. |
| E4 | Se requiere un interruptor de encendido fácilmente accesible a través del contenedor, para colocar la carga útil en estado STAND-BY. |
| E5 | El contenedor debe tener pequeños orificios de acceso para los interruptores de encendido, de no más de 10 mm. |
| E6 | Se requiere un indicador de encendido. |
| E7 | El CanSat debe funcionar durante un mínimo de dos horas cuando esté integrado en el cohete. |
| E8 | La baliza de audio debe funcionar con una batería independiente. |
| E9 | La baliza de audio debe tener un interruptor de encendido fácilmente accesible a través del contenedor. |

## Comunicaciones

| ID | Requisito |
| --- | --- |
| X1 | Se utilizarán radios que trabajen en las frecuencias autorizadas por ENACOM: 915 – 928 MHz y 2400 – 2483.5 MHz. |
| X2 | Las radios no deben utilizar el modo de difusión (broadcast). |
| X3 | La telemetría deberá enviar un comando automáticamente cuando el CanSat se separe del cohete (comienzo de misión). |
| X4 | El CanSat transmitirá la telemetría una vez por segundo. |
| X5 | La telemetría del CanSat debe incluir altitud, presión atmosférica, temperatura, aceleraciones y rotaciones en los tres ejes y coordenadas GPS que incluyan latitud, longitud, altitud y número de satélites rastreados. |
| X6 | Mediante un telecomando, la telemetría debe transmitir el estado de la batería y la señal recibida por los paneles solares. |

## Sensores

| ID | Requisito |
| --- | --- |
| SN1 | La carga útil del CanSat medirá su altitud utilizando la presión atmosférica. |
| SN2 | La carga útil del CanSat medirá su temperatura interna. |
| SN3 | La carga útil del CanSat medirá el voltaje de su batería. |
| SN4 | La carga útil del CanSat rastreará su posición mediante GPS. |
| SN5 | La carga útil del CanSat medirá sus tasas de aceleración y rotación. |
| SN6 | La carga útil del CanSat grabará en video el despliegue los sistemas de descenso. |
| SN7 | Las cámaras de video deben grabar en color y con una resolución mínima de 640x480. |
| SN8 | La carga útil del CanSat medirá la corriente de su batería. |

## Estación Terrena

| ID | Requisito |
| --- | --- |
| G1 | La estación terrena enviará un comando al CanSat para calibrar la altitud a cero cuando el CanSat esté en la plataforma de lanzamiento antes del despegue. |
| G2 | La estación terrena generará archivos CSV con todos los datos de los sensores, que se grabarán en la computadora de la estación terrena y en un disco de respaldo. |
| G3 | La telemetría debe incluir el tiempo de misión con una resolución de 1 segundo. |
| G4 | Cada equipo deberá desarrollar su propia estación terrena. |
| G5 | Toda la telemetría se mostrará en tiempo real en formato de texto durante el ascenso y el descenso en la estación terrena. |
| G6 | Toda la telemetría se mostrará en el Sistema Internacional de Unidades (SI) y las unidades deberán indicarse en las pantallas. |
| G7 | Los equipos graficarán la altitud, el voltaje de la batería, la corriente de la batería, los valores del acelerómetro y las tasas de rotación en tiempo real. |
| G8 | Los equipos mostrarán el tiempo de misión, la temperatura, la posición GPS, el recuento de paquetes recibidos, el recuento de paquetes perdidos y el estado del software de vuelo en tiempo real. |
| G9 | La estación terrena debe incluir una computadora portátil con un mínimo de dos horas de autonomía de batería, una radio y una antena. |
| G10 | La estación terrena debe ser portátil para que el equipo pueda ubicarse en el sitio de operación de la estación terrena a lo largo de la línea de vuelo. No habrá energía de CA disponible en el sitio de operación. |
| G11 | La estación terrena utilizará una antena de mesa o portátil. |
| G12 | Debido a que la estación terrena debe visualizarse bajo luz solar intensa, las pantallas deben diseñarse teniendo esto en cuenta, incluyendo el uso de fuentes más grandes (mínimo 14 puntos), trazos de gráficos y ejes en negrita, y un tema de texto oscuro sobre fondo claro. |
| G13 | Todos los datos se mostrarán simultáneamente en la interfaz gráfica (GUI) de la estación terrena. No se permiten pestañas. |
| G14 | El sistema terreno contará el número de paquetes recibidos. Tenga en cuenta que este número no es equivalente al contador de paquetes transmitidos, sino al conteo de paquetes recibidos con éxito en la estación terrena durante la duración del vuelo. |
| G15 | La estación terrena debe ser capaz de enviar telecomandos. |

## Software Vuelo

| ID | Requisito |
| --- | --- |
| F1 | El software de vuelo mantendrá un recuento de los paquetes transmitidos que se incrementará con cada transmisión de paquetes a lo largo de la misión. El valor se mantendrá a través de reinicios del procesador. |
| F2 | El CanSat mantendrá el tiempo de misión a lo largo de toda la misión, incluso en caso de reinicios del procesador o pérdida momentánea de energía. |
| F3 | El CanSat debe tener su tiempo configurado mediante un comando terreno con un margen de un segundo con respecto al tiempo UTC antes del lanzamiento. |
| F4 | El vuelo incluirá comandos para requerir información adicional. Estos comandos deberán estar documentados en el manual de la misión. |
| F5 | Los estados de configuración, como la calibración de altitud cero y el estado del software, se mantendrán en caso de un reinicio del procesador durante el lanzamiento y la misión. |
