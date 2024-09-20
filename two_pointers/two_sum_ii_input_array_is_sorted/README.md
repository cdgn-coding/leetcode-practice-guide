# Suma de Dos Números en un Arreglo Ordenado

## Descripción

Dado un arreglo de enteros `numbers` indexado desde 1, que ya está ordenado de forma no decreciente, encuentra dos números que sumen un valor objetivo específico. Estos dos números deben ser `numbers[index1]` y `numbers[index2]`, donde 1 ≤ index1 < index2 ≤ numbers.length.

Devuelve los índices de los dos números, index1 e index2, incrementados en 1, como un arreglo de enteros `[index1, index2]` de longitud 2.

Las pruebas están generadas de tal manera que existe exactamente una solución. No puedes usar el mismo elemento dos veces.

Tu solución debe utilizar solo espacio extra constante.

## Ejemplos

### Ejemplo 1:

**Entrada:** numbers = [2,7,11,15], target = 9
**Salida:** [1,2]
**Explicación:** La suma de 2 y 7 es 9. Por lo tanto, index1 = 1, index2 = 2. Devolvemos [1, 2].

### Ejemplo 2:

**Entrada:** numbers = [2,3,4], target = 6
**Salida:** [1,3]
**Explicación:** La suma de 2 y 4 es 6. Por lo tanto, index1 = 1, index2 = 3. Devolvemos [1, 3].

### Ejemplo 3:

**Entrada:** numbers = [-1,0], target = -1
**Salida:** [1,2]
**Explicación:** La suma de -1 y 0 es -1. Por lo tanto, index1 = 1, index2 = 2. Devolvemos [1, 2].

## Restricciones

- 2 ≤ numbers.length ≤ 3 * 10^4
- -1000 ≤ numbers[i] ≤ 1000
- numbers está ordenado en forma no decreciente.
- -1000 ≤ target ≤ 1000
- Las pruebas están generadas de tal manera que existe exactamente una solución.