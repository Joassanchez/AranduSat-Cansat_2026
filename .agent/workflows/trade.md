---
description: Hacer un trade (comparación de 2+ alternativas y selección) para un ítem del scoresheet
---

# /trade — comparación y selección

Roles: **investigador → ingeniero → redactor**. Entrada: el tema del trade y los ítems del scoresheet (P..) que cubre.

## 1. Entender qué pide el jurado

- Leé la fila del ítem en `referencia/scoresheet.md` (columna "Qué espera el jurado").
- Leé los requisitos que aplican en `referencia/anexo-a.md`.
- Anotá los criterios de selección y su peso **antes** de buscar opciones, para no ajustarlos a una opción favorita.

## 2. Investigar (investigador)

- Buscá **al menos 3 alternativas** reales que se consigan en Argentina o por courier.
- Para cada una: modelo, specs relevantes al ítem, masa, dimensiones, consumo si aplica, precio aproximado y **link al datasheet**.
- Descartá las que violen un requisito, diciendo cuál (por ejemplo, LiPo → E1).

## 3. Verificar (ingeniero)

- Comprobá que cada alternativa cumpla los requisitos con números: rango, masa, consumo, interfaz.
- Si el cálculo es repetible, dejalo como script en `subsistemas/<subsistema>/` o en `presupuestos/calc/`.

## 4. Escribir (redactor)

Archivo `subsistemas/<subsistema>/trades/AAAA-MM-DD-<tema>.md` con esta estructura:

```markdown
# Trade: <tema>

Cubre: P.. (scoresheet) · Requisitos: ..

## Criterios
| Criterio | Peso | Por qué importa |

## Alternativas
| Opción | Spec 1 | Spec 2 | Masa (g) | Precio | Fuente |

## Matriz de decisión
| Criterio | Peso | Opción A | Opción B | Opción C |
(puntaje 1–5, total ponderado)

## Selección
Opción elegida y 3–5 razones. Qué la haría cambiar.

## Preguntas abiertas
```

Después:

- Creá la decisión en `decisiones/` desde `_plantilla.md`, estado `propuesto`.
- Si la opción elegida suma masa, agregala al `masa.yaml` del subsistema.
- Hacé commit: `<subsistema>: trade de <tema>`.
