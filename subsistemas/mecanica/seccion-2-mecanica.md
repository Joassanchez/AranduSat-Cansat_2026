# Sección 2 – Mecánica y estructura (PDR CanSat Universitario)

Migrado del documento de trabajo del 2 de noviembre de 2026 (autor: Joaquín). Los diagramas del original no se migraron; quedan pendientes de exportar a `figuras/` (marcados como **[Figura pendiente]**).

## Alcance

Este es un **documento de trabajo** para que el equipo entienda los temas de mecánica y estructura y termine de definirlos juntos. Cada tema explica los conceptos, muestra las opciones con sus ventajas y desventajas, y cierra con una propuesta inicial y preguntas para discutir. Nada de lo que dice "propuesta" está cerrado. Los conceptos básicos (contenedor y carga útil, subsistemas, eyección, descenso en dos etapas, cargas en G, vocabulario de la PDR) están en un anexo al final. Cubre los requisitos S1–S9, M1–M4, C1–C4, C6–C8 y E3–E9 del Anexo A.

| Tema | Requisitos | Diapositivas PDR |
| --- | --- | --- |
| 2.1 Configuración general | C2, C3, C4, S7 | 6–8, 37 |
| 2.2 Materiales | S6, S9 | 38, 41 |
| 2.3 Dimensiones | S2, S3, S7 | 9, 14 |
| 2.4 Fijación | S8, M3, M4 | 39 |
| 2.5 Resistencia | S4, S5 | 76, 78 |
| 2.6 Masa y CG | S1 | 42–46 |
| 2.7 Accesos e integración | E3–E9, C6–C8 | 10–12, 40 |
| 2.9 Mecanismo de liberación | C4, M1–M3 | 40 |
| 2.8 Interfaz con el cohete | C1, C2 | 13, 14 |

Dependencias con otras áreas: el volumen y mecanismo de los paracaídas (descenso), la lista y masa de componentes (electrónica) y la ubicación de cámaras y panel solar (sensores/EPS).

### Resumen: propuestas iniciales y de qué dependen

| Tema | Propuesta inicial | Qué puede cambiarla |
| --- | --- | --- |
| 2.1 Configuración | B: cuerpo único con descenso en dos etapas | Que la organización exija separar carga útil y contenedor (la planilla de puntaje lo asume) |
| 2.2 Materiales | Tubo de ASA por FDM local; si la masa no cierra, ASA-LW poco espumado, PAHT-CF o PA12; PLA para prototipos | Stock de ASA en el taller y cotización real |
| 2.3 Dimensiones | 90 mm (0/−0,5) × ≈ 230 mm | Las medidas reales de la sección de carga del cohete |
| 2.4 Fijación | Bandeja perforada unida a la tapa inferior, insertos de latón M3, baterías con láminas soldadas | Cuántas placas y qué batería elija electrónica |
| 2.5 Resistencia | Cálculos manuales + ensayos de caída, vibración, térmico y tirón | Velocidad final de descenso; herramientas disponibles |
| 2.6 Masa | Estructura impresa en ASA ≈ 216 g (modelo 3D): quedan ≈ 285 g para el resto; plantilla de presupuesto y alojamiento para lastre | Los componentes reales de electrónica y descenso |
| 2.7 Accesos | Orificios de 8 mm, cámara a cenit en el borde superior, ventilación para el barómetro | Las cámaras y el panel solar elegidos |
| 2.8 Interfaz | Exterior liso y chaflanado; fit check con tubo de prueba | Datos del cohete y del sistema de eyección |
| 2.9 Mecanismo | Servo con pasador que libera el cordón del compartimento del segundo sistema | Qué libera exactamente (lo define descenso) y el servo elegido |

Las tres dudas que más pesan: **¿manda el Anexo A o la planilla?**, **¿cuánto mide la sección de carga del cohete?** y **¿qué componentes y masas eligen electrónica y descenso?**

## 2.1 Configuración física general

La primera decisión del proyecto es si el CanSat es **una sola pieza** o **dos piezas que se separan en vuelo**. Define el resto: dónde van los paracaídas, cuánta masa queda para electrónica y qué mecanismos hay que construir. Hay dos opciones viables; la propuesta inicial es la B, pero depende de una respuesta de la organización.

### Qué tiene que pasar mecánicamente

Independientemente de la opción, la secuencia de la misión exige:

- Sobrevivir al empuje y a la eyección dentro del fuselaje (S4, S5).
- Salir del cohete sin trabarse (S7) y abrir solo el paracaídas de primera etapa (C3).
- Detectar el 80% de la altitud máxima en la bajada y **cambiar de sistema de descenso** (C4). Esto implica un mecanismo actuado por la electrónica.
- Grabar ese cambio con la cámara a cenit y el suelo con la cámara a nadir (C6, C7).
- Aterrizar entero y ser localizable con la baliza (C8).

El punto 3 es el único mecanismo obligatorio, y hay restricciones sobre él: nada pirotécnico ni químico (M1), si usa calor debe estar encerrado (M2) y debe mantener su estado bajo cualquier carga (M3).

### Opción A: contenedor y carga útil separables

Es el esquema de CanSat USA. Por ejemplo, el equipo 1043 (CanSat USA 2026) separa la carga útil del contenedor al 80% del apogeo y la baja con un parapente ([PDR 1043](https://www.cansatcompetition.com/docs/teams/cansat2026_1043_pdr_v07.pdf)).

Ojo con el origen de esta opción: **ningún documento de la CONAE dice que la carga útil se separe del contenedor**. La idea viene de CanSat USA, cuyo requisito equivalente sí dice que al 80% del apogeo la carga útil se libera del contenedor. Nuestro C4 dice otra cosa: que el CanSat libera otro sistema de descenso. La plantilla PDR también viene de CanSat USA (habla de paracaídas del contenedor y parapente de la carga útil), y por eso sugiere la separación aunque nuestro Anexo no la pida.

La **planilla de puntaje (Scoresheet V2)** sí asume la separación, pero también está copiada de CanSat USA 2026 sin adaptar: pide la carga útil fuera del contenedor con todo desplegado, un trade de cómo se libera la carga útil del contenedor (2 estrategias), paracaídas del contenedor, parapente con dirección, ojiva, cáncamo sobre disco de madera y un huevo como instrumento. Varias de esas cosas (ojiva, huevo, cáncamo, parapente) no aparecen en nuestro Anexo A. Hay contradicción entre Anexo y planilla, y conviene preguntar cuál manda antes de elegir entre A y B.

- **Contenedor**: tubo exterior de 90 mm, con el paracaídas de 15 m/s fijado arriba.
- **Carga útil**: un cilindro más chico dentro del contenedor (≈ 84 mm exterior, ≈ 80 mm interior) con toda la electrónica, las cámaras, la baliza y su propio paracaídas de 5 m/s.
- **Separación**: al 80% de altitud un servo suelta una traba; la carga útil cae por el extremo inferior y su paracaídas sale por arrastre.
- El contenedor sigue bajando solo con el paracaídas de la etapa 1.

Variantes a discutir: ¿la carga útil sale por abajo (por gravedad) o por arriba (extraída por su paracaídas)? ¿El contenedor lleva algo de electrónica o es solo un tubo?

### Opción B: cuerpo único con descenso en dos etapas

Es el esquema de dual deploy de la cohetería. La carcasa exterior es a la vez contenedor y estructura de la carga útil; nada se separa.

- Un solo cilindro de 90 mm.
- Compartimento superior con el paracaídas de etapa 1 y, debajo o al lado, el principal plegado.
- Al 80% de altitud, un servo libera una traba o una tapa y sale el principal.
- Cámara a cenit en el borde de la tapa superior (en el centro vería el paracaídas plegado, ver 2.7); cámara a nadir en la tapa inferior.

Variantes a discutir:

- **B1**: el paracaídas de etapa 1 queda conectado y se suma el principal (más simple, pero hay que considerar que los dos aportan arrastre).
- **B2**: se suelta el de etapa 1 ("cutaway") y se abre solo el principal (más predecible en velocidad, pero un paracaídas cae suelto).
- **B3**: el principal sale junto con el de etapa 1 pero atado con un lazo que se corta al 80% ("reefing"; si se corta con hilo de nicrom tiene que estar encerrado por M2).

**[Figura pendiente]** Configuraciones A y B · lanzamiento y desde el 80%. En A el contenedor sigue cayendo con el paracaídas de etapa 1 y la carga útil baja aparte con el suyo; en B todo baja junto, primero con el paracaídas chico y después con el principal.

### Ojo: son dos decisiones distintas

A y B no se diferencian en "paracaídas vs. parapente". Hay dos preguntas independientes:

- **¿El CanSat se divide en dos cuerpos?** Sí → opción A. No → opción B.
- **¿Qué es el "otro sistema de descenso" de C4?** C4 no lo especifica: puede ser un segundo paracaídas, un parapente, un autogiro u otro. La planilla de puntaje (copiada de CanSat USA) espera un **parapente**.

|  | Segundo sistema: paracaídas | Segundo sistema: parapente |
| --- | --- | --- |
| **A: se separan** | La carga útil sale del contenedor y abre su paracaídas | Esquema de CanSat USA: la carga útil sale y despliega el parapente |
| **B: un solo cuerpo** | Dual deploy clásico (variantes B1–B3) | El cuerpo entero suelta el paracaídas de etapa 1 y despliega un parapente |

Cualquiera de las cuatro combinaciones cumple la letra de C4. La planilla favorece la columna del parapente y, sobre todo, la esquina A + parapente.

Sobre el **80%**: se mide en la **bajada**. La "altitud máxima" (apogeo) solo se conoce después de alcanzarla, y en el ascenso el CanSat todavía está dentro del cohete. Ejemplo: con apogeo de 600 m, el segundo sistema se activa al pasar por 480 m de bajada.

### Comparación

| Criterio | A: separables | B: cuerpo único |
| --- | --- | --- |
| Lectura de C2–C4 | Es el esquema de CanSat USA; nuestro Anexo no lo pide explícitamente | Coincide con la letra de C4: "el CanSat liberará otro sistema de descenso" |
| Masa de paredes | Dos tubos: ≈ 245 g en ASA | Un tubo: ≈ 136 g en ASA |
| Espacio interior | Diámetro útil ≈ 80 mm | Diámetro útil 86 mm |
| Eventos de riesgo | Separación, traba, extracción del paracaídas, líneas enredadas | Liberación del principal |
| Recuperación | Dos objetos en el campo; la baliza va en la carga útil | Un objeto con baliza |
| Interruptores E4/E5/E9 | Deben alinear orificios en dos paredes | Acceso directo |
| Cámaras C6/C7 | Ven la separación y el paracaídas de la carga útil | Ven la apertura del principal |
| Semejanza con CanSat USA (premio final) | Alta | Media |

La diferencia de masa es la más fuerte: con 500 g totales, las paredes de A se llevan casi la mitad antes de poner un solo componente.

### Matriz de decisión

Puntaje de 1 a 5 (5 = mejor), evaluación cualitativa para discutir en el equipo:

| Criterio | Peso | A: separables | B: cuerpo único |
| --- | --- | --- | --- |
| Masa disponible para el resto | 25% | 2 | 5 |
| Cumplimiento del Anexo (C2–C4) | 20% | 4 | 5 |
| Riesgo de falla (cantidad de eventos mecánicos) | 20% | 2 | 4 |
| Coincidencia con la planilla de puntaje | 15% | 5 | 3 |
| Volumen interior | 10% | 3 | 5 |
| Accesos y recuperación | 10% | 2 | 5 |
| **Total ponderado** | 100% | **2,95** | **4,50** |

B gana con claridad. La excepción: si la organización responde que la planilla manda y la separación es obligatoria, deja de ser un criterio con peso y pasa a ser un requisito, y A queda como única opción.

### Propuesta inicial para discutir

Arrancar con **B** como línea base y mantener **A** documentada como alternativa. Motivos: más margen de masa y volumen, menos eventos de riesgo, un solo objeto a recuperar y accesos más simples.

Lo que haría cambiar la decisión:

- Que la organización confirme que C4 exige separación física → pasamos a A.
- Que el equipo priorice parecerse a CanSat USA porque el premio es viajar a esa competencia.
- Que descenso proponga un parapente o un sistema que solo funcione separado.

### Preguntas para el equipo

- [ ] ¿Cómo leemos "contenedor" en el Anexo: pieza separable o carcasa?
- [ ] ¿Cuál variante de B preferimos (B1, B2, B3) según lo que investigue descenso?
- [ ] ¿Qué mecanismo de liberación queremos probar primero: servo con traba o corte de lazo encerrado?
- [ ] ¿Quién arma un prototipo rápido (tubo impreso + traba) para probar la liberación antes de la PDR?

## 2.2 Materiales y métodos de fabricación

Comparando solo por desempeño técnico, el mejor material para el cuerpo es **nylon PA12 impreso por fusión de polvo (MJF o SLS)**: es el más liviano con pared de 2 mm, igual de resistente en todas las direcciones, tenaz ante golpes y no se ablanda con el calor. Le sigue el **nylon con fibra de carbono (PAHT-CF) impreso por FDM**. Pero no hace falta el mejor: ASA impreso por FDM en un taller local cumple con margen y es la propuesta inicial; el nylon queda como opción si la masa no cierra.

### Qué piden los requisitos

- **S6**: "El grosor de la pared del exterior debe ser de al menos 2 mm **cuando se imprima en 3D** y no debe flexionarse ni deformarse bajo tensión."
- **S9**: "Los materiales del contenedor del CanSat no deberán ser contaminantes ni perjudiciales para el ambiente."
- Indirectamente: S4/S5 (15 G y 30 G), S1 (masa) y S7 (deslizar libre: precisión de medidas).

### Criterios de comparación, en orden de importancia

- **Masa con pared de 2 mm (densidad)**: después del tubo quedan ≈ 360 g para todo lo demás (2.6). Cada 0,1 g/cm³ de densidad son ≈ 13 g en el tubo.
- **Resistencia al impacto y entre capas**: el choque de 30 G y el aterrizaje (2.5).
- **Resistencia al calor (HDT)**: sol en la rampa, auto, ensayo térmico a 60 °C.
- **Rigidez (módulo)**: "no flexionarse" (S6). Con 2 mm de pared y forma de tubo, cualquier plástico de esta lista es suficientemente rígido; pesa menos que los otros criterios.
- **Precisión dimensional**: 90 mm con tolerancia de 0,5 mm.
- **Transparencia a la radio**: el tubo no puede bloquear radio ni GPS.

### Conceptos para leer las tablas

- **Tracción (MPa)**: tensión que aguanta antes de romperse.
- **Módulo (MPa)**: rigidez.
- **Impacto (kJ/m²)**: energía que absorbe antes de quebrarse de golpe.
- **HDT (°C)**: temperatura a la que se ablanda bajo carga.
- **Anisotropía**: en la impresión por filamento (FDM) la pieza es más débil **entre capas** (eje Z). Un tubo impreso parado tiene las capas como anillos: un golpe o una flexión tiende a separarlas. En la fusión de polvo (MJF/SLS) las capas se funden entre sí y la pieza es casi igual de resistente en todas direcciones.

### Métodos de fabricación

| Método | Cómo funciona | Fortaleza | Debilidad |
| --- | --- | --- | --- |
| FDM (filamento) | Una boquilla deposita plástico fundido capa por capa | Muchos materiales; piezas grandes | Débil entre capas; precisión ± 0,2–0,3 mm |
| MJF / SLS (fusión de polvo) | Un láser o un agente térmico funde capas de polvo de nylon | Casi isótropo; tenaz; precisión ≈ ± 0,3 mm; sin soportes | Pocos materiales (PA12, PA11); superficie algo porosa |
| SLA (resina) | Un láser cura resina líquida | Muy preciso y liso | Frágil ante golpes; se degrada al sol |
| Tubo comercial | Tubo de fábrica, se corta y perfora | Pared continua y pareja | Diámetro exacto difícil; orificios y encastres a mano |

### Materiales impresos: comparación

Valores de hojas de datos de fabricantes (FDM: [guía Bambu Lab](https://cdn1.bambulab.com/filament/a5e185aed14e6/filament-guide-en-4.pdf), [PAHT-CF](https://cdn.shopify.com/s/files/1/0380/5149/files/Bambu_PAHT-CF_Technical_Data_Sheet.pdf); MJF: [Protolabs PA12](https://www.protolabs.com/media/1010893/2019-mjf-datasheet-pa-12-black.pdf)). Los ensayos de distintos fabricantes no son idénticos: sirven para ordenar, no para comparar decimales. Masa del tubo 90/86 × 230 mm (≈ 127 cm³).

| Material | Qué es | Método | Densidad (g/cm³) | Masa tubo (g) | Tracción X-Y / Z (MPa) | Impacto X-Y (kJ/m²) | HDT (°C) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PA12 | Nylon 12 (poliamida) en polvo, fundido capa por capa; plástico técnico tenaz | MJF | 1,01 | ≈ 128 | 49 / 47 | Tenaz (12% alargamiento) | 175 |
| PAHT-CF | Nylon de alta temperatura con fibra de carbono corta, en filamento | FDM | 1,06 | ≈ 135 | 88 / 64 | 57,5 | 194 |
| ASA | Acrilonitrilo estireno acrilato: pariente del ABS, pensado para exteriores (resiste el sol) | FDM | 1,05–1,13 | ≈ 133–144 | 37 / 31 | 41,0 | 100 |
| ABS | Acrilonitrilo butadieno estireno: el plástico de los bloques Lego; tenaz y aguanta calor, pero se amarillenta al sol | FDM | ≈ 1,05 | ≈ 133 | — | 39,3 | 87 |
| PETG-CF | PETG con fibra de carbono corta mezclada | FDM | 1,25 | ≈ 159 | 59 / 38 | 41,2 | 74 |
| PETG | Poliéster (el PET de las botellas) modificado con glicol para poder imprimirlo | FDM | ≈ 1,27 | ≈ 161 | — | 52,7 | 69 |
| PLA | Ácido poliláctico, de origen vegetal (maíz o caña); el filamento más común y fácil | FDM | 1,24 | ≈ 158 | 39 / 35 | 26,6 | 57 |
| PLA-CF | PLA con fibra de carbono corta mezclada | FDM | 1,22 | ≈ 155 | 38 / 26 | 23,2 | 55 |

### Ranking para el tubo exterior

- **PA12 por MJF/SLS.** El más liviano (≈ 30 g menos que PETG), casi igual de resistente en Z que en X-Y (47 vs. 49 MPa), tenaz, aguanta 175 °C y absorbe poca humedad. Su módulo (1.900 MPa) es menor que el del PLA, pero un tubo de 2 mm no flexiona con estas cargas (2.5). Variante: **PA11**, aún más dúctil ante golpes, con densidad parecida.
- **PAHT-CF por FDM.** El más fuerte y rígido, casi tan liviano y con la mayor resistencia al calor. Pierde contra el PA12 porque entre capas sigue siendo más débil (impacto en Z de 13,3 kJ/m², igual que el PLA) y porque absorbe humedad: hay que secarlo a 80 °C antes de imprimir.
- **ASA / ABS por FDM.** Livianos y resistentes al calor, con impacto moderado. Alternativa sólida si el nylon no conviene por otro motivo.
- **PETG / PETG-CF.** Buen impacto, pero ≈ 25 g más pesados que el nylon y se ablandan a 70 °C.
- **PLA / PLA-CF.** Los menos recomendables para vuelo: frágiles y se ablandan a 55 °C (un auto al sol los deforma).

### ¿Hace falta el mejor material? Lo que alcanza

No. El ranking dice cuál es el mejor, pero las cargas de esta misión son chicas: el tubo trabaja a menos del 1% de su resistencia (2.5, cálculo 1). La altura del vuelo casi no influye; las cargas vienen de la eyección, la apertura del paracaídas y el aterrizaje, que son iguales a 500 m que a 1.000 m.

Lo que el PA12 aporta de verdad sobre un buen filamento son **≈ 8 g menos que ASA** (≈ 30 g menos que PETG) y la ausencia de debilidad entre capas. Ninguna de las dos cosas es necesaria para cumplir los requisitos.

| Nivel | Material | Masa tubo | Cumple S4, S5, S6 | Comentario |
| --- | --- | --- | --- | --- |
| Suficiente | PETG por FDM | ≈ 161 g | Sí, con margen | Barato y fácil; pesa ≈ 25 g más que ASA (quedan ≈ 340 g para el resto) |
| Recomendado | ASA por FDM | ≈ 136 g | Sí, con margen | Liviano, aguanta 100 °C y golpes; se imprime en talleres locales |
| Mejor si sobra presupuesto | PAHT-CF por FDM o PA12 por MJF | ≈ 128–135 g | Sí, con mucho margen | Solo vale la pena si la masa queda muy ajustada |

Por eso el PA12 importado queda como **opción, no como necesidad**. Se justifica solo si al final la masa no cierra o si el costo resulta bajo al cotizarlo.

#### Matriz de decisión para el tubo

Se separan los criterios técnicos de los prácticos, para ver cómo cambia la elección según cuánto pese cada grupo. Puntaje de 1 a 5 (5 = mejor):

| Criterio | Peso dentro del grupo | PA12 (MJF) | PAHT-CF | ASA | ASA-LW poco espumado | PETG |
| --- | --- | --- | --- | --- | --- | --- |
| Masa del tubo | 30% técnico | 5 | 4 | 4 | 5 | 2 |
| Impacto y resistencia entre capas | 30% técnico | 5 | 4 | 3 | 2 | 4 |
| Resistencia al calor | 20% técnico | 5 | 5 | 4 | 3 | 2 |
| Precisión y repetibilidad | 20% técnico | 4 | 3 | 3 | 2 | 3 |
| **Subtotal técnico** |  | **4,80** | **4,00** | **3,50** | **3,10** | **2,80** |
| Disponibilidad local y plazo | 50% práctico | 2 | 3 | 4 | 3 | 5 |
| Costo | 50% práctico | 3 | 3 | 5 | 4 | 5 |
| **Subtotal práctico** |  | **2,50** | **3,00** | **4,50** | **3,50** | **5,00** |
| **Total (70% técnico + 30% práctico)** |  | **4,11** | **3,70** | **3,80** | **3,22** | **3,46** |

Lectura honesta: **por desempeño técnico gana PA12**, y con un 30% de peso práctico sigue ganando. ASA pasa adelante si lo práctico pesa un 40% o más. La propuesta de ASA se apoya en que el margen técnico sobra (2.5): la diferencia de PA12 son ≈ 8 g y una resistencia que no se necesita. Si la cotización de PA12 resulta baja y el plazo entra en el cronograma, pasar a PA12 es una mejora razonable.

Para **piezas internas** (placa de montaje, soportes, cunas) alcanza con **ASA**, el mismo material del tubo: las cargas son chicas (una batería a 30 G empuja ≈ 14 N), los insertos de latón funcionan bien y un solo material simplifica el pedido y el presupuesto de masa. Dos excepciones:

- **Anclaje del paracaídas y traba del mecanismo**: son las piezas más exigidas (≈ 100 N en un punto chico, y M3 pide que la traba no se abra sola). En ASA se pueden hacer con más espesor y bien orientadas; en PAHT-CF, o con un cáncamo o pieza metálica atornillada, el margen es mucho mayor.
- **Placa de montaje grande y fina**: ASA es menos rígido que PLA-CF; se compensa con 3 mm de espesor o nervaduras, sin cambiar de material.

Para **prototipos y pruebas de encaje** el criterio es otro (rapidez y bajo costo): ahí PLA es suficiente, porque no vuela.

**¿Y el PLA con fibra de carbono?** Son fibras cortas mezcladas en PLA, no un compuesto como el de un cuadro de bicicleta. Es ≈ 35% más rígido, pero no más resistente: entre capas baja de 35 a 26 MPa y se vuelve más quebradizo, así que no conviene para el tubo ([PLA](https://cdn.shopify.com/s/files/1/0380/5149/files/Bambu_PLA_Basic_Technical_Data_Sheet.pdf) vs. [PLA-CF](https://cdn.shopify.com/s/files/1/0380/5149/files/Bambu_PLA-CF_Technical_Data_Sheet.pdf)). La fibra corta sí rinde en nylon (PAHT-CF).

### Lo que usó el equipo 1043 y cuándo conviene

El equipo 1043 de CanSat USA hizo casi todas sus piezas en **ASA-LW** (ASA espumado) y solo el gancho de liberación, la pieza más exigida, en **PPA-CF** (nylon de alto rendimiento con fibra de carbono) ([PDR 1043](https://www.cansatcompetition.com/docs/teams/cansat2026_1043_pdr_v07.pdf)). Es la misma lógica de nuestra propuesta: un material general liviano y uno muy fuerte solo donde hace falta.

**ASA-LW.** Es ASA con un agente que hace espuma al imprimirse. La densidad la controla la temperatura de impresión: cuanto más caliente, más espuma, más liviano y más débil.

| Punto | Densidad (g/cm³) | Tracción X-Y / Z (MPa) | Masa del tubo | Fuente |
| --- | --- | --- | --- | --- |
| ASA común | 1,05 | 37 / 31 | ≈ 133 g | [Bambu ASA](https://polyalkemi.no/wp-content/uploads/2024/01/Bambu_ASA_Technical_Data_Sheet.pdf) |
| ASA-LW poco espumado (225 °C) | 0,99 | 32 / 21 | ≈ 126 g | [Bambu ASA Aero](https://cdn.shopify.com/s/files/1/0584/7236/6216/files/Bambu_ASA_Aero_Technical_Data_Sheet.pdf) |
| ASA-LW muy espumado (lo que usó el 1043) | 0,6 | 9 | ≈ 76 g | PDR 1043 |

- **Conviene** en piezas internas poco cargadas (carcasas de cámaras, soportes livianos, tapas sin anclaje), donde ahorra masa casi sin riesgo.
- **Conviene en el tubo solo poco espumado y solo si la masa no cierra**: ahorra ≈ 10 g y conserva margen de sobra para 30 G (0,27 MPa de carga contra 21 MPa de resistencia). Es una alternativa local y barata antes de importar PA12.
- **No conviene** en el tubo muy espumado: con 9 MPa y menos de la mitad de rigidez es dudoso que cumpla "no flexionarse ni deformarse" (S6), y el impacto entre capas es muy bajo.
- **No conviene** donde van insertos o tornillos, ni en el anclaje del paracaídas o la traba: el material espumado agarra mal las roscas.
- Ojo práctico: la densidad final depende de cómo configure el taller la impresión; hay que pedirla por escrito y pesar la pieza al recibirla.

**PPA-CF.** Según el PDR del 1043: densidad 1,25 g/cm³, resistencia 168 MPa y módulo 9.860 MPa, varias veces más fuerte que cualquier otra opción de la tabla.

- **Conviene** en piezas chicas muy exigidas: gancho, traba del mecanismo, anclaje del paracaídas. Son pocos gramos, así que su precio casi no pesa.
- **No conviene** en piezas grandes: es más pesado, caro, y exige boquilla endurecida, secado e impresora cerrada.
- Cumple el mismo rol que en nuestra propuesta damos al PAHT-CF o a una pieza metálica.

### Tubos comerciales

| Opción | Densidad (g/cm³) | Masa aprox. (230 mm) | Evaluación técnica |
| --- | --- | --- | --- |
| Fibra de vidrio, pared 1 mm | ≈ 1,9 | ≈ 120 g | Comparable al PA12 en masa y más resistente; deja pasar la radio. Pero el diámetro exacto y los encastres internos son difíciles de lograr |
| Fibra de carbono, pared 1 mm | ≈ 1,55 | ≈ 100 g | El más liviano y rígido, pero **bloquea radio y GPS**: descartado para el cuerpo |
| Aluminio, pared 1 mm | 2,7 | ≈ 175 g | Muy resistente, pero **bloquea radio y GPS** y es pesado: descartado |
| PVC de 90 mm | ≈ 1,4 | ≈ 175 g (pared 2 mm) | Pesado; diámetro real puede superar 90 mm; contiene cloro (discutible con S9) |
| Cartón o tubo de cohetería | ≈ 0,7–1,3 | ≈ 50–100 g | Muy liviano, pero se daña con humedad y golpes |

El descarte de carbono y aluminio es técnico: un tubo conductor funciona como jaula de Faraday y aísla las antenas. La fibra de vidrio es la única alternativa comercial competitiva, con la desventaja de tener que mecanizar a mano ventanas, orificios y encastres, que en una pieza impresa salen hechos.

**Conclusión: conviene imprimir el tubo.** La impresión da el diámetro exacto que dibujemos, integra de una vez orificios, ventanas, rebajes y alojamientos para insertos, pesa menos que PVC o aluminio y no bloquea la radio. La ventaja del tubo comercial (pared continua, sin debilidad entre capas) no pesa porque la resistencia sobra (2.5). Solo un tubo de fibra de vidrio de exactamente 90 mm con tapas impresas podría competir, pero suma trabajo sin resolver un problema que tengamos.

### S9: cómo justificar que no es contaminante

Termoplásticos estables, sin piezas que se desprendan, y el CanSat completo se recupera tras el vuelo. Evitar plomo (lastre) y PVC si se quiere evitar la discusión por el cloro.

### Propuesta inicial para discutir

- **Tubo y tapas de vuelo**: ASA por FDM en un taller local.
- **Placa de montaje y piezas internas**: ASA por defecto; PAHT-CF o metal en el anclaje del paracaídas y la traba del mecanismo.
- **Si la masa no cierra**: pasar el tubo a ASA-LW poco espumado (local, ≈ 10 g menos), PAHT-CF (local) o PA12 por MJF (importado); ASA-LW también en piezas internas poco cargadas.
- **Prototipos**: PLA.

### Dónde imprimir y precios

**Conclusión: es viable y barato.** El ASA se imprime en talleres argentinos con envío al interior, y el juego completo de piezas de vuelo cuesta del orden de $30.000–70.000, menos del 10% del límite de C9 ($1.000.000). El PA12 por MJF solo se consigue afuera y queda como opción.

#### Precio de los filamentos en Argentina

Precio de venta al público por kilo, relevado entre octubre y noviembre de 2026. Es lo que paga el taller por el material, no el precio de una pieza impresa.

| Material | Rango por kg (ARS) | Fuentes |
| --- | --- | --- |
| PLA | $18.000–28.000 | [War Record](https://www.warrecord.net/blogs/noticias/cuanto-cuesta-imprimir-en-3d-en-argentina-en-2026), [Printalot](https://printalot.com.ar/productos/filamentos/pet-g/petg-1-75-mm-1-kg/) |
| PETG | $18.000–26.000 | [Printalot](https://printalot.com.ar/productos/filamentos/pet-g/petg-1-75-mm-1-kg/) ($17.935), [Grilon3 en Sistemas Junín](https://sistemasjunin.com.ar/product/filamento-petg-grilon3-blanco-1kg/) ($19.490), War Record |
| ABS | $19.000–30.000 | Printalot ($19.465), War Record |
| **ASA** | **$22.000–42.000** | [Elegoo en impresoras3d.com.ar](https://impresoras3d.com.ar/productos/filamento-elegoo-asa-1-75mm-1kg-negro/) ($21.960), [Elegoo en Defra](https://defrastore.com.ar/productos/filamento-3d-elegoo-asa-x-1kg/) ($31.500), War Record ($32.000–42.000) |
| Nylon | $55.000–80.000 | War Record |
| Nylon con fibra de carbono (PA-CF) | $90.000–175.000 | War Record, [Sunlu PA12-CF en Filatek](https://www.filatek.com.ar/productos/filamento-sunlu-pa12-cf-x1kg-nylon-12fibra-de-carbono-xcvio) ($175.000) |

Dato a tener en cuenta: las dos tiendas que publicaban ASA Elegoo figuraban **sin stock**. El ASA es menos común que el PLA o el PETG, así que conviene confirmar con el taller que lo tenga antes de diseñar todo alrededor de él. Si no lo hay, el reemplazo directo es ABS (propiedades parecidas, algo menos resistente al sol).

#### Cuánto costaría nuestro juego de piezas en ASA

Estimación propia, a confirmar con cotización:

| Concepto | Cantidad | Costo aprox. (ARS) |
| --- | --- | --- |
| Material (tubo, tapas, placa y soportes: ≈ 210 g + 20% de desperdicio) | ≈ 250 g | $5.500–10.500 |
| Horas de impresora profesional ($1.500–2.500/h según War Record) | ≈ 16–23 h | $24.000–58.000 |
| **Total por juego** |  | **≈ $30.000–70.000** |

Conviene pedir dos juegos (vuelo y repuesto), más uno o dos prototipos en PLA. El total del proyecto en estructura quedaría del orden de $100.000–200.000.

#### Proveedores relevados

| Proveedor | Tecnología y materiales | Envío |
| --- | --- | --- |
| [Printonic](https://printonic.com.ar/) (CABA) | FDM: ASA, PETG, ABS, nylon, fibra de carbono, PC; cotizador online y respuesta en 48 h hábiles | Todo el país por Andreani |
| [Trideo](https://www.trideo3d.com/en/buenos-aires) (Buenos Aires) | FDM: ABS, PETG, nylon CF, PC/ABS, Ultem; resina DLP; cotización online subiendo el STL | Nacional |
| [Hornero 3DX](https://hornero3dx.com/productos/impresoras-3d/formlabs-fuse/) (CABA) | Vende SLS Formlabs Fuse y ofrece impresión en su fábrica; hay que preguntar si incluye SLS | A consultar |
| [JLC3DP](https://jlc3dp.com/es/help/article/PA12-HP-Nylon) (exterior) | MJF PA12/PA11, tolerancia ± 0,3 mm, ≈ 72 h de producción | Courier internacional; franquicia de USD 400 con solo IVA ([detalle](https://www.derechoenzapatillas.com/2026/envios-postales-franquicia-400-dolares-correo-courier/), a confirmar en ARCA) |

También conviene preguntar en talleres de Posadas o la región: ahorran el envío y permiten ir a medir las piezas.

#### Qué pedirle al taller

Una pieza impresa varía mucho según cómo se configura la impresión. Para que cumpla lo que calculamos, el pedido tiene que especificar:

- **Material y marca**, y que el ASA o ABS se imprima en **impresora cerrada** (sin cerramiento se deforma).
- **Tubo impreso parado** (eje vertical), para que salga redondo y sin soportes.
- **Pared maciza**: perímetros suficientes para los 2 mm (5 con boquilla de 0,4 mm).
- **Altura de capa** de 0,2 mm o menos.
- **Diámetro exterior verificado con calibre** antes de despachar; tolerancia pedida 89,5–90,0 mm.
- Para la placa y los soportes: relleno de al menos 40% y 4 perímetros alrededor de los agujeros de insertos.

#### Cómo encaja con el desarrollo

- **Prototipos**: PLA por FDM, para iterar rápido.
- **Piezas de vuelo**: ASA por FDM en un taller local, con un juego de repuesto.
- **Solo si hace falta bajar masa**: ASA-LW poco espumado o PAHT-CF locales, o un pedido único de PA12 por MJF cuando el diseño esté congelado (CDR).

#### Pendiente

- [ ] Pedir cotización del juego en ASA a Printonic y Trideo, y a algún taller de Posadas.
- [ ] Confirmar que el taller tenga ASA en stock (o aceptar ABS).
- [ ] Opcional: cotizar el tubo en PA12 en JLC3DP con envío a Posadas, para comparar.

### Preguntas para el equipo

- [ ] ¿Quién pide las cotizaciones en ASA (Printonic, Trideo, talleres de Posadas)?
- [ ] ¿Imprimimos primero un tramo corto de tubo para verificar el diámetro real que entrega el proveedor?

## 2.3 Dimensiones y volumen

Las medidas exteriores están casi fijadas por el Anexo, pero hay una contradicción con las Bases y un rango de largo para decidir. La propuesta inicial es **90 mm de diámetro y unos 230 mm de largo**, a confirmar cuando conozcamos el cohete.

### Qué dicen los requisitos

| Fuente | Qué dice | Cómo lo leemos |
| --- | --- | --- |
| Bases §4 | Cilindro de 95 mm de diámetro y 200 mm de largo | Probablemente el espacio disponible en el cohete (TBR) |
| S2 | Diámetro del CanSat: 90 mm | Diámetro exterior máximo de nuestra pieza |
| S3 | Largo total de 200 a 250 mm, incluidos los sistemas de descenso | Los paracaídas plegados van dentro de ese largo |
| S6 | Pared de al menos 2 mm si es impresa | Diámetro interior máximo 86 mm |
| S7 | Debe deslizar libremente fuera del cohete | Necesitamos holgura y bordes sin aristas |

Si los 95 mm son el tubo del cohete, quedan 5 mm de juego diametral (2,5 mm por lado). Como referencia, el equipo 1043 de CanSat USA declaró holguras de 3 y 5 mm en su diapositiva de compatibilidad ([PDR 1043](https://www.cansatcompetition.com/docs/teams/cansat2026_1043_pdr_v07.pdf)).

**[Figura pendiente]** Vista lateral con cotas · mm.

### Cuánto se aparta una pieza impresa de su medida

- Una impresora FDM típica tiene un error de ±0,2–0,3 mm en diámetro.
- La primera capa suele salir ensanchada ("pata de elefante"), justo en el borde que entra primero al tubo.
- Los termoplásticos sin carga como el ASA se dilatan del orden de 70–100 × 10⁻⁶ por °C (valor típico: las hojas de datos de filamento ASA no lo informan): con 30 °C más (sol en la rampa), 90 mm crecen ≈ 0,2–0,3 mm.

Por eso conviene especificar **90 mm con tolerancia 0/−0,5 mm** (nunca más de 90) y **chaflanar los extremos**. Hay que imprimir una pieza de prueba y medirla con calibre para conocer el error real del taller que imprima.

### Opciones de largo

| Largo | A favor | En contra |
| --- | --- | --- |
| 200 mm (mínimo) | Menos masa de pared | Menos lugar para paracaídas; cualquier error lo deja fuera de S3 |
| ≈ 230 mm (intermedio) | Margen hacia ambos límites; se puede recortar | Habrá que confirmar que entra en la sección del cohete |
| 250 mm (máximo) | Máximo volumen | Más masa; un error por exceso lo deja fuera de S3 |

### Cálculo del volumen interior

El volumen de un cilindro es el área de la base por el largo. Con 86 mm de diámetro interior el área es π × 43² ≈ 5.810 mm² = 58,1 cm².

| Largo total | Volumen interior bruto |
| --- | --- |
| 200 mm | ≈ 1.160 cm³ |
| 230 mm | ≈ 1.340 cm³ |
| 250 mm | ≈ 1.450 cm³ |

Al bruto hay que restarle tapas, placas de montaje y los paracaídas plegados. Ese reparto se arma con descenso y electrónica.

### Cuánto pesa solo la pared

El material de la pared es la corona entre 90 y 86 mm: π × (45² − 43²) ≈ 553 mm². Por 230 mm de largo da ≈ 127 cm³. En PLA (≈ 1,24 g/cm³) o PETG (≈ 1,27 g/cm³) macizos son **≈ 155–160 g**, casi un tercio de los 500 g; en ASA (≈ 1,05–1,13 g/cm³), el material propuesto, es ≈ 136 g; en PA12 (1,01 g/cm³), ≈ 128 g. Esto conecta directamente con 2.2 (la pared de 2 mm queda maciza, así que solo la densidad del material cambia esta masa) y 2.6 (masa).

### Preguntas para el equipo

- [ ] ¿Pedimos ya al taller un tramo corto de tubo para medir su precisión real?
- [ ] ¿Qué volumen estiman descenso para los dos paracaídas plegados?
- [ ] ¿Nos quedamos con 230 mm hasta que la organización nos dé las medidas de la sección de carga del cohete (diámetro interior y largo útil), o preferimos otro valor?

## 2.4 Fijación de componentes

Todo lo que va adentro tiene que quedar **atornillado o pegado, nunca suelto ni apoyado**, porque con 15 G de vibración y 30 G de choque cualquier pieza libre se mueve, golpea o se desconecta. La opción recomendada es una **bandeja perforada a lo largo del tubo, unida a la tapa inferior**; abajo se explica por qué y cuáles son las alternativas.

### Qué piden los requisitos

- **S8**: "Todos los componentes electrónicos y mecánicos deben estar montados de forma fija utilizando soportes adecuados, tales como separadores, tornillos o adhesivos de alto rendimiento."
- **M4**: "No se deben utilizar contactos de resorte para realizar conexiones eléctricas a las baterías. Las fuerzas de choque pueden provocar desconexiones momentáneas."
- **M3**: los mecanismos deben mantener su estado bajo cualquier carga (una traba no puede abrirse sola por un golpe).

### Qué es una placa perforada

Es una **pieza plana con agujeros repetidos en una grilla regular**, por ejemplo uno cada 10 mm en filas y columnas. Funciona como los tableros perforados de garaje donde se cuelgan herramientas: no hace falta decidir de antemano dónde va cada cosa, porque hay agujeros en todos lados. Un ejemplo comercial es la [grilla de montaje de Adafruit](https://www.adafruit.com/products/5774), una placa de aluminio con agujeros en grilla para atornillar plaquetas; la nuestra sería la misma idea, impresa en ASA.

No confundir con la **placa perforada de electrónica** (perfboard), la plaqueta con agujeros cada 2,54 mm donde se sueldan componentes para armar un circuito. Esa es parte del circuito, no de la estructura; puede ir atornillada encima de la nuestra.

### Opción recomendada: bandeja perforada unida a la tapa inferior

Una placa de ASA de ≈ 80 mm de ancho, 3 mm de espesor y ≈ 150 mm de largo, con agujeros de 3,2 mm (para tornillos M3) cada 10 mm. Va parada a lo largo del tubo, por el centro, atornillada a la tapa inferior: **tapa y bandeja forman un solo conjunto que entra y sale del tubo por abajo**.

**[Figura pendiente]** Bandeja perforada dentro del CanSat · esquema sin escala. El conjunto resaltado (bandeja y tapa inferior) sale entero por abajo; la parte superior con los paracaídas queda cerrada. La ubicación de los componentes es orientativa hasta tener la selección de electrónica.

Por qué es la mejor para nosotros:

- **Se arma y se prueba fuera del tubo**, con la electrónica a la vista y acceso a las dos caras.
- **Se cambian baterías sin tocar los paracaídas**: se saca la tapa inferior con la bandeja y la parte superior no se abre (2.7).
- **El peso queda abajo**: la batería en la parte baja de la bandeja baja el centro de gravedad, que es lo que conviene colgado del paracaídas (2.6).
- **Tolera cambios**: aunque los componentes estén elegidos en la PDR, entre la PDR y la CDR es normal que alguno cambie (un sensor que falla en una prueba, una cámara que no se consigue). Con la grilla se mueven tornillos en vez de reimprimir.
- **Liviana**: ≈ 35 g en ASA maciza según el modelo 3D preliminar (2.6), menos con relleno parcial.

Detalle a resolver: la bandeja tiene que quedar trabada también en su extremo superior (una ranura o un tope en el compartimento) para que no vibre como un trampolín. Además, el servo del mecanismo queda en la parte superior: su cable necesita un conector que se desenchufe al sacar la bandeja.

Para la PDR hay que mostrar el layout con los **componentes reales** que elija electrónica, ubicados sobre la bandeja con sus dimensiones. Para eso hace falta la lista de modelo, dimensiones, masa y forma de fijación de cada uno.

### Alternativas

**Discos apilados con varillas roscadas.** Dos o tres varillas M3 a lo largo del tubo, con discos horizontales (pisos) sostenidos por tuercas; cada piso lleva un grupo de componentes. Es muy firme y la altura de cada piso se ajusta fácil, pero cuesta acceder a los pisos del medio, los cables tienen que pasar entre pisos y con varillas de acero suma ≈ 50–65 g. Conviene si electrónica divide el circuito en varias placas redondas de ≈ 80 mm.

**Esqueleto impreso a medida.** Una sola pieza con un hueco justo para cada componente. Es la más liviana (≈ 20 g) y compacta, pero cualquier cambio obliga a rediseñar y reimprimir. Conviene como **evolución de la bandeja en la CDR**, cuando los componentes estén confirmados y se quiera ganar masa o espacio.

|  | Bandeja perforada | Discos con varillas | Esqueleto a medida |
| --- | --- | --- | --- |
| Masa aprox. | ≈ 35 g (modelo 3D) | ≈ 50–65 g | ≈ 20 g |
| Acceso a componentes | Muy bueno, dos caras | Regular, por pisos | Bueno |
| Tolerancia a cambios | Alta | Media | Baja |
| Cambio de batería sin tocar paracaídas | Sí, sale con la tapa inferior | Posible, más trabajo | Depende del diseño |
| Mejor para | PDR y prototipos | Placas redondas apiladas | Diseño final (CDR) |

#### Matriz de decisión

| Criterio | Peso | Bandeja perforada | Discos con varillas | Esqueleto a medida |
| --- | --- | --- | --- | --- |
| Tolerancia a cambios de componentes | 25% | 5 | 3 | 1 |
| Acceso a componentes | 20% | 5 | 2 | 4 |
| Masa | 20% | 4 | 2 | 5 |
| Rigidez ante vibración | 20% | 3 | 5 | 4 |
| Cambio de batería sin tocar paracaídas | 15% | 5 | 3 | 3 |
| **Total ponderado** | 100% | **4,40** | **3,00** | **3,30** |

Puntaje de 1 a 5, evaluación cualitativa. La bandeja gana mientras los componentes puedan cambiar; en la CDR, con el diseño congelado, la tolerancia a cambios pierde peso y el esqueleto a medida se vuelve competitivo por masa.

### Formas de fijar, de mejor a peor para nuestro caso

- **Tornillos con insertos roscados de latón** (heat-set): se calientan con el soldador y se hunden en el plástico. En un ensayo con M3 en PETG, aguantaron ≈ 3 veces más torque que roscar directo en el plástico, con igual resistencia al arranque (≈ 120 kg) ([CNC Kitchen](https://www.cnckitchen.com/blog/helicoils-threaded-insets-and-embedded-nuts-in-3d-prints-strength-amp-strength-assessment)). Ideales para lo que se arma y desarma muchas veces.
- **Tuercas embutidas** en un alojamiento impreso: más baratas, igual de firmes si la tuerca queda empujada contra la pieza.
- **Rosca directa en el plástico**: aguanta el arranque, pero se gasta tras varios montajes. Solo para piezas que no se desarman.
- **Separadores (standoffs)** de nylon o latón M3/M2.5 para levantar las placas de circuito: separan la placa de la estructura y dejan pasar cables.
- **Antiaflojado**: tuercas autofrenantes (con anillo de nylon) o arandelas de presión. El líquido fijador de roscas (tipo Loctite) solo en uniones metal-metal: puede atacar y agrietar algunos plásticos.
- **Adhesivos**: epóxi para uniones permanentes; cinta doble faz de espuma (tipo VHB) para módulos chicos. El cianoacrilato ("La Gotita") es quebradizo ante golpes, y la **cola caliente se ablanda cerca de 60 °C**, justo la temperatura del ensayo térmico de CanSat USA.

### Baterías (M4)

La mayoría de los portapilas de 18650 tienen **resortes**, así que M4 los prohibe. Opciones:

- Celdas con **láminas soldadas de fábrica** ("tabs") y cables soldados a esas láminas. Nunca soldar directo sobre el cuerpo de la celda.
- Pack armado con **soldadura por puntos** (lo hacen casas de baterías).
- La celda se sujeta en una cuna impresa con precintos o una correa, para que no se deslice con el choque.
- Para la baliza (E8, batería independiente), lo mismo: pila de botón en portapila con traba, o pila con láminas soldadas.

La elección de batería la hace electrónica; a mecánica le toca la cuna y la sujeción.

### Cables y conectores

Los conectores sueltos son la falla más común en vibración. Preferir conectores con traba (JST-PH, JST-GH), fijar cada mazo con precintos a la estructura y, donde no haya traba, una gota de silicona o cola sobre el conector. Lo que no se desconecta nunca, soldado.

### Cómo se cierra el tubo

Las tapas superior e inferior se atornillan al tubo **en forma radial** (tornillos que atraviesan la pared hacia un inserto en la tapa). Los tornillos deben ser de **cabeza fresada** o quedar hundidos para no sobresalir del diámetro de 90 mm (S7).

### Propuesta inicial para discutir

- Bandeja perforada de ASA unida a la tapa inferior, con separadores M3 para las placas de circuito.
- Insertos de latón M3 en todo lo que se desarma (tapas, placa); tuercas embutidas donde no haya espacio.
- Baterías con láminas soldadas, en cuna impresa con precintos.
- Tapas con tornillos radiales de cabeza fresada.

### Preguntas para el equipo

- [ ] ¿Confirmamos la bandeja perforada, o electrónica prefiere placas redondas apiladas (discos con varillas)?
- [ ] ¿Qué batería elige electrónica, y viene con láminas soldadas?
- [ ] ¿Conseguimos insertos de latón M3 y una punta de soldador para colocarlos?

## 2.5 Resistencia estructural

Los cálculos muestran que **el tubo en sí aguanta con mucho margen**; lo que realmente falla en un CanSat son las uniones: tapas que se despegan entre capas, conectores que se sueltan, baterías que se corren y el anclaje del paracaídas. Por eso el análisis se apoya en cálculos simples y, sobre todo, en ensayos.

### Qué piden los requisitos

- **S4**: "La estructura del CanSat debe soportar vibraciones de 15 Gs."
- **S5**: "El CanSat debe soportar un impacto de choque de 30 Gs."
- **S6**: la pared "no debe flexionarse ni deformarse bajo tensión".

No dicen cómo verificarlo. CanSat USA, de donde vienen, define ensayos concretos que podemos adoptar (ver abajo).

### De dónde salen las cargas en el vuelo

| Momento | Tipo de carga | Qué la provoca |
| --- | --- | --- |
| Encendido y empuje del motor | Aceleración axial + vibración | El motor; dura pocos segundos |
| Eyección en el apogeo | Choque, dirección al azar | La carga de eyección empuja al CanSat fuera del tubo |
| Apertura del paracaídas de etapa 1 | Tirón en el anclaje | El paracaídas frena al CanSat |
| Apertura del principal (80%) | Tirón mayor en el anclaje | Pasa de 15 a 5 m/s |
| Aterrizaje | Choque en la base | Depende del suelo |

### Cálculo 1: ¿aguanta el tubo 30 G?

Con 500 g a 30 G, la fuerza total es F = m × a = 0,5 kg × 30 × 9,81 m/s² ≈ **147 N** (como apoyar 15 kg encima). El área de la pared es ≈ 553 mm², así que la tensión es 147 / 553 ≈ **0,27 MPa**. El ASA aguanta ≈ 37 MPa a lo largo de las capas y ≈ 31 MPa entre capas (hoja de datos Bambu ASA): aun contra el valor más débil, el margen es de más de 100 veces. El tubo no es el problema.

### Cálculo 2: ¿aguantan las fijaciones?

Cada pieza empuja su soporte con 30 veces su peso. Una batería de 47 g a 30 G hace ≈ 14 N; una cámara de 15 g, ≈ 4,4 N. Un inserto M3 resistió ≈ 1.000 N al arranque en un ensayo hecho en PETG (2.4); en ASA, de resistencia parecida, se espera el mismo orden, a verificar en el ensayo de tirón. El margen también es enorme, **siempre que la pieza esté atornillada y no solo apoyada o pegada con cola caliente**.

### Cálculo 3: el tirón del paracaídas principal

Cuando se abre el principal, el CanSat todavía baja a ≈ 15 m/s. La fuerza de arrastre en ese instante es:

```latex
F = \tfrac{1}{2}\,\rho\,v^2\,C_d\,A
```

Con ρ = 1,1 kg/m³, v = 15 m/s, C_d = 0,8 y A = 0,45 m² (el orden de magnitud del anexo de conceptos), F ≈ 45 N, unas **9 G** sobre el CanSat. Los paracaídas suelen dar un pico de apertura 1,5–2 veces mayor, así que el anclaje debe resistir **≈ 100 N con margen**. Es la carga más previsible del vuelo, y la que más sufre: el punto de amarre de las líneas y la unión de esa tapa con el tubo.

El principal podría abrirse por etapas o con un "slider" para suavizar el tirón; eso lo evalúa descenso.

### Cálculo 4: el aterrizaje

La desaceleración al tocar el suelo depende de cuántos centímetros "cede" el impacto: a = v² / (2 × d).

| Superficie | Distancia de frenado d | Desaceleración a 5 m/s |
| --- | --- | --- |
| Pasto o tierra blanda | ≈ 5 cm | ≈ 25 G |
| Tierra dura | ≈ 2 cm | ≈ 64 G |
| Piedra o superficie rígida | ≈ 1 cm | ≈ 127 G |

En suelo duro, el aterrizaje puede superar los 30 G. Formas de absorberlo:

- **Tapa inferior deformable**: una base impresa con relleno bajo o en panal, que se aplasta y "gasta" la energía. Se reemplaza después del vuelo.
- **Espuma** (goma eva) en la base.
- Componentes pesados lejos de la base que golpea.
- Bajar más lento: más cerca de 2 m/s que de 8 m/s, dentro del margen de C4.

### Vibración (15 G)

La vibración no rompe por fuerza sino por **repetición y resonancia**: una placa sostenida solo de un lado o con separadores muy largos se comporta como un trampolín y amplifica la vibración. Reglas prácticas: fijar las placas en los cuatro vértices, separadores lo más cortos posible, y nada de componentes pesados colgando de un cable o un pin.

### Simulación por elementos finitos (FEA)

Fusion 360, SolidWorks o FreeCAD pueden simular las cargas sobre el modelo 3D. Sirve para **comparar diseños** (¿qué tapa se deforma menos?) y encontrar zonas con tensión concentrada. No conviene confiar en los números absolutos: el software supone material macizo e isótropo, y una pieza impresa es más débil entre capas. Para la PDR alcanza con los cálculos manuales; una simulación de la tapa con el anclaje del paracaídas suma puntos.

### Ensayos: cómo probarlo en la práctica

CanSat USA define estos ensayos caseros ([Mission Guide 2026](https://cansatcompetition.com/docs/CanSat_Mission_Guide_2026.pdf)); son razonables para adoptarlos:

| Ensayo | Cómo se hace | Qué verifica |
| --- | --- | --- |
| Caída (≈ 30 G) | El CanSat cuelga de un cordón que no estira de 61 cm atado a un punto fijo; se lo levanta hasta la altura del amarre y se suelta. No se puede sostener el cordón con la mano | S5 y el anclaje del paracaídas; que no se corte la energía ni la telemetría |
| Vibración | Lijadora orbital (no de disco) de 12.000–14.000 oscilaciones/min, fija boca arriba en una morsa, con el CanSat montado encima. 5 ciclos de encendido de 5 s | S4; que nada se afloje y el acelerómetro siga midiendo |
| Térmico | Conservadora con secador de pelo, mantener 55–60 °C durante 2 h con el CanSat encendido | Que el plástico no se deforme y los pegamentos aguanten |
| Vacío | CanSat dentro de un balde de 18 L tapado y una aspiradora | Que la presión simulada dispare los mecanismos (prueba de software) |
| Fit check | Deslizar en un tubo del diámetro del cohete | S7 |

Además: **tirón del anclaje** con una balanza de equipaje colgando ≈ 10 kg (≈ 100 N), y registrar el acelerómetro del propio CanSat durante cada ensayo para mostrar cuántos G se alcanzaron.

### Propuesta inicial para discutir

- En la PDR: cálculos 1 a 4 como evidencia de que el diseño es viable, y la tabla de ensayos como plan.
- Diseñar con especial cuidado el anclaje del paracaídas y la tapa inferior absorbente.
- Hacer un primer ensayo de caída y de tirón con el prototipo en PLA, antes de la CDR, y repetirlos con las piezas de vuelo en ASA. El ensayo térmico solo vale en ASA: el PLA se ablanda a 55 °C.

### Preguntas para el equipo

- [ ] ¿Alguien tiene una lijadora orbital para el ensayo de vibración?
- [ ] ¿Qué velocidad de etapa 2 apunta descenso: más cerca de 3 o de 5 m/s? Cambia mucho el aterrizaje.
- [ ] ¿Hacemos una simulación FEA de la tapa con el anclaje, o solo cálculos?

## 2.6 Masa y centro de gravedad

Todavía no se puede dar un total: la masa depende de los componentes que elijan electrónica y descenso. Lo que sí se calcula hoy es la estructura impresa: después del tubo quedan **≈ 360 g**, y después de tubo, tapas y bandeja (modelo 3D preliminar), **≈ 285 g** para todo lo demás, con ASA.

El presupuesto vivo está en [`masa.yaml`](masa.yaml); el total del CanSat se calcula con `python presupuestos/calc/masa_total.py`.

### Qué pide el requisito

**S1**: "La masa combinada del CanSat y el contenedor debe ser de 500 gramos +/- 10 gramos." Es una ventana, no un máximo: **también hay que llegar**. Si el CanSat queda liviano, se agrega lastre; si queda pesado, hay que sacar algo.

### Lo que se puede calcular hoy: el tubo

La masa del tubo sale de la geometría (pared maciza de 2 mm, 90/86 × 230 mm, ≈ 127 cm³) por la densidad del material (2.2):

| Material del tubo | Masa del tubo | Queda para el resto |
| --- | --- | --- |
| PA12 (MJF) | ≈ 128 g | ≈ 372 g |
| **ASA (propuesto)** | **≈ 133–144 g** | **≈ 356–367 g** |
| PLA | ≈ 158 g | ≈ 342 g |
| PETG | ≈ 161 g | ≈ 339 g |

Con ASA quedan **≈ 360 g para todo lo demás**: tapas, bandeja, paracaídas, mecanismo, electrónica, baterías, cámaras, baliza y panel solar. Cada gramo que se ahorra en el tubo es un gramo más para el resto.

### Modelo 3D preliminar

Un modelo paramétrico simple (CadQuery) de la configuración B permite calcular también las tapas y la bandeja. Con todo macizo en ASA (1,05–1,13 g/cm³), **la estructura impresa pesa ≈ 212–228 g y quedan ≈ 270–290 g** para tornillería, descenso, electrónica y lastre.

| Pieza | Supuestos del modelo | Volumen (cm³) | Masa en ASA (g) |
| --- | --- | --- | --- |
| Tubo | 90/86 × 230 mm, chaflán 0,8 mm | 127,0 | 133–144 |
| Tapa superior | Tapón Ø 85,6 mm: disco de 3 mm + aro de 7 × 2 mm para tornillos radiales | 20,9 | 22–24 |
| Tapa inferior | Igual a la superior (sin anillo absorbente ni alojamiento de lastre todavía) | 20,9 | 22–24 |
| Bandeja | 80 × 150 × 3 mm, 120 agujeros de 3,2 mm cada 10 mm | 33,1 | 35–37 |
| **Total estructura impresa** |  | **201,9** | **212–228** |

Es una cota superior: las tapas y la bandeja con relleno parcial pesan menos, y faltan detalles (orificios, ventanas, alojamiento de cámaras, anclaje) que suman o restan pocos gramos. El modelo queda como base para el diseño detallado de la CDR.

### Una referencia real

El equipo 1043 de CanSat USA publicó su presupuesto completo en la PDR ([PDR 1043](https://www.cansatcompetition.com/docs/teams/cansat2026_1043_pdr_v07.pdf)), con un límite de 1.000 g:

| Parte | Masa | Proporción |
| --- | --- | --- |
| Estructura y mecánica (contenedor, ojiva, paracaídas, parapente, mecanismos, tornillería; incluye un huevo de ≈ 59 g y un disco de madera con cáncamo de ≈ 82 g que nosotros no llevamos) | ≈ 567 g | 57% |
| Electrónica (placas, sensores, radio, baterías, servos, cámaras) | ≈ 396 g | 40% |
| Margen | 11 g | 1% |

Dos lecciones: en un CanSat **la estructura suele llevarse la mitad o más (sin el huevo y el disco, la del 1043 sería ≈ 52%)** de la masa, y por eso el material del tubo es la palanca principal; y cada fila de su tabla indica de dónde sale el número (software, hoja de datos o medición).

### Cómo se arma el presupuesto

- Listar cada componente por subsistema (los mismos subsistemas de la plantilla PDR; ver "Subsistemas" en el anexo de conceptos).
- Poner su masa y **de dónde sale el número**: calculado, hoja de datos o medido en balanza. La planilla de puntaje lo pide explícitamente.
- Agregar una incertidumbre: grande para lo calculado o estimado, chica para lo medido.
- Sumar, comparar con la ventana de 490–510 g y decidir qué hacer con la diferencia.

En el repo, cada subsistema carga sus componentes en su propio `masa.yaml` y el script suma todos. Reparto de responsabilidades:

| Subsistema | Componente | Masa (g) | Incertidumbre (g) | Fuente | Quién la completa |
| --- | --- | --- | --- | --- | --- |
| Mecánico | Tubo exterior ASA 90/86 × 230 mm | 133–144 | ± 6 (densidad según marca) | Calculado (2.2) | Mecánica |
| Mecánico | Tapas superior e inferior | ≈ 45 (2 × 22) | ± 3; baja con relleno parcial | Modelo 3D preliminar, macizo | Mecánica |
| Mecánico | Bandeja y soportes | ≈ 35 | ± 2; baja con relleno parcial | Modelo 3D preliminar, macizo | Mecánica |
| Mecánico | Tornillos, tuercas e insertos | Por definir | Chica | Hojas de datos | Mecánica |
| Mecánico | Mecanismo de liberación (servo y traba) | Por definir | Chica | Hoja de datos del servo | Mecánica / descenso |
| Control de descenso | Paracaídas etapa 1 y segundo sistema, con líneas | Por definir | Según fuente | Hoja de datos o medido | Descenso |
| Sensores | Sensores y cámaras (C6, C7) | Por definir | Chica | Hojas de datos | Sensores |
| C&DH | Microcontrolador, memoria, radio y antena | Por definir | Chica | Hojas de datos | C&DH |
| EPS | Baterías (principal y baliza), reguladores, interruptores, LED, panel solar | Por definir | Chica | Hojas de datos | EPS |
| Todos | Placas de circuito, cables y conectores | Por definir | Grande hasta medir | Estimado, luego medido | Electrónica |
| Ajuste | Lastre | Lo que falte para 500 g | — | Calculado | Mecánica |

Para la PDR cada fila tiene que tener su número y su fuente; para la CDR, lo ideal es que esté medido en balanza.

### Lastre de ajuste

Conviene dejar desde el diseño un **alojamiento para lastre** (5–20 g) para afinar la masa al final, por ejemplo un hueco en la tapa inferior con tapa atornillada. Materiales: arandelas o tornillos de acero, o bolitas de acero. **No usar plomo**: es contaminante (S9).

### Centro de gravedad (CG)

El CG es el punto donde se puede considerar concentrada toda la masa. Nos importa por tres cosas:

- **Colgado del paracaídas**, el CanSat queda estable si el CG está lejos del punto de amarre. Con los paracaídas arriba, conviene el CG **bajo**.
- **La cámara a nadir** (C7) filma mejor si el CanSat no se balancea.
- **El aterrizaje** golpea primero la base: los componentes pesados no deben quedar justo sobre ella sin protección.

Compromiso posible: la batería (el componente más pesado) en el tercio inferior, pero sobre la tapa absorbente, no apoyada en ella.

Cómo calcularlo: en el modelo 3D (Fusion 360 y similares lo dan si se asigna la masa a cada pieza), o a mano con la suma de (masa × posición) dividida por la masa total. Cómo medirlo en el prototipo: apoyarlo horizontal sobre un borde (una regla de canto) y buscar el punto de equilibrio.

### Propuesta inicial para discutir

- Completar la plantilla con los componentes que elijan electrónica y descenso.
- Diseñar con un alojamiento de lastre en la base.
- Si el total supera 510 g, la primera palanca es el tubo: material (ASA → ASA-LW poco espumado → PA12) y largo.

### Preguntas para el equipo

- [ ] ¿Qué componentes concretos eligen electrónica y descenso, y cuánto pesan según su hoja de datos?
- [ ] ¿Tenemos balanza con resolución de 0,1 g para medir piezas?

## 2.7 Accesos e integración

El tubo no puede ser cerrado del todo: necesita orificios para los interruptores, una forma de ver el indicador de encendido, ventanas para las dos cámaras, salida de sonido para la baliza, lugar para el panel solar y **ventilación para el sensor de presión**. Todo eso tiene que quedar a ras para que el CanSat deslice (S7). Esta sección también propone el orden de armado.

### Qué piden los requisitos

| Requisito | Qué dice | Qué implica para mecánica |
| --- | --- | --- |
| E4 | Interruptor de encendido fácilmente accesible a través del contenedor, para poner la carga útil en STAND-BY | Un orificio alineado con el interruptor principal |
| E5 | Orificios de acceso para los interruptores de no más de 10 mm | Diámetro máximo de cada orificio |
| E6 | Indicador de encendido | El LED tiene que verse desde afuera |
| E9 | Interruptor de la baliza fácilmente accesible | Un segundo orificio |
| C8 | Baliza audible, independiente de la electrónica | El sonido tiene que salir del tubo |
| E3 | Uno o más paneles solares que reciban radiación y emitan una señal | Panel en la superficie exterior |
| C6 / C7 | Video de todo el descenso hacia cenit (arriba) y nadir (abajo), mostrando la activación de los sistemas de descenso | Dos ventanas con vista despejada |
| E7 | Funcionar al menos 2 horas integrado en el cohete | Probablemente se encienda antes de cargar el cohete, sin acceso después (a confirmar con la organización) |

### Interruptores (E4, E5, E9)

| Tipo | Cómo funciona | A favor | En contra |
| --- | --- | --- | --- |
| Deslizante empotrado | Se mueve con un palito o destornillador por el orificio | Simple, barato | Un golpe puede moverlo (M3); conviene con traba |
| Pulsador con enclavamiento | Se aprieta para encender y queda | Fácil de accionar | Puede saltar con el choque si no es de buena calidad |
| "Interruptor de tornillo" | Un tornillo que cierra el contacto entre dos tuercas al enroscarse (lo usa el equipo 1043) | No se mueve con golpes ni vibración | Lento de accionar; requiere diseño propio |
| Reed magnético | Un imán afuera abre o cierra el circuito, sin agujero | Sin orificios | Encender con un imán puede no cumplir "accesible a través del contenedor"; consultar |

El orificio va con un **margen bajo los 10 mm** (por ejemplo, 8 mm) y con un chaflán para guiar la herramienta.

### Indicador de encendido (E6)

Tres formas: el LED asomando por su propio orificio; el LED detrás del orificio del interruptor (un solo agujero para las dos cosas); o una **guía de luz**, un cilindro de plástico transparente que lleva la luz del LED hasta la pared.

### Cámaras (C6, C7)

Un problema de diseño: en la configuración B los paracaídas van arriba, así que **una cámara en el centro de la tapa superior miraría el paracaídas plegado** hasta que salga. Opciones:

- Cámara a cenit en el **borde** de la tapa superior o en el costado del tubo, apuntando hacia arriba y un poco hacia afuera: ve las líneas y la apertura del principal.
- Cámara a nadir en la **tapa inferior**, mirando hacia abajo a través de un orificio.

La lente puede quedar con orificio abierto (vista limpia, pero entra polvo) o detrás de una ventana de policarbonato (protegida, pero con reflejos). Las cámaras con lente de gran angular tienen que tener el orificio lo bastante amplio para que el borde no aparezca en la imagen.

#### Trade de montaje de cámaras

La planilla pide al menos dos formas de montar la cámara que mira al sistema de descenso. Se comparan dos ubicaciones para cada cámara; una tercera (cámara sobresaliendo del tubo, como una cámara de acción) se descarta porque no cumple S7. En todos los casos la cámara va en un alojamiento impreso atornillado (S8), como hizo el equipo 1094 de CanSat USA con soportes a medida fijados con tornillos M3 ([CDR 1094](https://www.cansatcompetition.com/docs/teams/Cansat2026_1094_cdr_v02.pdf)).

| Cámara | Opción | Vista | Protección | A ras (S7) | Integración | Total |
| --- | --- | --- | --- | --- | --- | --- |
| Cenit (C6) | **A. Borde de la tapa superior, apuntando arriba y algo hacia afuera** | 4 | 4 | 4 | 4 | **4,00** |
| Cenit (C6) | B. Ventana lateral en la parte superior del tubo, inclinada hacia arriba | 3 | 4 | 3 | 3 | 3,25 |
| Nadir (C7) | **A. Centro de la tapa inferior, lente hundida** | 5 | 3 | 5 | 4 | **4,30** |
| Nadir (C7) | B. Ventana lateral en la parte inferior del tubo, inclinada hacia abajo | 3 | 4 | 4 | 3 | 3,45 |

Pesos: vista 35%, protección ante eyección y aterrizaje 25%, a ras del tubo 20%, integración (fijación, cables, espacio) 20%. Puntajes de 1 a 5, evaluación cualitativa para discutir.

**Selección: A para las dos cámaras.** Las ventanas laterales protegen mejor, pero ven en ángulo y obligan a cortar la pared del tubo cerca de la bandeja.

Un conflicto a resolver: la cámara a nadir en el centro de la tapa inferior queda justo donde golpea el aterrizaje, y 2.5 propone que esa tapa sea absorbente. Solución propuesta: la lente queda **hundida 5–10 mm** dentro de la tapa, y un anillo exterior deformable toca el suelo primero.

### Baliza (C8)

Un zumbador dentro de un tubo cerrado apenas se oye. Hace falta una **rejilla de orificios** chicos frente al zumbador, o montarlo contra la pared con un orificio propio.

### Panel solar (E3)

E3 pide paneles que "reciban la radiación solar a fines de emitir una señal", o sea que deben estar en el exterior. Sobre un tubo curvo hay dos opciones: un **panel flexible** que acompañe la curva, o un **panel chico plano** en un rebaje del tubo para que no sobresalga. En ambos casos, a ras y protegido del roce con el cohete.

### Ventilación para el sensor de presión

Nuestro Anexo no lo menciona, pero es física: **si el tubo está cerrado, el barómetro mide la presión de adentro**, que cambia con retraso. La altitud saldría mal y el 80% se detectaría tarde. CanSat USA exige al menos dos orificios de ventilación de 6 mm por eso. Los orificios de los interruptores pueden cumplir esa función si están cerca del sensor, pero conviene sumar orificios propios.

### Secuencia de armado

1. Armar la electrónica sobre la placa de montaje, fuera del tubo, y probarla.
2. Colocar la batería principal y la de la baliza (cargadas).
3. Deslizar la placa dentro del tubo y atornillar la tapa inferior.
4. Plegar el paracaídas principal y armar el mecanismo de liberación (trabado).
5. Plegar el paracaídas de etapa 1 y colocar la tapa superior.
6. Encender por el orificio (E4), verificar el LED (E6) y la telemetría en la estación terrena.
7. Encender la baliza (E9).
8. Verificar masa en balanza y deslizar en el cohete.

Este orden define dos cosas del diseño: **las baterías tienen que poder cambiarse sin desarmar los paracaídas**, y el encendido tiene que poder hacerse con todo cerrado. Conviene hacer una lista de verificación para el día del lanzamiento.

### Propuesta inicial para discutir

- Interruptor de tornillo o deslizante con traba, en orificios de 8 mm, con el LED visible por el mismo orificio.
- Cámara a cenit en el borde de la tapa superior; cámara a nadir en el centro de la tapa inferior, con la lente hundida y un anillo que absorba el aterrizaje.
- Rejilla para la baliza y dos orificios de ventilación de 6 mm cerca del barómetro.
- Panel solar plano en un rebaje del tubo.

### Preguntas para el equipo

- [ ] ¿Qué cámaras elige electrónica, y cuánto miden?
- [ ] ¿El panel solar tiene que alimentar algo o solo detectar luz ("emitir una señal")?
- [ ] ¿Consultamos si un interruptor magnético cuenta como "accesible a través del contenedor"?
- [ ] ¿Cómo se recargan las baterías si hay demoras en la rampa (E7 pide 2 horas)?

## 2.8 Interfaz con el cohete

El CanSat viaja dentro del fuselaje, en la sección superior (C1), y sale empujado por la carga de eyección del motor (C2). El cohete de la categoría universitaria todavía no está publicado, así que esta sección junta lo que se sabe, lo que implica para el diseño y lo que falta preguntar.

### Lo que sabemos del vehículo

- En las ediciones de secundario se usó un cohete SKYTEC de 1,10 m de altura y 80 mm de diámetro ([argentina.gob.ar](https://www.argentina.gob.ar/node/344271)), con vuelos de 230 a 300 m ([Tiempo Argentino](https://www.tiempoar.com.ar/ta_article/despertando-la-vocacion-cientifica-alumnos-de-escuelas-secundarias-disenaron-satelites-y-los-lanzaron-en-el-centro-espacial-de-cordoba/)).
- Ese cohete no sirve de referencia directa: no entra un CanSat de 90 mm y las Bases piden más de 500 m. Habrá un vehículo más grande.
- La ejecución técnica de esta edición está a cargo de ACEMA (Asociación de Cohetería Experimental y Modelista de Argentina) ([CONAE](https://www.argentina.gob.ar/noticias/la-conae-lanza-cansat-argentina-2026)). Es probable que ellos definan el cohete y sus datos.

### Cómo sale el CanSat

Como se explica en el anexo de conceptos, al final del retardo se enciende la carga de eyección y el gas a presión empuja hacia afuera todo lo que hay en la sección superior. Las guías de CanSat USA advierten que en ese momento la orientación no está controlada y el despliegue es violento.

Una diferencia importante con CanSat USA: allá el contenedor va arriba del cohete y la carga útil hace de ojiva. Acá todo va **dentro** del fuselaje, así que no diseñamos ojiva, pero todo depende de que el CanSat deslice bien.

### Qué implica para el diseño

- **Superficie exterior lisa**: interruptores, ventanas de cámara y panel solar a ras, sin salientes que enganchen.
- **Diámetro nunca mayor a 90 mm** y extremos chaflanados (ver 2.3).
- **Paracaídas de etapa 1 que salga solo**, sin depender de cómo quede orientado el CanSat (C3 pide despliegue automático).
- **Protección del calor de la eyección**: en cohetería se usan pistones, guata o bolsas de despliegue. Falta saber qué provee el cohete.
- **Cargas**: la eyección y la apertura del paracaídas son los choques que entran en el análisis de 30 G (2.5).

### Opciones según lo que responda la organización

| Si el cohete... | Entonces nosotros... |
| --- | --- |
| Tiene pistón o protección propia | Solo cuidamos el ajuste y la salida |
| No tiene protección | Agregamos una tapa o disco de sacrificio en el extremo expuesto, más masa |
| Comparte sección con su propio paracaídas | Hay que acordar orden de salida y cómo se evita el enredo |
| Tiene la sección más corta que 230 mm | Recortamos largo y redistribuimos volumen |

### Cómo lo verificamos

**Fit check**: con un tramo de tubo del mismo diámetro interior que el cohete, el CanSat debe deslizar por su propio peso con el tubo vertical, en ambas orientaciones. Conviene hacerlo con el primer prototipo impreso, no recién en la FRR.

### Preguntas para el equipo

- [ ] ¿Quién canaliza las preguntas a la organización (docente responsable o Aula Virtual)?
- [ ] ¿Conseguimos un tramo de tubo de 95 mm (PVC, cartón) para el fit check mientras tanto?

## 2.9 Mecanismo de liberación

Se recomienda un **servo que tira de un pasador**: el pasador atraviesa los lazos del cordón que mantiene cerrado el compartimento del segundo sistema de descenso, y al 80% de la altitud el servo lo retira. Es el único mecanismo obligatorio del CanSat (C4) y la planilla pide comparar al menos dos estrategias, así que esta sección las evalúa con criterios explícitos.

### Qué tiene que hacer y qué restricciones tiene

- **Mantener cerrado** el compartimento del segundo sistema durante el empuje, la eyección y la primera etapa de descenso (15 G, 30 G).
- **Abrir** cuando el software detecta el 80% de la altitud máxima en la bajada.
- **M1**: nada pirotécnico ni químico. **M2**: si usa calor, encerrado. **M3**: "mantener su configuración o estados bajo todas las fuerzas aplicadas": no puede abrirse solo por un golpe ni cerrarse después de abrir.
- Conviene que también se pueda activar por telecomando desde la estación terrena (G15), para los ensayos.

El mecanismo es el mismo para las configuraciones A y B: en A libera la carga útil del contenedor; en B libera el segundo paracaídas o parapente. Lo que se libera lo define descenso; cómo se retiene y se suelta, mecánica.

### Opciones

**Servo con traba (pestillo).** El brazo del servo engancha una pestaña de la tapa del compartimento; al girar la suelta. Simple y reutilizable, pero la fuerza de la tapa actúa sobre el brazo del servo: un golpe fuerte puede forzarlo, salvo que la traba se diseñe para que la carga no lo haga girar.

**Servo con pasador ("pin-pull").** Un cordón mantiene cerrada la tapa; sus extremos terminan en lazos que se enhebran en un pasador. El servo retira el pasador y el cordón se suelta. La carga del cordón queda sobre el pasador, no sobre el servo: el servo solo vence el rozamiento al retirarlo. Reutilizable y fácil de ensayar cientos de veces.

**Corte de cordón por calor (hilo de nicrom o resistencia).** El cordón pasa en contacto con un hilo de nicrom o una resistencia; al pasarle corriente se calienta y corta el cordón. Es la solución clásica en CanSat y CubeSat: muy liviana y sin piezas móviles. En un CanSat experimental, un cordón de Dyneema de 0,2 mm (≈ 53 N de resistencia) cortado por una resistencia liberó los paneles en menos de 0,89 s ([Aerospace, 2021](https://www.mdpi.com/2226-4310/8/7/192)). Desventajas: se usa una sola vez (hay que rearmar el cordón en cada ensayo), pide un pico de corriente alto, y por M2 tiene que quedar encerrado.

**Electroimán.** Retiene una placa de acero mientras recibe corriente y la suelta al cortarla. **Se descarta**: si la batería falla o hay un microcorte por el choque, se abre solo (no cumple M3), y consume energía durante las 2 horas de espera en el cohete (E7).

### Matriz de decisión

Cumplir M1–M3 es eliminatorio. Entre las que cumplen, puntaje de 1 a 5 (5 = mejor):

| Criterio | Peso | Servo con traba | Servo con pasador | Corte por calor |
| --- | --- | --- | --- | --- |
| Retención bajo 15 G y 30 G (M3) | 35% | 3 | 4 | 4 |
| Posibilidad de ensayar y repetir | 20% | 5 | 5 | 2 |
| Simplicidad de fabricación e integración | 20% | 4 | 3 | 3 |
| Masa | 15% | 3 | 3 | 5 |
| Consumo eléctrico | 10% | 4 | 4 | 2 |
| **Total ponderado** | 100% | **3,70** | **3,85** | **3,35** |

Los puntajes son una evaluación cualitativa para discutir en el equipo, no una medición. El servo con pasador gana por un margen chico, sobre todo porque la carga no recae en el servo; si el equipo valora más la masa, el corte por calor queda cerca.

### Opción recomendada: servo con pasador

**[Figura pendiente]** Mecanismo de pasador · trabado y liberado. La carga del cordón la toma el pasador; el servo solo vence el rozamiento al retirarlo.

- **Servo**: micro servo con engranajes metálicos, atornillado a la estructura del compartimento (S8). Su modelo y masa los define mecánica con descenso.
- **Pasador**: varilla de acero o latón de ≈ 2 mm, guiada por un buje impreso para que no se trabe ni se salga con la vibración.
- **Cordón**: Dyneema o nylon trenzado, con resistencia muy superior a la carga del paracaídas plegado.
- **Para cumplir M3**: el pasador queda retenido por rozamiento y por el propio servo; una vez retirado no puede volver. Antes de cada vuelo se verifica que entre y salga sin forzar.
- **Ensayo**: activarlo por telecomando con el compartimento cargado, después del ensayo de vibración y del de caída (2.5), y con el CanSat colgado para simular el tirón del paracaídas de etapa 1.

### Preguntas para el equipo

- [ ] ¿Qué libera exactamente el mecanismo: el principal (B1, B3), el corte del paracaídas de etapa 1 (B2) o la carga útil (A)? Lo define descenso.
- [ ] ¿Preferimos el corte por calor para ahorrar masa, aceptando rearmar el cordón en cada ensayo?
- [ ] ¿Qué servo usamos, y lo alimenta la batería principal o un regulador propio? Lo define EPS.

## Preguntas abiertas para la organización

Las Bases (§2) indican que las consultas por mail se reciben durante la inscripción; si ese período cerró, canalizarlas por el Aula Virtual o el docente responsable.

- [ ] ¿Qué cohete se usará y cuál es el diámetro interior y el largo útil de la sección de carga?
- [ ] ¿Los 95 mm de las Bases son el espacio del cohete y los 90 mm del Anexo el diámetro máximo del CanSat? ¿Con qué tolerancia?
- [ ] ¿Los 200–250 mm incluyen ambos paracaídas plegados? ¿El paracaídas del cohete comparte la sección?
- [ ] ¿Cómo se protege el CanSat de los gases de eyección (pistón, guata) o debemos proveerlo?
- [ ] ¿En qué orientación va dentro del fuselaje y cómo queda retenido en el ascenso?
- [ ] ¿Qué apogeo, aceleración máxima de empuje y velocidad en la eyección se esperan?
- [ ] ¿C4 exige separar físicamente la carga útil del contenedor, o alcanza con desplegar un segundo sistema de descenso?
- [ ] ¿Los interruptores (E4/E9) deben ser accesibles con el CanSat integrado, o se enciende antes de insertarlo?
- [ ] ¿Pueden facilitar un plano o un tramo de tubo para un fit check previo a la FRR?

Preguntas que surgieron después:

- [ ] La planilla de puntaje pide ojiva, huevo como instrumento, cáncamo en disco de madera, parapente y liberación de la carga útil, que no están en el Anexo A. ¿Cuál manda? ¿Esas diapositivas se adaptan?
- [ ] El largo: ¿200 mm fijos (Bases §4) o de 200 a 250 mm (S3)?
- [ ] C4 pide 5 m/s "promedio durante todo el descenso": ¿se promedia desde el apogeo o desde el 80%?
- [ ] ¿Un interruptor magnético (sin orificio) cumple E4 "accesible a través del contenedor"?

## Anexo: conceptos clave

Antes de discutir opciones conviene tener un vocabulario común. Acá se explica lo que aparece en las Bases y el Anexo A y lo que se usa en el resto del documento.

### CanSat, contenedor y carga útil

- **CanSat**: el sistema completo que entregamos, todo lo que entra al cohete y vuelve al suelo. S1 limita su masa a 500 g ± 10 g, contando el contenedor.
- **Carga útil (payload)**: la parte que cumple la misión: electrónica, sensores, radio, cámaras, baterías y baliza. Es el equivalente al satélite o instrumento en una misión real.
- **Contenedor (container)**: la envoltura que protege a la carga útil durante el lanzamiento y la eyección. Es el equivalente al carenado que protege a un satélite dentro de un lanzador.

En CanSat USA, de donde viene nuestro Anexo, son **dos piezas distintas**. Su guía 2020 exige que el contenedor sea sólido, rodee por completo a la carga útil y pueda tener abierto el extremo por donde ella sale ([guía 2020](https://www.scribd.com/document/530201229/CanSat-Mission-Guide-2020)). En vuelo, el contenedor libera a la carga útil a una altura fijada.

En nuestro Anexo, "contenedor" aparece en estos requisitos, pero ninguno dice explícitamente que se separe:

| Requisito | Qué dice del contenedor |
| --- | --- |
| C1 | Va montado dentro del fuselaje, en la parte superior del cohete |
| C2 | Sale del cohete junto con la carga útil en la eyección |
| S1 | Su masa se suma a la del CanSat: 500 g ± 10 g en total |
| S7 | Puede sujetar piezas desplegables, pero debe deslizar libremente |
| S9 | Sus materiales no deben ser contaminantes |
| E4, E5, E9 | Los interruptores deben ser accesibles a través de él, con orificios de 10 mm como máximo |

Hay entonces dos lecturas posibles: contenedor y carga útil como piezas que se separan en vuelo, o contenedor como carcasa exterior que protege y no se separa. Esto es el centro de la discusión de 2.1.

### Subsistemas

Un **subsistema** es una parte del CanSat que cumple una función concreta, con sus propios componentes, sus propios requisitos y un responsable. Dividir el sistema así permite que cada integrante trabaje en paralelo sobre su parte, como en una misión espacial real, y después se integre todo. Lo que conecta a dos subsistemas (un cable, un tornillo, un dato que se pasa) se llama **interfaz**, y es donde más problemas aparecen.

Para nuestro CanSat los subsistemas no hay que inventarlos: la plantilla de la PDR ya los define, y el Anexo A agrupa sus requisitos de forma parecida.

| Subsistema | Qué hace | Requisitos del Anexo | Páginas de la plantilla PDR |
| --- | --- | --- | --- |
| Sensores | Miden presión, temperatura, posición GPS, aceleración, rotación, tensión y corriente de batería; incluye las dos cámaras | SN, C6, C7 | 15–31 |
| Control de descenso | Paracaídas de etapa 1, segundo sistema de descenso y cálculo de velocidades | C3, C4 | 32–36 |
| Mecánico | Estructura, materiales, fijación, mecanismos de liberación, masa y accesos (este documento) | S1–S9, M1–M4 | 37–46 |
| Comunicaciones y manejo de datos (C&DH) | Microcontrolador, memoria, radio, formato de telemetría y comandos | C5, X | 47–56 |
| Potencia eléctrica (EPS) | Baterías, reguladores, interruptores, indicador de encendido, panel solar, presupuesto de energía | E1–E9, C8 | 57–65 |
| Software de vuelo (FSW) | Estados de la misión, detección del apogeo y del 80%, activación de mecanismos, recuperación ante reinicios | F | 66–68 |
| Estación terrena (GCS) | Computadora, antena y software que reciben, grafican y guardan la telemetría y envían comandos | G | 69–74 |

Además hay partes de la PDR que no son subsistemas sino **transversales**: el panorama del sistema (configuración, CONOPS, compatibilidad con el cohete), integración y ensayos, y gestión (costos y cronograma).

Ejemplos de interfaces que tocan a mecánica:

- **Con descenso**: volumen de los paracaídas, punto de anclaje y mecanismo de liberación.
- **Con sensores**: ventanas de cámaras y ventilación del barómetro.
- **Con EPS**: cuna de batería, orificios de interruptores, panel solar.
- **Con C&DH**: ubicación de la antena, que no puede quedar tapada por piezas conductoras.
- **Con todos**: el presupuesto de masa (2.6), que suma lo de cada subsistema.

### El cohete y el vuelo

- **Cohete sonda**: sube, llega a un punto máximo y vuelve sin entrar en órbita (vuelo suborbital).
- **Fuselaje (airframe)**: el tubo que forma el cuerpo del cohete. La **sección de carga** es el tramo donde va el CanSat.
- **Ojiva (nose cone)**: la punta del cohete. En CanSat USA la carga útil cumple ese rol; en nuestro caso no.
- **Apogeo**: el punto más alto del vuelo, donde la velocidad vertical es cero.

Un motor de cohetería modelista tiene tres fases:

- **Empuje**: el propelente quema y acelera el cohete.
- **Retardo (delay)**: un grano que no da empuje y deja que el cohete siga subiendo por inercia hasta cerca del apogeo; además suele largar humo para seguirlo con la vista ([Discount Rocketry](https://discountrocketry.com/model_rocket_motor.php)).
- **Carga de eyección**: al terminar el retardo se enciende una pequeña carga, típicamente de pólvora, que genera gas y empuja hacia afuera el sistema de recuperación ([ASP Rocketry](https://www.asp-rocketry.com/uploaded_files/files/About-Model-Rocket-Engines.pdf)).

Para nosotros, la eyección es un golpe de gas caliente a presión que expulsa al CanSat sin orientación controlada. De ahí salen S5 (choque), S7 (deslizar libre) y la necesidad de proteger los paracaídas del calor.

### Descenso en dos etapas

En cohetería esto se llama **dual deploy**: un paracaídas chico (drogue) se abre en el apogeo y baja rápido, y uno grande (principal) se abre más cerca del suelo. Así el viento tiene menos tiempo para desplazar al cohete lejos ([SSI Stanford](https://ssi-wiki.stanford.edu/Special:MobileDiff/1596)). Los principales suelen ser de 2 a 4 veces más grandes que el drogue.

En nuestro caso:

- **Etapa 1** (C3): desde la eyección, 15 ± 3 m/s.
- **Etapa 2** (C4): desde el 80% de la altitud máxima, ya bajando, 5 ± 3 m/s promedio.

Ejemplo de "80% de la altitud máxima": si el apogeo es 600 m, el cambio ocurre al pasar por 480 m de bajada. El software tiene que guardar el apogeo y comparar contra él.

Una ambigüedad para consultar: C4 pide 5 m/s promedio "durante todo el descenso". Si se promedia desde el apogeo, el 20% inicial a 15 m/s obliga a bajar el resto a ≈ 4,3 m/s para que el promedio dé 5. Sigue dentro de ±3 m/s, pero cambia el tamaño del paracaídas.

**¿Para qué sirve en nuestro caso?** En cohetería, el dual deploy reduce la deriva por viento porque se cae rápido la mayor parte del trayecto. Acá el beneficio físico es casi nulo: solo el 20% superior se baja rápido. Con apogeo de 600 m y viento de 5 m/s:

| Esquema | Tiempo de descenso | Deriva |
| --- | --- | --- |
| Un solo paracaídas a 5 m/s | 120 s | ≈ 600 m |
| 15 m/s hasta 480 m, luego 5 m/s | ≈ 104 s | ≈ 520 m |
| Promedio de 5 m/s sobre todo el descenso (otra lectura de C4) | 120 s | ≈ 600 m |

El valor real es otro: el certamen evalúa que el CanSat **detecte una condición en vuelo y ejecute un mecanismo por sí solo**, como haría una sonda real, y que las cámaras lo registren (C6, C7). Eso vale igual para A o para B: la separación tampoco aporta una ventaja física, es la forma que eligió CanSat USA para su misión.

### Velocidad terminal

Un cuerpo con paracaídas acelera hasta que la resistencia del aire iguala su peso; esa velocidad constante es la velocidad terminal:

```latex
v_t = \sqrt{\frac{2\,m\,g}{\rho\,C_d\,A}}
```

Donde m es la masa (kg), g = 9,81 m/s², ρ la densidad del aire (≈ 1,1–1,2 kg/m³ según la altura del sitio, TBR), C_d el coeficiente de arrastre del paracaídas (≈ 0,8 para un domo simple, a confirmar con descenso) y A el área del paracaídas (m²).

Orden de magnitud con 500 g, ρ = 1,1 y C_d = 0,8:

| Etapa | Velocidad objetivo | Área necesaria | Diámetro aprox. |
| --- | --- | --- | --- |
| 1 | 15 m/s | ≈ 0,05 m² | ≈ 25 cm |
| 2 | 5 m/s | ≈ 0,45 m² | ≈ 75 cm |

El dimensionamiento real lo hace descenso; a mecánica le importa porque define cuánto volumen ocupan plegados.

### Holgura y tolerancia

- **Tolerancia**: cuánto puede variar una medida al fabricarla. Ejemplo: 90 mm con tolerancia 0/−0,5 mm significa que la pieza puede medir entre 89,5 y 90,0 mm.
- **Holgura (juego)**: el espacio libre entre dos piezas que encajan. Puede darse por lado (radial) o en total (diametral): un CanSat de 90 mm en un tubo de 95 mm tiene 5 mm diametrales, 2,5 mm por lado.
- Poca holgura: se traba al salir (incumple S7). Mucha: el CanSat golpetea dentro del tubo con la vibración (S4).

### Cargas: qué significan 15 G y 30 G

1 G es la aceleración de la gravedad (9,81 m/s²). Bajo n G, cada pieza empuja sobre su soporte n veces su peso. Ejemplo: una batería 18650 de unos 47 g a 30 G ejerce ≈ 14 N, como si pesara 1,4 kg.

- **Vibración (S4, 15 G)**: oscilación sostenida durante el empuje. Afloja tornillos, fatiga soldaduras y suelta conectores.
- **Choque (S5, 30 G)**: un pico breve: la eyección, la apertura del paracaídas o el aterrizaje.

CanSat USA usa los mismos valores: 15 G de aceleración de lanzamiento y 30 G de choque ([guía 2021](https://www.scribd.com/document/483209181/CanSat-Mission-Guide-2021)).

### Vocabulario de las revisiones

| Término | Qué significa |
| --- | --- |
| PDR | Revisión Preliminar de Diseño (Etapa 2): mostrar que entendemos los requisitos y tenemos un diseño viable con opciones evaluadas |
| CDR | Revisión Crítica de Diseño (Etapa 3): diseño detallado, pruebas y TBD resueltos |
| FRR / PFR | Revisión de preparación de vuelo (presencial, el día anterior) y revisión posterior al vuelo |
| Trade | Comparación de dos o más opciones con criterios explícitos y una elección justificada; la planilla lo puntúa en casi todas las diapositivas |
| TBD | To Be Determined: dato que todavía no está definido |
| TBR | To Be Reviewed: dato propuesto que falta confirmar |
| CONOPS | Concepto de operaciones: la secuencia de la misión desde el armado hasta la recuperación |
| Fit check | Prueba de encaje del CanSat en el tubo del cohete |

## Fuentes

- Bases y Condiciones y Anexo A, CANSAT Universitario 2026/2027 (CONAE) — ver `referencia/`
- [Lanzamiento CANSAT Argentina, cohete SKYTEC](https://www.argentina.gob.ar/node/344271)
- [La CONAE lanza CANSAT Argentina 2026](https://www.argentina.gob.ar/noticias/la-conae-lanza-cansat-argentina-2026)
- [Tiempo Argentino: lanzamiento CANSAT secundario](https://www.tiempoar.com.ar/ta_article/despertando-la-vocacion-cientifica-alumnos-de-escuelas-secundarias-disenaron-satelites-y-los-lanzaron-en-el-centro-espacial-de-cordoba/)
- [PDR CanSat USA 2026, Team 1043 Daedalus](https://www.cansatcompetition.com/docs/teams/cansat2026_1043_pdr_v07.pdf)
- [CanSat Mission Guide 2020](https://www.scribd.com/document/530201229/CanSat-Mission-Guide-2020)
- [CanSat Mission Guide 2023](https://www.scribd.com/document/611536709/CanSat-Mission-Guide-2023e)
- [CanSat Mission Guide 2021](https://www.scribd.com/document/483209181/CanSat-Mission-Guide-2021)
- [Discount Rocketry: fases de un motor modelista](https://discountrocketry.com/model_rocket_motor.php)
- [ASP Rocketry: About Model Rocket Engines](https://www.asp-rocketry.com/uploaded_files/files/About-Model-Rocket-Engines.pdf)
- [SSI Stanford: dual deployment](https://ssi-wiki.stanford.edu/Special:MobileDiff/1596)
- [Guía de filamentos Bambu Lab](https://cdn1.bambulab.com/filament/a5e185aed14e6/filament-guide-en-4.pdf)
- [Hoja de datos PLA Basic](https://cdn.shopify.com/s/files/1/0380/5149/files/Bambu_PLA_Basic_Technical_Data_Sheet.pdf)
- [Hoja de datos PLA-CF](https://cdn.shopify.com/s/files/1/0380/5149/files/Bambu_PLA-CF_Technical_Data_Sheet.pdf)
- [Hoja de datos PETG-CF](https://cdn.shopify.com/s/files/1/0380/5149/files/Bambu_PETG-CF_Technical_Data_Sheet.pdf)
- [All3DP: PLA vs ABS vs PETG](https://all3dp.com/2/pla-vs-abs-vs-petg/)
- [CanSat Mission Guide 2026 (CanSat USA)](https://cansatcompetition.com/docs/CanSat_Mission_Guide_2026.pdf)
- [CNC Kitchen: insertos y roscas en piezas impresas](https://www.cnckitchen.com/blog/helicoils-threaded-insets-and-embedded-nuts-in-3d-prints-strength-amp-strength-assessment)
- [Protolabs: hoja de datos MJF PA 12](https://www.protolabs.com/media/1010893/2019-mjf-datasheet-pa-12-black.pdf)
- [Hoja de datos PAHT-CF](https://cdn.shopify.com/s/files/1/0380/5149/files/Bambu_PAHT-CF_Technical_Data_Sheet.pdf)
- [Hoja de datos Bambu ASA](https://polyalkemi.no/wp-content/uploads/2024/01/Bambu_ASA_Technical_Data_Sheet.pdf)
- [Hoja de datos Polymaker PolyLite ASA](https://cdn.shopify.com/s/files/1/0603/6609/files/PolyLite_ASA_TDS_V5.1.pdf)
- [Hoja de datos Bambu ASA Aero (ASA espumado)](https://cdn.shopify.com/s/files/1/0584/7236/6216/files/Bambu_ASA_Aero_Technical_Data_Sheet.pdf)
- [CDR CanSat USA 2026, Team 1094](https://www.cansatcompetition.com/docs/teams/Cansat2026_1094_cdr_v02.pdf)
- [Aerospace (MDPI, 2021): CanSat con mecanismo de corte de cordón](https://www.mdpi.com/2226-4310/8/7/192)
- Modelo 3D preliminar propio (CadQuery), archivos STEP y STL del equipo
