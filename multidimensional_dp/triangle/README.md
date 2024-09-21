# Suma del Camino Mínimo en un Triángulo

## Descripción

Dado un arreglo en forma de triángulo, calcula la suma mínima del camino desde la cima hasta la base.

En cada paso, puedes moverte a un número adyacente en la fila inferior. Más específicamente, si estás en el índice i de la fila actual, puedes moverte al índice i o al índice i + 1 de la siguiente fila.

## Ejemplos

### Ejemplo 1:

**Entrada:** triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
**Salida:** 11
**Explicación:** El triángulo se ve así:
```
   2
  3 4
 6 5 7
4 1 8 3
```
La suma mínima del camino desde la cima hasta la base es 2 + 3 + 5 + 1 = 11 (subrayado arriba).

### Ejemplo 2:

**Entrada:** triangle = [[-10]]
**Salida:** -10

## Restricciones

- 1 <= triangle.length <= 200
- triangle[0].length == 1
- triangle[i].length == triangle[i - 1].length + 1
- -10^4 <= triangle[i][j] <= 10^4

## Desafío adicional

¿Podrías resolver este problema utilizando solo O(n) de espacio adicional, donde n es el número total de filas en el triángulo?