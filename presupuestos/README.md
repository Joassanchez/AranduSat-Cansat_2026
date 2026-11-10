# Presupuestos

## Masa (S1: 500 g ± 10 g)

Cada subsistema carga sus componentes en `subsistemas/<subsistema>/masa.yaml`. El total se calcula con:

```bash
python presupuestos/calc/masa_total.py              # tabla en la terminal
python presupuestos/calc/masa_total.py --markdown   # tabla para el PDR (diapositivas 42–46)
```

El script suma lo definido, combina las incertidumbres (RSS y peor caso), lista lo pendiente, compara con la ventana de 490–510 g y compara cada subsistema con su parte en [`asignacion-masa.yaml`](asignacion-masa.yaml) (estructura 230 g, descenso 60 g, electrónica y sensores 120 g, potencia 70 g, margen 20 g, según la Guía). Sale con error si algún `masa.yaml` tiene problemas de formato (fuente inválida, masa sin referencia).

## Próximos

- Presupuesto de energía (EPS, diapositiva 65, en Wh).
- Presupuesto de costos (C9 y diapositivas 80–81).
