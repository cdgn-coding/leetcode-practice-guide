# Implementación de un Trie (Árbol de Prefijos)

## Descripción

Un trie (pronunciado como "trai") o árbol de prefijos es una estructura de datos en forma de árbol utilizada para almacenar y recuperar eficientemente claves en un conjunto de cadenas. Esta estructura de datos tiene diversas aplicaciones, como el autocompletado y la corrección ortográfica.

Implementa la clase Trie con las siguientes funciones:

- `Trie()`: Inicializa el objeto trie.
- `void insert(String palabra)`: Inserta la cadena `palabra` en el trie.
- `boolean search(String palabra)`: Devuelve `true` si la cadena `palabra` está en el trie (es decir, si se insertó previamente), y `false` en caso contrario.
- `boolean startsWith(String prefijo)`: Devuelve `true` si existe una cadena previamente insertada que tiene el prefijo `prefijo`, y `false` en caso contrario.

## Ejemplo

### Entrada
```
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
```

### Salida
```
[null, null, true, false, true, null, true]
```

### Explicación
```
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // devuelve True
trie.search("app");     // devuelve False
trie.startsWith("app"); // devuelve True
trie.insert("app");
trie.search("app");     // devuelve True
```

## Restricciones

- 1 <= longitud de palabra, longitud de prefijo <= 2000
- `palabra` y `prefijo` contienen solo letras minúsculas del alfabeto inglés.
- Se realizarán como máximo 3 * 10^4 llamadas en total a las funciones insert, search y startsWith.