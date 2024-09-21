# Diseño de un Diccionario de Palabras

## Descripción

Diseña una estructura de datos que permita añadir nuevas palabras y buscar si una cadena coincide con alguna de las palabras previamente añadidas.

Implementa la clase `WordDictionary` con las siguientes funciones:

- `WordDictionary()`: Inicializa el objeto.
- `void addWord(word)`: Añade una palabra a la estructura de datos para futuras búsquedas.
- `bool search(word)`: Devuelve `true` si existe alguna cadena en la estructura que coincida con la palabra buscada, o `false` en caso contrario. La palabra puede contener puntos '.' que pueden coincidir con cualquier letra.

## Ejemplo

```
Entrada:
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

Salida:
[null,null,null,null,false,true,true,true]

Explicación:
WordDictionary diccionario = new WordDictionary();
diccionario.addWord("bad");
diccionario.addWord("dad");
diccionario.addWord("mad");
diccionario.search("pad"); // devuelve False
diccionario.search("bad"); // devuelve True
diccionario.search(".ad"); // devuelve True
diccionario.search("b.."); // devuelve True
```

## Restricciones

- 1 <= longitud de la palabra <= 25
- Las palabras añadidas con `addWord` consisten en letras minúsculas del alfabeto inglés.
- Las palabras buscadas con `search` consisten en '.' o letras minúsculas del alfabeto inglés.
- Habrá como máximo 2 puntos en la palabra para las consultas de búsqueda.
- Se realizarán como máximo 10^4 llamadas en total a `addWord` y `search`.