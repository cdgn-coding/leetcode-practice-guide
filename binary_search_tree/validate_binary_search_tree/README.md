# Árbol Binario de Búsqueda Válido

## Descripción

Dado el nodo raíz de un árbol binario, determina si es un árbol binario de búsqueda (ABB) válido.

Un ABB válido se define de la siguiente manera:

- El subárbol izquierdo de un nodo contiene solo nodos con claves menores que la clave del nodo.
- El subárbol derecho de un nodo contiene solo nodos con claves mayores que la clave del nodo.
- Tanto el subárbol izquierdo como el derecho también deben ser árboles binarios de búsqueda.

## Ejemplos

### Ejemplo 1:

**Entrada:** raíz = [2,1,3]
**Salida:** verdadero

### Ejemplo 2:

**Entrada:** raíz = [5,1,4,null,null,3,6]
**Salida:** falso
**Explicación:** El valor del nodo raíz es 5, pero el valor de su hijo derecho es 4.

## Restricciones

- El número de nodos en el árbol está en el rango [1, 10^4].
- -2^31 <= valor del nodo <= 2^31 - 1