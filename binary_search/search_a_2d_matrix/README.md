# Búsqueda en Matriz Ordenada

## Descripción

Se te proporciona una matriz de enteros `matriz` de dimensiones m x n con las siguientes propiedades:

- Cada fila está ordenada de forma no decreciente.
- El primer entero de cada fila es mayor que el último entero de la fila anterior.

Dado un entero `objetivo`, devuelve `true` si el `objetivo` se encuentra en la `matriz` o `false` en caso contrario.

Debes escribir una solución con una complejidad temporal de O(log(m * n)).

## Ejemplos

### Ejemplo 1:

**Entrada:** 
```
matriz = [
  [1,3,5,7],
  [10,11,16,20],
  [23,30,34,60]
], 
objetivo = 3
```
**Salida:** true

### Ejemplo 2:

**Entrada:** 
```
matriz = [
  [1,3,5,7],
  [10,11,16,20],
  [23,30,34,60]
], 
objetivo = 13
```
**Salida:** false

## Restricciones

- m == matriz.length
- n == matriz[i].length
- 1 <= m, n <= 100
- -10^4 <= matriz[i][j], objetivo <= 10^4