# Clonar Grafo

## Descripción

Se te proporciona una referencia a un nodo en un grafo no dirigido y conectado.

Tu tarea es devolver una copia profunda (clon) del grafo.

Cada nodo en el grafo contiene un valor (entero) y una lista de sus vecinos.

```python
class Nodo:
    def __init__(self, val = 0, vecinos = None):
        self.val = val
        self.vecinos = vecinos if vecinos is not None else []
```

## Formato del caso de prueba

Para simplificar, el valor de cada nodo es igual al índice del nodo (empezando desde 1). Por ejemplo, el primer nodo tiene val == 1, el segundo nodo tiene val == 2, y así sucesivamente. El grafo se representa en el caso de prueba utilizando una lista de adyacencia.

Una lista de adyacencia es una colección de listas no ordenadas utilizada para representar un grafo finito. Cada lista describe el conjunto de vecinos de un nodo en el grafo.

El nodo dado siempre será el primer nodo con val = 1. Debes devolver la copia del nodo dado como referencia al grafo clonado.

## Ejemplos

### Ejemplo 1:

**Entrada:** listaAdyacencia = [[2,4],[1,3],[2,4],[1,3]]
**Salida:** [[2,4],[1,3],[2,4],[1,3]]
**Explicación:** Hay 4 nodos en el grafo.
- Los vecinos del 1er nodo (val = 1) son el 2º nodo (val = 2) y el 4º nodo (val = 4).
- Los vecinos del 2º nodo (val = 2) son el 1er nodo (val = 1) y el 3er nodo (val = 3).
- Los vecinos del 3er nodo (val = 3) son el 2º nodo (val = 2) y el 4º nodo (val = 4).
- Los vecinos del 4º nodo (val = 4) son el 1er nodo (val = 1) y el 3er nodo (val = 3).

### Ejemplo 2:

**Entrada:** listaAdyacencia = [[]]
**Salida:** [[]]
**Explicación:** La entrada contiene una lista vacía. El grafo consiste en un solo nodo con val = 1 y no tiene vecinos.

### Ejemplo 3:

**Entrada:** listaAdyacencia = []
**Salida:** []
**Explicación:** Este es un grafo vacío, no tiene ningún nodo.

## Restricciones

- El número de nodos en el grafo está en el rango [0, 100].
- 1 <= Nodo.val <= 100
- El valor de cada nodo (Nodo.val) es único.
- No hay aristas repetidas ni bucles en el grafo.
- El grafo está conectado y todos los nodos pueden ser visitados partiendo del nodo dado.