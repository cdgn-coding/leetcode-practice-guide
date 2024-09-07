# K-ésimo Elemento Más Pequeño en un Árbol Binario de Búsqueda

## Descripción

Dado el `nodo raíz` de un árbol binario de búsqueda y un entero `k`, devuelve el *`k`-ésimo valor más pequeño* (****indexado desde 1****) de todos los valores de los nodos en el árbol.

**Ejemplo 1:**

```mermaid
graph TD
    3((3)) --> 1((1))
    3 --> 4((4))
    1 --> N1[null]
    1 --> 2((2))
```

En este árbol, el elemento más pequeño es 1. Como estamos buscando el primer elemento más pequeño (k = 1), la respuesta es 1.

**Ejemplo 2:**

```mermaid
graph TD
    5((5)) --> 3((3))
    5 --> 6((6))
    3 --> 2((2))
    3 --> 4((4))
    2 --> 1((1))
    2 --> N1[null]
    6 --> N2[null]
    6 --> N3[null]
```

Si ordenamos los elementos de este árbol de menor a mayor, obtenemos: 1, 2, 3, 4, 5, 6. El tercer elemento más pequeño (k = 3) es 3.
