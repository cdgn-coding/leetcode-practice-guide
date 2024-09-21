# Matriz de Ceros

## Descripción

Dada una matriz de enteros `matrix` de dimensiones m x n, si un elemento es 0, establece toda su fila y columna a 0.

Debes realizar esta operación in situ (sin usar espacio adicional).

## Ejemplos

### Ejemplo 1:

**Entrada:** matrix = [[1,1,1],[1,0,1],[1,1,1]]
**Salida:** [[1,0,1],[0,0,0],[1,0,1]]

### Ejemplo 2:

**Entrada:** matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
**Salida:** [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

## Restricciones

- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2^31 <= matrix[i][j] <= 2^31 - 1

## Desafío adicional

Una solución directa que utilice O(mn) de espacio probablemente no sea la mejor idea.
Una mejora simple utiliza O(m + n) de espacio, pero aún no es la solución óptima.
¿Podrías idear una solución que use espacio constante?