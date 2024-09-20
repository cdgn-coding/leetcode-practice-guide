# Justificación de Texto

## Descripción

Dado un arreglo de cadenas `words` y un ancho máximo `maxWidth`, formatea el texto de manera que cada línea tenga exactamente `maxWidth` caracteres y esté completamente justificada (alineada a la izquierda y a la derecha).

Debes empaquetar las palabras utilizando un enfoque codicioso, es decir, empaquetar tantas palabras como puedas en cada línea. Agrega espacios adicionales `' '` cuando sea necesario para que cada línea tenga exactamente `maxWidth` caracteres.

Los espacios adicionales entre palabras deben distribuirse lo más uniformemente posible. Si el número de espacios en una línea no se divide equitativamente entre las palabras, los espacios vacíos a la izquierda tendrán más espacios que los espacios a la derecha.

Para la última línea del texto, debe estar alineada a la izquierda y no se deben insertar espacios adicionales entre las palabras.

## Ejemplos

### Ejemplo 1

- Entrada: 
  - `words = ["This", "is", "an", "example", "of", "text", "justification."]`
  - `maxWidth = 16`
- Salida:
```
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

### Ejemplo 2

- Entrada:
  - `words = ["What","must","be","acknowledgment","shall","be"]`
  - `maxWidth = 16`
- Salida:
```
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
```
Explicación: Ten en cuenta que la última línea es "shall be    " en lugar de "shall     be", porque la última línea debe estar alineada a la izquierda en lugar de estar completamente justificada.
Nota que la segunda línea también está alineada a la izquierda porque contiene solo una palabra.

### Ejemplo 3

- Entrada:
  - `words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]`
  - `maxWidth = 20`
- Salida:
```
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
```

## Restricciones

- `1 <= words.length <= 300`
- `1 <= words[i].length <= 20`
- `words[i]` consiste solo en letras y símbolos en inglés.
- `1 <= maxWidth <= 100`
- `words[i].length <= maxWidth`