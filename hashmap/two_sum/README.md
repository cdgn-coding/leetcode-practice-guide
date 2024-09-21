# Suma de Dos Números

## Descripción

Dado un arreglo de números enteros `nums` y un entero `target`, devuelve los índices de los dos números que suman `target`.

Puedes asumir que cada entrada tendrá exactamente una solución, y no puedes usar el mismo elemento dos veces.

Puedes devolver la respuesta en cualquier orden.

## Ejemplos

### Ejemplo 1:

**Entrada:** nums = [2,7,11,15], target = 9
**Salida:** [0,1]
**Explicación:** Como nums[0] + nums[1] == 9, devolvemos [0, 1].

### Ejemplo 2:

**Entrada:** nums = [3,2,4], target = 6
**Salida:** [1,2]

### Ejemplo 3:

**Entrada:** nums = [3,3], target = 6
**Salida:** [0,1]

## Restricciones

- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Solo existe una respuesta válida.

## Desafío adicional

¿Puedes proponer un algoritmo con una complejidad temporal menor a O(n^2)?