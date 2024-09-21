# Conectar nodos del mismo nivel en un árbol binario

## Descripción

Dado un árbol binario con la siguiente estructura:

```cpp
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

Tu tarea es completar cada puntero `next` para que apunte al nodo de su derecha en el mismo nivel. Si no hay un nodo a la derecha, el puntero `next` debe establecerse como `NULL`.

Inicialmente, todos los punteros `next` están configurados como `NULL`.

## Ejemplos

### Ejemplo 1:

**Entrada:** root = [1,2,3,4,5,null,7]
**Salida:** [1,#,2,3,#,4,5,7,#]

**Explicación:** Dado el árbol binario de la Figura A, tu función debe completar cada puntero `next` para que apunte al nodo de su derecha, como se muestra en la Figura B. La salida serializada está en orden de nivel, conectada por los punteros `next`, con '#' indicando el final de cada nivel.

### Ejemplo 2:

**Entrada:** root = []
**Salida:** []

## Restricciones

- El número de nodos en el árbol está en el rango [0, 6000].
- -100 <= Node.val <= 100

## Desafío adicional

- Solo puedes usar espacio extra constante.
- El enfoque recursivo es válido. Puedes asumir que el espacio implícito de la pila no cuenta como espacio extra para este problema.