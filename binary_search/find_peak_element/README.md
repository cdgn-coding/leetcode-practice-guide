# Elemento Pico

## Descripción

Un elemento pico es aquel que es estrictamente mayor que sus vecinos.

Dado un arreglo de enteros `nums` indexado desde 0, encuentra un elemento pico y devuelve su índice. Si el arreglo contiene múltiples picos, devuelve el índice de cualquiera de ellos.

Puedes imaginar que `nums[-1] = nums[n] = -∞`. En otras palabras, un elemento siempre se considera estrictamente mayor que un vecino que está fuera del arreglo.

Debes escribir un algoritmo que se ejecute en tiempo O(log n).

## Ejemplos

### Ejemplo 1:

**Entrada:** nums = [1,2,3,1]
**Salida:** 2
**Explicación:** 3 es un elemento pico y tu función debe devolver el índice 2.

### Ejemplo 2:

**Entrada:** nums = [1,2,1,3,5,6,4]
**Salida:** 5
**Explicación:** Tu función puede devolver el índice 1 donde el elemento pico es 2, o el índice 5 donde el elemento pico es 6.

## Restricciones

- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
- nums[i] != nums[i + 1] para todo i válido.