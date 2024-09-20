# Subarreglo Mínimo con Suma Mayor o Igual al Objetivo

## Descripción

Dado un arreglo de enteros positivos `nums` y un entero positivo `target`, encuentra la longitud mínima de un subarreglo cuya suma sea mayor o igual a `target`. Si no existe tal subarreglo, devuelve 0.

## Ejemplos

### Ejemplo 1:

**Entrada:** target = 7, nums = [2,3,1,2,4,3]
**Salida:** 2
**Explicación:** El subarreglo [4,3] tiene la longitud mínima que cumple con la condición del problema.

### Ejemplo 2:

**Entrada:** target = 4, nums = [1,4,4]
**Salida:** 1

### Ejemplo 3:

**Entrada:** target = 11, nums = [1,1,1,1,1,1,1,1]
**Salida:** 0

## Restricciones

- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4

## Desafío adicional

Si has logrado implementar la solución con complejidad O(n), intenta desarrollar otra solución con complejidad temporal O(n log(n)).