# Aplanar un Árbol Binario a una "Lista Enlazada"

## Descripción

Dado el nodo raíz de un árbol binario, aplana el árbol en una "lista enlazada":

- La "lista enlazada" debe utilizar la misma clase `TreeNode`, donde el puntero del hijo derecho apunta al siguiente nodo en la lista y el puntero del hijo izquierdo siempre es nulo.
- El orden de los nodos en la "lista enlazada" debe coincidir con el recorrido pre-orden del árbol binario original.

## Ejemplos

### Ejemplo 1:

**Entrada:** raíz = [1,2,5,3,4,null,6]
**Salida:** [1,null,2,null,3,null,4,null,5,null,6]

### Ejemplo 2:

**Entrada:** raíz = []
**Salida:** []

### Ejemplo 3:

**Entrada:** raíz = [0]
**Salida:** [0]

## Restricciones

- El número de nodos en el árbol está en el rango [0, 2000].
- -100 ≤ Valor del nodo ≤ 100

## Desafío adicional

¿Puedes aplanar el árbol in situ (con un espacio adicional O(1))?