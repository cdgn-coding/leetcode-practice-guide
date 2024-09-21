# Fusión de Intervalos

## Descripción

Dado un arreglo de intervalos donde `intervals[i] = [inicio_i, fin_i]`, combina todos los intervalos superpuestos y devuelve un arreglo de los intervalos no superpuestos que cubran todos los intervalos de la entrada.

## Ejemplos

### Ejemplo 1:

**Entrada:** intervals = [[1,3],[2,6],[8,10],[15,18]]
**Salida:** [[1,6],[8,10],[15,18]]
**Explicación:** Como los intervalos [1,3] y [2,6] se superponen, se combinan en [1,6].

### Ejemplo 2:

**Entrada:** intervals = [[1,4],[4,5]]
**Salida:** [[1,5]]
**Explicación:** Los intervalos [1,4] y [4,5] se consideran superpuestos.

## Restricciones

- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= inicio_i <= fin_i <= 10^4