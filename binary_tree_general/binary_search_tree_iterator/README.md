# Iterador de Árbol Binario de Búsqueda

## Descripción

Implementa la clase `BSTIterator` que representa un iterador para el recorrido en orden de un árbol binario de búsqueda (BST):

- `BSTIterator(TreeNode root)`: Inicializa un objeto de la clase `BSTIterator`. La raíz del BST se proporciona como parte del constructor. El puntero debe inicializarse en un número no existente menor que cualquier elemento en el BST.
- `boolean hasNext()`: Devuelve `true` si existe un número en el recorrido a la derecha del puntero, de lo contrario devuelve `false`.
- `int next()`: Mueve el puntero a la derecha y luego devuelve el número en la posición del puntero.

Ten en cuenta que al inicializar el puntero en un número no existente menor que cualquier elemento, la primera llamada a `next()` devolverá el elemento más pequeño del BST.

Puedes asumir que las llamadas a `next()` siempre serán válidas. Es decir, siempre habrá un siguiente número en el recorrido en orden cuando se llame a `next()`.

## Ejemplo

### Entrada
```
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
```

### Salida
```
[null, 3, 7, true, 9, true, 15, true, 20, false]
```

### Explicación
```
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // devuelve 3
bSTIterator.next();    // devuelve 7
bSTIterator.hasNext(); // devuelve True
bSTIterator.next();    // devuelve 9
bSTIterator.hasNext(); // devuelve True
bSTIterator.next();    // devuelve 15
bSTIterator.hasNext(); // devuelve True
bSTIterator.next();    // devuelve 20
bSTIterator.hasNext(); // devuelve False
```

## Restricciones

- El número de nodos en el árbol está en el rango [1, 10^5].
- 0 <= Node.val <= 10^6
- Se realizarán como máximo 10^5 llamadas a `hasNext` y `next`.

## Desafío adicional

¿Podrías implementar `next()` y `hasNext()` para que se ejecuten en un tiempo promedio de O(1) y usen O(h) de memoria, donde h es la altura del árbol?