# Búsqueda por Inserción

## Descripción

Dado un arreglo ordenado de enteros distintos y un valor objetivo, devuelve el índice si se encuentra el objetivo. Si no, devuelve el índice donde debería insertarse para mantener el orden.

Debes implementar un algoritmo con una complejidad temporal de O(log n).

## Ejemplos

### Ejemplo 1:

**Entrada:** nums = [1,3,5,6], objetivo = 5
**Salida:** 2

### Ejemplo 2:

**Entrada:** nums = [1,3,5,6], objetivo = 2
**Salida:** 1

### Ejemplo 3:

**Entrada:** nums = [1,3,5,6], objetivo = 7
**Salida:** 4

## Restricciones

- 1 ≤ longitud de nums ≤ 10^4
- -10^4 ≤ nums[i] ≤ 10^4
- nums contiene valores distintos ordenados de forma ascendente.
- -10^4 ≤ objetivo ≤ 10^4