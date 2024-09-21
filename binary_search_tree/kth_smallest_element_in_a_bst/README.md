# K-ésimo Elemento Más Pequeño en un BST

## Descripción

Dado el nodo raíz de un árbol binario de búsqueda (BST) y un número entero k, devuelve el k-ésimo valor más pequeño (considerando que el índice comienza en 1) de entre todos los valores de los nodos en el árbol.

## Ejemplos

### Ejemplo 1:

**Entrada:** raíz = [3,1,4,null,2], k = 1
**Salida:** 1

### Ejemplo 2:

**Entrada:** raíz = [5,3,6,2,4,null,null,1], k = 3
**Salida:** 3

## Restricciones

- El número de nodos en el árbol es n.
- 1 <= k <= n <= 10^4
- 0 <= Valor del Nodo <= 10^4

## Pregunta adicional

¿Cómo optimizarías la solución si el BST se modifica con frecuencia (es decir, si se realizan operaciones de inserción y eliminación) y necesitas encontrar el k-ésimo elemento más pequeño regularmente?