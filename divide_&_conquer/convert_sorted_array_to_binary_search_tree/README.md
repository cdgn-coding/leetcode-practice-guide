# Convertir Array Ordenado a Árbol Binario de Búsqueda Equilibrado

## Descripción

Dado un array de enteros `nums` donde los elementos están ordenados de forma ascendente, conviértelo en un árbol binario de búsqueda equilibrado en altura.

## Ejemplos

### Ejemplo 1:

**Entrada:** nums = [-10,-3,0,5,9]
**Salida:** [0,-3,9,-10,null,5]
**Explicación:** [0,-10,5,null,-3,null,9] también es una solución válida:

![Ejemplo 1](https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg)

### Ejemplo 2:

**Entrada:** nums = [1,3]
**Salida:** [3,1]
**Explicación:** Tanto [1,null,3] como [3,1] son árboles binarios de búsqueda equilibrados en altura.

![Ejemplo 2](https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg)

## Restricciones

- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums está ordenado en orden estrictamente creciente.