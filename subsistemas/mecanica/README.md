# Mecánica y estructura

**Persona:** P2 · **Responsable:** Joaquín Sánchez · **Pestaña de la Guía:** 3 · revisores en `.github/CODEOWNERS`

## Alcance

Estructura, materiales, fijación, mecanismo de liberación, accesos, interfaz con el cohete y presupuesto de masa.

- Requisitos del Anexo A: S1–S9, M1–M4, C1, C2, E5 (asignación de la Guía §1.3)
- Diapositivas de la plantilla PDR: 9–12, 14 y 37–46
- Ítems del scoresheet: filas con subsistema `mecanica` en [`pdr/trazabilidad.md`](../../pdr/trazabilidad.md)

## Estructura

- `trades/`: una comparativa por archivo (`AAAA-MM-DD-tema.md`)
- `figuras/`: imágenes para el PDR (PNG/SVG)
- `cad/`: exportaciones STEP/STL
- `masa.yaml`: masa de los componentes de este subsistema
- `ESTADO.md`: qué está hecho, qué falta, qué está bloqueado

## Documentos

- [`guia-03-mecanica.md`](guia-03-mecanica.md): pestaña de la Guía de desarrollo con el formato Qué pide / Qué hay que entender / Opciones / Decisión / Pendientes
- [`seccion-2-mecanica.md`](seccion-2-mecanica.md): investigación completa de la Sección 2 (documento del 2/11/2026)
