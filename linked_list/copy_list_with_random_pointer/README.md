# Copia Profunda de Lista Enlazada con Puntero Aleatorio

## Descripción del Problema

Se te proporciona una lista enlazada de longitud n donde cada nodo contiene un puntero aleatorio adicional, que puede apuntar a cualquier nodo de la lista o ser nulo.

Tu tarea es construir una copia profunda de esta lista. La copia profunda debe consistir en exactamente n nodos nuevos, donde cada nuevo nodo tiene su valor establecido al valor de su nodo correspondiente en la lista original. Tanto el puntero "siguiente" como el puntero "aleatorio" de los nuevos nodos deben apuntar a nodos nuevos en la lista copiada, de manera que los punteros en la lista original y en la lista copiada representen el mismo estado de la lista. Ninguno de los punteros en la nueva lista debe apuntar a nodos de la lista original.

Por ejemplo, si hay dos nodos X e Y en la lista original, donde X.aleatorio --> Y, entonces para los dos nodos correspondientes x e y en la lista copiada, x.aleatorio --> y.

Debes devolver la cabeza de la lista enlazada copiada.

La lista enlazada se representa en la entrada/salida como una lista de n nodos. Cada nodo se representa como un par [val, índice_aleatorio] donde:

- val: un entero que representa Node.val
- índice_aleatorio: el índice del nodo (rango de 0 a n-1) al que apunta el puntero aleatorio, o null si no apunta a ningún nodo.

Tu código solo recibirá la cabeza de la lista enlazada original.

## Ejemplos

### Ejemplo 1:

**Entrada:** head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
**Salida:** [[7,null],[13,0],[11,4],[10,2],[1,0]]

### Ejemplo 2:

**Entrada:** head = [[1,1],[2,1]]
**Salida:** [[1,1],[2,1]]

### Ejemplo 3:

**Entrada:** head = [[3,null],[3,0],[3,null]]
**Salida:** [[3,null],[3,0],[3,null]]

## Restricciones

- 0 <= n <= 1000
- -10^4 <= Node.val <= 10^4
- Node.random es null o apunta a algún nodo en la lista enlazada.