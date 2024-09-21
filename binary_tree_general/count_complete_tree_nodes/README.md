# Contar Nodos en un Árbol Binario Completo

## Descripción

Dado el nodo raíz de un árbol binario completo, devuelve el número total de nodos en el árbol.

Según Wikipedia, en un árbol binario completo, todos los niveles, excepto posiblemente el último, están completamente llenos. Además, todos los nodos en el último nivel están lo más a la izquierda posible. El último nivel h puede tener entre 1 y 2^h nodos, inclusive.

Diseña un algoritmo que se ejecute en un tiempo inferior a O(n), donde n es el número total de nodos.

## Ejemplos

### Ejemplo 1:

**Entrada:** raíz = [1,2,3,4,5,6]
**Salida:** 6

### Ejemplo 2:

**Entrada:** raíz = []
**Salida:** 0

### Ejemplo 3:

**Entrada:** raíz = [1]
**Salida:** 1

## Restricciones

- El número de nodos en el árbol está en el rango [0, 5 * 10^4].
- El valor de cada nodo está entre 0 y 5 * 10^4, inclusive.
- Se garantiza que el árbol es completo.

## Nota

Este problema requiere implementar una solución eficiente que aproveche las propiedades de un árbol binario completo para lograr un tiempo de ejecución menor que O(n).