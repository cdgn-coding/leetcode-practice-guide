# Longitud de la Subsecuencia Creciente más Larga

## Descripción

Dado un arreglo de enteros `nums`, devuelve la longitud de la subsecuencia creciente más larga.

Una subsecuencia es una secuencia que se puede derivar del arreglo original eliminando algunos elementos (o ninguno) sin cambiar el orden de los elementos restantes. Una secuencia se considera estrictamente creciente si cada elemento es mayor que el anterior.

## Ejemplos

### Ejemplo 1:

**Entrada:** nums = [10,9,2,5,3,7,101,18]
**Salida:** 4
**Explicación:** La subsecuencia creciente más larga es [2,3,7,101], por lo tanto, la longitud es 4.

### Ejemplo 2:

**Entrada:** nums = [0,1,0,3,2,3]
**Salida:** 4

### Ejemplo 3:

**Entrada:** nums = [7,7,7,7,7,7,7]
**Salida:** 1

## Restricciones

- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4

## Desafío adicional

¿Puedes desarrollar un algoritmo que se ejecute con una complejidad temporal de O(n log(n))?