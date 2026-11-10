# Sensores

**Persona:** P3 · **Responsable:** Tabarez (según la Guía) · **Pestaña de la Guía:** 5 · revisores en `.github/CODEOWNERS`

## Alcance

Presión, temperatura, tensión y corriente de batería, GNSS, aceleración, rotación y las dos cámaras.

- Requisitos del Anexo A: SN1–SN8, C6, C7
- Diapositivas de la plantilla PDR: 15–31
- Ítems del scoresheet: filas con subsistema `sensores` en [`pdr/trazabilidad.md`](../../pdr/trazabilidad.md)

## Estructura

- `trades/`: una comparativa por archivo (`AAAA-MM-DD-tema.md`)
- `figuras/`: imágenes para el PDR (PNG/SVG)
- `masa.yaml`: masa de los componentes de este subsistema
- `ESTADO.md`: qué está hecho, qué falta, qué está bloqueado

## Documentos

- [`guia-05-sensores.md`](guia-05-sensores.md): pestaña de la Guía de desarrollo con el formato Qué pide / Qué hay que entender / Opciones / Decisión / Pendientes
