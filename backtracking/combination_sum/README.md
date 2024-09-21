# Combinaciones de Suma

## Descripción

Dado un array de enteros distintos llamado `candidates` y un entero objetivo `target`, devuelve una lista de todas las combinaciones únicas de `candidates` cuya suma sea igual a `target`. Puedes devolver las combinaciones en cualquier orden.

El mismo número puede ser elegido de `candidates` un número ilimitado de veces. Dos combinaciones se consideran únicas si la frecuencia de al menos uno de los números elegidos es diferente.

Los casos de prueba están generados de tal manera que el número de combinaciones únicas que suman `target` es menor a 150 para los datos de entrada dados.

## Ejemplos

### Ejemplo 1:

**Entrada:** candidates = [2,3,6,7], target = 7
**Salida:** [[2,2,3],[7]]
**Explicación:**
2 y 3 son candidatos, y 2 + 2 + 3 = 7. Ten en cuenta que 2 puede usarse varias veces.
7 es un candidato, y 7 = 7.
Estas son las únicas dos combinaciones posibles.

### Ejemplo 2:

**Entrada:** candidates = [2,3,5], target = 8
**Salida:** [[2,2,2,2],[2,3,3],[3,5]]

### Ejemplo 3:

**Entrada:** candidates = [2], target = 1
**Salida:** []

## Restricciones

- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- Todos los elementos de candidates son distintos.
- 1 <= target <= 40