---
description: Recalcular el presupuesto de masa y verificar márgenes contra los requisitos
---

# /calcular — presupuestos y márgenes

Rol: **ingeniero**.

1. Corré `python presupuestos/calc/masa_total.py`.
2. Leé la salida: total, incertidumbre, componentes pendientes (`masa_g: null`) y margen contra la ventana de S1 (490–510 g).
3. Reportá a la persona:
   - Total actual y rango con incertidumbre.
   - Cuántos componentes faltan y de qué subsistema.
   - Si el total (con su incertidumbre) cae fuera de la ventana, qué subsistema aporta más y qué palancas hay (ver `subsistemas/mecanica/seccion-2-mecanica.md` §2.6).
4. Si cambiaste masas de tu subsistema, verificá que cada fila tenga `fuente` y `referencia`.

Otros cálculos (velocidad terminal, consumo, tirón del paracaídas): dejá la fórmula, los valores con unidades y el resultado en el trade o en un script. Nunca un número sin su cálculo.
