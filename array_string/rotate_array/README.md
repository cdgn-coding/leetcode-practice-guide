# Rotar un Array

## Descripción

Dado un array de enteros `nums`, rota el array hacia la derecha `k` pasos, donde `k` es no negativo.

## Ejemplos

### Ejemplo 1

**Entrada:** nums = [1,2,3,4,5,6,7], k = 3
**Salida:** [5,6,7,1,2,3,4]
**Explicación:**
- Rotar 1 paso a la derecha: [7,1,2,3,4,5,6]
- Rotar 2 pasos a la derecha: [6,7,1,2,3,4,5]
- Rotar 3 pasos a la derecha: [5,6,7,1,2,3,4]

### Ejemplo 2

**Entrada:** nums = [-1,-100,3,99], k = 2
**Salida:** [3,99,-1,-100]
**Explicación:**
- Rotar 1 paso a la derecha: [99,-1,-100,3]
- Rotar 2 pasos a la derecha: [3,99,-1,-100]

## Restricciones

- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- 0 <= k <= 10^5

## Seguimiento

Intenta encontrar tantas soluciones como puedas. Hay al menos tres formas diferentes de resolver este problema.
¿Podrías hacerlo in-place con O(1) de espacio extra?