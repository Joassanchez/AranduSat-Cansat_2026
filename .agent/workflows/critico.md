---
description: Revisar el trabajo de una rama como lo haría el jurado (correr en una conversación nueva)
---

# /critico — revisión independiente

Rol: **crítico**. Corré este workflow en una **conversación nueva**, sin el historial de quien hizo el trabajo. Tu trabajo es encontrar problemas, no aprobar.

## 1. Qué cambió

- `git diff main...HEAD --stat` y luego el diff de los archivos relevantes.
- Identificá qué ítems del scoresheet (P..) y qué requisitos dice cubrir el trabajo.

## 2. Revisar contra el scoresheet

Para cada ítem que cubre, leé su fila en `referencia/scoresheet.md` y verificá:

- [ ] Los trades muestran **2 o más alternativas** con specs comparables.
- [ ] Hay una **selección explícita con criterios** y razones.
- [ ] Se cubre todo lo que pide la columna "Qué espera el jurado" (por ejemplo, el ítem de batería pide corriente máxima y capacidad en mAh **y** Wh).

## 3. Revisar contra los requisitos

- [ ] Ninguna opción seleccionada viola un requisito del Anexo A (revisá en particular E1: no LiPo; M1: no pirotecnia; M4: no contactos de resorte; S2/S3: dimensiones; S1: masa; X1: frecuencias ENACOM).
- [ ] Los conflictos conocidos (ver `AGENTS.md`) están señalados, no resueltos por cuenta propia.

## 4. Revisar fuentes y números

- [ ] Cada spec tiene link a datasheet o fuente oficial. Abrí al menos 3 links al azar y verificá que el número coincida.
- [ ] Cada cálculo tiene fórmula, valores con unidades y resultado. Rehacé al menos uno.
- [ ] Las masas nuevas están en `masa.yaml` con fuente e incertidumbre, y `python presupuestos/calc/masa_total.py` corre sin errores.

## 5. Revisar el formato de la Guía

- [ ] La parte **Qué pide** de cada subsección no fue modificada.
- [ ] **Opciones** tiene al menos dos alternativas con datos y fuente.
- [ ] **Decisión** cabe en una o dos líneas y cita el requisito que cumple.
- [ ] La decisión está en el registro de `decisiones/guia-12-decisiones-y-cumplimiento.md`.
- [ ] Las dudas nuevas para la organización están en `consultas-conae.md`.
- [ ] Si la subsección depende de un supuesto de diseño de `AGENTS.md`, lo dice.

## 6. Revisar el proceso

- [ ] Solo se modificaron archivos de la carpeta del subsistema y `decisiones/` (o hay pedido explícito).
- [ ] Las decisiones nuevas quedaron como propuestas.
- [ ] `ESTADO.md` está actualizado.

## 7. Informe

Escribí el informe con este formato y dáselo a la persona para pegarlo en el PR:

```markdown
## 🤖 Revisión del crítico

**Veredicto:** Aprobado / Aprobado con cambios menores / Necesita cambios

**Ítems del scoresheet:** P.. ✅ · P.. ⚠️ (qué falta)

**Problemas encontrados**
1. [Bloqueante] …
2. [Menor] …

**Verificaciones hechas:** links abiertos, cálculos rehechos.
```

Bloqueante = pierde puntos en el scoresheet, viola un requisito o tiene un dato sin fuente. Si hay bloqueantes, el veredicto es "Necesita cambios".
