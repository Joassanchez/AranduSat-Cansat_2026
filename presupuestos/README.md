# Presupuestos

## Masa (S1: 500 g ± 10 g)

Cada subsistema carga sus componentes en `subsistemas/<subsistema>/masa.yaml`. El total se calcula con:

```bash
python presupuestos/calc/masa_total.py              # tabla en la terminal
python presupuestos/calc/masa_total.py --markdown   # tabla para el PDR (diapositivas 42–46)
```

El script suma lo definido, combina las incertidumbres (RSS y peor caso), lista lo pendiente y compara con la ventana de 490–510 g. Sale con error si algún `masa.yaml` tiene problemas de formato (fuente inválida, masa sin referencia).

## Próximos

- Presupuesto de energía (EPS, diapositiva 65, en Wh).
- Presupuesto de costos (C9 y diapositivas 80–81).
