# Combinaciones

## Descripción

Dados dos números enteros `n` y `k`, devuelve todas las posibles combinaciones de `k` números elegidos del rango [1, n].

Puedes devolver la respuesta en cualquier orden.

## Ejemplos

### Ejemplo 1:

**Entrada:** n = 4, k = 2
**Salida:** [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
**Explicación:** Hay 4 elegir 2 = 6 combinaciones en total.
Nota: Las combinaciones no tienen orden, es decir, [1,2] y [2,1] se consideran la misma combinación.

### Ejemplo 2:

**Entrada:** n = 1, k = 1
**Salida:** [[1]]
**Explicación:** Hay 1 elegir 1 = 1 combinación en total.

## Restricciones

- 1 <= n <= 20
- 1 <= k <= n