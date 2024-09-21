# Búsqueda en un Array Rotado Ordenado

## Descripción

Se te proporciona un array de enteros `nums` ordenado de forma ascendente (con valores distintos).

Antes de ser pasado a tu función, `nums` puede haber sido rotado en un índice pivote desconocido `k` (1 <= k < nums.length), de tal manera que el array resultante es [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (indexado desde 0). Por ejemplo, [0,1,2,4,5,6,7] podría ser rotado en el índice pivote 3 y convertirse en [4,5,6,7,0,1,2].

Dado el array `nums` después de la posible rotación y un entero `target`, devuelve el índice de `target` si está en `nums`, o -1 si no está en `nums`.

Debes escribir un algoritmo con una complejidad de tiempo de O(log n).

## Ejemplos

### Ejemplo 1:

**Entrada:** nums = [4,5,6,7,0,1,2], target = 0
**Salida:** 4

### Ejemplo 2:

**Entrada:** nums = [4,5,6,7,0,1,2], target = 3
**Salida:** -1

### Ejemplo 3:

**Entrada:** nums = [1], target = 0
**Salida:** -1

## Restricciones

- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- Todos los valores en nums son únicos.
- nums es un array ascendente que posiblemente ha sido rotado.
- -10^4 <= target <= 10^4