# Pila con Mínimo

## Descripción

Diseña una pila que admita las operaciones de inserción (push), extracción (pop), obtener el elemento superior (top) y recuperar el elemento mínimo, todas en tiempo constante.

Implementa la clase `MinStack` con los siguientes métodos:

- `MinStack()`: Inicializa el objeto de la pila.
- `void push(int val)`: Inserta el elemento `val` en la parte superior de la pila.
- `void pop()`: Elimina el elemento en la parte superior de la pila.
- `int top()`: Obtiene el elemento superior de la pila.
- `int getMin()`: Recupera el elemento mínimo de la pila.

Debes implementar una solución con complejidad temporal O(1) para cada función.

## Ejemplo

```
Entrada
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Salida
[null,null,null,null,-3,null,0,-2]

Explicación
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // devuelve -3
minStack.pop();
minStack.top();    // devuelve 0
minStack.getMin(); // devuelve -2
```

## Restricciones

- -2^31 <= val <= 2^31 - 1
- Los métodos pop, top y getMin siempre serán llamados en pilas no vacías.
- Se realizarán como máximo 3 * 10^4 llamadas en total a push, pop, top y getMin.