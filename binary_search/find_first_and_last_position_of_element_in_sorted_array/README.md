# Buscar rango de un elemento

## Descripción

Dado un arreglo de números enteros `nums` ordenado de forma no decreciente, encuentra las posiciones de inicio y fin de un valor objetivo dado.

Si el valor objetivo no se encuentra en el arreglo, devuelve [-1, -1].

Debes implementar un algoritmo con una complejidad temporal de O(log n).

## Ejemplos

### Ejemplo 1:

**Entrada:** nums = [5,7,7,8,8,10], objetivo = 8
**Salida:** [3,4]

### Ejemplo 2:

**Entrada:** nums = [5,7,7,8,8,10], objetivo = 6
**Salida:** [-1,-1]

### Ejemplo 3:

**Entrada:** nums = [], objetivo = 0
**Salida:** [-1,-1]

## Restricciones

- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- nums está ordenado de forma no decreciente
- -10^9 <= objetivo <= 10^9