# 0. Inicio

> Pestaña 0 de la *PDR CanSat Universitario – Guía de desarrollo* (Google Docs), migrada al repo el 10/11/2026. Desde la migración se edita acá; ver la sección "La Guía de Drive y el repo" del README.

Documento de trabajo del equipo para entender, diseñar y decidir el CanSat tema por tema. Al final se vuelca en la plantilla de diapositivas de la CONAE, que es lo único que se entrega.

## Qué se entrega

  - Solo el paquete de diapositivas PDR, en **PDF**, armado sobre la plantilla de la CONAE y subido al Aula Virtual. No hay un documento escrito aparte.
  - La diapositiva 3 pide el **link a un video** de presentación del diseño preliminar.
  - El jurado puntúa con el Scoresheet V2: 2 puntos por ítem y 10 por la calidad de la presentación, 262 en total. Fuera de término o en otro formato, el equipo queda eliminado.

## Fechas clave

| Fecha | Hito |
| --- | --- |
| 14 oct 2026 | Reunión virtual de lineamientos (ya hecha) |
| 17 al 21 nov 2026 | Envío del PDR y revisiones virtuales |
| 23 al 27 nov 2026 | Lista de mérito: pasan 20 equipos |
| 31 mar 2027 | Entrega del CDR |
| 5 al 9 abr 2027 | Presentaciones del CDR: pasan 6 finalistas |

Fuente: [Cronograma oficial de la CONAE](https://www.argentina.gob.ar/ciencia/conae/cansat-argentina/requisitos-cansat-universitario/cronograma).

## Cómo se usa cada pestaña

Cada pestaña es un subsistema. Cada subsección tiene el mismo formato:

1.  **Qué pide**: los requisitos del Anexo A y los ítems del scoresheet que corresponden. Ya está cargado; no hay que tocarlo.
2.  **Qué hay que entender**: los apuntes de investigación. Lo que hay que aprender antes de poder comparar opciones: conceptos, fórmulas, cálculos y los links de donde sale cada dato. Sirve para que el resto del equipo entienda el tema sin investigar de cero y para poder responder si el jurado pregunta.

    1.  Ejemplo (paracaídas): qué es la velocidad terminal y cómo se calcula; qué es el coeficiente de arrastre (Cd) y cuánto vale para cada tipo de paracaídas; qué materiales se usan y cuánto pesan.
3.  **Opciones**: al menos dos alternativas con sus datos, comparadas en la tabla. El jurado puntúa esta comparación (trade).
4.  **Decisión**: la opción elegida y por qué, en una o dos líneas, citando el requisito que cumple. Esa frase se copia a la pestaña 12 y pasa casi igual a la diapositiva de selección.

    1.  Ejemplo (números inventados): "Paracaídas hemisférico de 30 cm de nylon: con 500 g da 14 m/s, dentro de lo que pide C3 (15 ± 3 m/s), y es el más fácil de plegar".
5.  **Pendientes**: lo que todavía no está resuelto o hay que verificar después, para que nada quede olvidado entre reuniones. Cuando se resuelve, se borra o se pasa a Decisión.

    1.  Ejemplo: confirmar el Cd con una prueba de caída; recalcular cuando se cierre la masa final; esperar la respuesta de la CONAE sobre el diámetro.

En resumen: entender es investigar, opciones es comparar, decisión es elegir y pendientes es lo que queda abierto.

Reglas del equipo:

  - Cada decisión cita el requisito que cumple (por ejemplo S1 o C3) y se anota en la pestaña 12.
  - Cada contradicción o duda con la CONAE va a la pestaña 13.
  - Unidades del SI: masas en gramos, energía en Wh, velocidades en m/s.
  - Los ítems marcados *(sin diapositiva)* los puntúa el scoresheet, pero la plantilla no los trae: hay que agregar esas diapositivas.

## Orden de trabajo

1.  Misión y requisitos (pestaña 1).
2.  Arquitectura y presupuesto de masa (pestaña 2).
3.  Mecánica y descenso (pestañas 3 y 4): definen el espacio disponible.
4.  Sensores, C&DH y potencia (pestañas 5 a 7).
5.  Software de vuelo y estación terrena (pestañas 8 y 9).
6.  Pruebas, operaciones y gestión (pestañas 10 y 11).

## Estado por pestaña

| Pestaña | Qué contiene | Responsable | Estado |
| --- | --- | --- | --- |
| 1. Misión y requisitos | Resumen de misión, los 65 requisitos, CONOPS |   | Sin empezar |
| 2. Arquitectura y masa | Configuraciones A y B, dimensiones, presupuesto de masa |   | Sin empezar |
| 3. Mecánica y estructura | Estructura, contenedor, mecanismos, montaje de cámaras | Joaquín Sánchez | Sin empezar |
| 4. Control de descenso | Paracaídas, segundo sistema, cálculos de velocidad |   | Sin empezar |
| 5. Sensores | Trade y selección de cada sensor y cámara | Tabarez | Sin empezar |
| 6. Procesamiento y comunicaciones | Procesador, memoria, RTC, radio, telemetría, comandos | Tabarez | Sin empezar |
| 7. Potencia | Batería, presupuesto de energía, baliza |   | Sin empezar |
| 8. Software de vuelo | Arquitectura, estados, reinicios, modo simulación |   | Sin empezar |
| 9. Estación terrena | Hardware, antena, interfaz, CSV |   | Sin empezar |
| 10. Pruebas y operaciones | Planes de prueba, secuencia de eventos, recuperación |   | Sin empezar |
| 11. Gestión | Equipo, presupuesto, cronograma, riesgos, armado final | Tabarez y Bojanovich | Sin empezar |
| 12. Decisiones y cumplimiento | Tabla de cumplimiento y registro de decisiones |   | Sin empezar |
| 13. Dudas y consultas CONAE | Contradicciones a consultar |   | Sin empezar |
| 14. Glosario y fuentes | Siglas y fuentes |   | Sin empezar |
