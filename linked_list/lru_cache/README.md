# Caché de Uso Menos Reciente (LRU)

## Descripción

Diseña una estructura de datos que cumpla con las restricciones de una caché de Uso Menos Reciente (LRU, por sus siglas en inglés).

Implementa la clase `LRUCache` con las siguientes operaciones:

- `LRUCache(int capacidad)`: Inicializa la caché LRU con una capacidad positiva.
- `int get(int clave)`: Devuelve el valor asociado a la clave si existe, de lo contrario retorna -1.
- `void put(int clave, int valor)`: Actualiza el valor de la clave si esta existe. En caso contrario, añade el par clave-valor a la caché. Si el número de claves excede la capacidad debido a esta operación, elimina la clave usada menos recientemente.

Las funciones `get` y `put` deben ejecutarse con una complejidad temporal promedio de O(1).

## Ejemplo

```
Entrada:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

Salida:
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explicación:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1);  // la caché es {1=1}
lRUCache.put(2, 2);  // la caché es {1=1, 2=2}
lRUCache.get(1);     // devuelve 1
lRUCache.put(3, 3);  // la clave LRU era 2, se elimina la clave 2, la caché es {1=1, 3=3}
lRUCache.get(2);     // devuelve -1 (no encontrado)
lRUCache.put(4, 4);  // la clave LRU era 1, se elimina la clave 1, la caché es {4=4, 3=3}
lRUCache.get(1);     // devuelve -1 (no encontrado)
lRUCache.get(3);     // devuelve 3
lRUCache.get(4);     // devuelve 4
```

## Restricciones

- 1 <= capacidad <= 3000
- 0 <= clave <= 10^4
- 0 <= valor <= 10^5
- Se realizarán como máximo 2 * 10^5 llamadas a las funciones get y put.