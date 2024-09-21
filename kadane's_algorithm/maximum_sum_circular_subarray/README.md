# Suma Máxima de Subarreglo Circular

## Descripción

Dado un arreglo circular de enteros `nums` de longitud `n`, devuelve la suma máxima posible de un subarreglo no vacío de `nums`.

Un arreglo circular significa que el final del arreglo se conecta con el principio. Formalmente, el siguiente elemento de `nums[i]` es `nums[(i + 1) % n]` y el elemento anterior de `nums[i]` es `nums[(i - 1 + n) % n]`.

Un subarreglo puede incluir cada elemento del búfer fijo `nums` como máximo una vez. Formalmente, para un subarreglo `nums[i], nums[i + 1], ..., nums[j]`, no existen `i <= k1, k2 <= j` con `k1 % n == k2 % n`.

## Ejemplos

### Ejemplo 1:

**Entrada:** nums = [1,-2,3,-2]
**Salida:** 3
**Explicación:** El subarreglo [3] tiene la suma máxima de 3.

### Ejemplo 2:

**Entrada:** nums = [5,-3,5]
**Salida:** 10
**Explicación:** El subarreglo [5,5] tiene la suma máxima de 5 + 5 = 10.

### Ejemplo 3:

**Entrada:** nums = [-3,-2,-3]
**Salida:** -2
**Explicación:** El subarreglo [-2] tiene la suma máxima de -2.

## Restricciones

- n == nums.length
- 1 <= n <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4