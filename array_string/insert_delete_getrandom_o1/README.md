# Conjunto Aleatorio

## Descripción

Implementa la clase `RandomizedSet` que soporta las siguientes operaciones:

- `RandomizedSet()`: Inicializa el objeto RandomizedSet.
- `bool insert(int val)`: Inserta un elemento `val` en el conjunto si no está presente. Retorna `true` si el elemento no estaba presente, `false` en caso contrario.
- `bool remove(int val)`: Elimina un elemento `val` del conjunto si está presente. Retorna `true` si el elemento estaba presente, `false` en caso contrario.
- `int getRandom()`: Retorna un elemento aleatorio del conjunto actual de elementos (se garantiza que al menos un elemento existe cuando se llama a este método). Cada elemento debe tener la misma probabilidad de ser retornado.

Debes implementar las funciones de la clase de tal manera que cada función tenga una complejidad de tiempo promedio de O(1).

## Ejemplos

```
Entrada:
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]

Salida:
[null, true, false, true, 2, true, false, 2]

Explicación:
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserta 1 en el conjunto. Retorna true ya que 1 se insertó exitosamente.
randomizedSet.remove(2); // Retorna false ya que 2 no existe en el conjunto.
randomizedSet.insert(2); // Inserta 2 en el conjunto, retorna true. El conjunto ahora contiene [1,2].
randomizedSet.getRandom(); // getRandom() debe retornar 1 o 2 aleatoriamente.
randomizedSet.remove(1); // Elimina 1 del conjunto, retorna true. El conjunto ahora contiene [2].
randomizedSet.insert(2); // 2 ya estaba en el conjunto, por lo que retorna false.
randomizedSet.getRandom(); // Como 2 es el único número en el conjunto, getRandom() siempre retornará 2.
```

## Restricciones

- -2^31 <= val <= 2^31 - 1
- Se realizarán como máximo 2 * 10^5 llamadas a `insert`, `remove` y `getRandom`.
- Habrá al menos un elemento en la estructura de datos cuando se llame a `getRandom`.