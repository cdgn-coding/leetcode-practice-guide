## Descripción

Dado el nodo raíz de un Árbol Binario de Búsqueda (BST), devuelve la diferencia absoluta mínima entre los valores de cualquier par de nodos diferentes en el árbol.

**Ejemplo 1:**

```mermaid
graph TD
    4((4)) --> 2((2))
    4 --> 6((6))
    2 --> 1((1))
    2 --> 3((3))
```

La diferencia mínima es 1

**Ejemplo 2:**

```mermaid
graph TD
    1((1)) --> 0((0))
    1 --> 48((48))
    48 --> 12((12))
    48 --> 49((49))
```

La diferencia mínima es 1