# Inserción de Intervalos

## Descripción

Se te proporciona un array de intervalos no superpuestos llamado `intervals`, donde `intervals[i] = [inicio_i, fin_i]` representa el inicio y el fin del i-ésimo intervalo. Los intervalos están ordenados de forma ascendente según su valor de inicio.

También se te da un nuevo intervalo `newInterval = [inicio, fin]` que representa el inicio y el fin de otro intervalo.

Tu tarea es insertar `newInterval` en `intervals` de manera que:
1. `intervals` siga ordenado de forma ascendente según el valor de inicio.
2. `intervals` no contenga intervalos superpuestos (fusiona los intervalos que se superpongan si es necesario).

Devuelve `intervals` después de realizar la inserción.

Nota: No es necesario modificar `intervals` in situ. Puedes crear un nuevo array y devolverlo.

## Ejemplos

### Ejemplo 1:

**Entrada:** intervals = [[1,3],[6,9]], newInterval = [2,5]
**Salida:** [[1,5],[6,9]]

### Ejemplo 2:

**Entrada:** intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
**Salida:** [[1,2],[3,10],[12,16]]
**Explicación:** El nuevo intervalo [4,8] se superpone con [3,5], [6,7] y [8,10].

## Restricciones

- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= inicio_i <= fin_i <= 10^5
- `intervals` está ordenado por inicio_i de forma ascendente.
- newInterval.length == 2
- 0 <= inicio <= fin <= 10^5