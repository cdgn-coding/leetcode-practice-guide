# Índices de Subcadenas Concatenadas

## Descripción

Se te proporciona una cadena `s` y un arreglo de cadenas `words`. Todas las cadenas en `words` tienen la misma longitud.

Una cadena concatenada es aquella que contiene exactamente todas las cadenas de cualquier permutación de `words` unidas.

Por ejemplo, si `words = ["ab","cd","ef"]`, entonces "abcdef", "abefcd", "cdabef", "cdefab", "efabcd" y "efcdab" son todas cadenas concatenadas. "acdbef" no es una cadena concatenada porque no es la unión de ninguna permutación de `words`.

Tu tarea es devolver un arreglo con los índices iniciales de todas las subcadenas concatenadas en `s`. Puedes devolver la respuesta en cualquier orden.

## Ejemplos

### Ejemplo 1:

**Entrada:** s = "barfoothefoobarman", words = ["foo","bar"]

**Salida:** [0,9]

**Explicación:**
- La subcadena que comienza en 0 es "barfoo". Es la concatenación de ["bar","foo"], que es una permutación de `words`.
- La subcadena que comienza en 9 es "foobar". Es la concatenación de ["foo","bar"], que es una permutación de `words`.

### Ejemplo 2:

**Entrada:** s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

**Salida:** []

**Explicación:** No hay subcadenas concatenadas.

### Ejemplo 3:

**Entrada:** s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

**Salida:** [6,9,12]

**Explicación:**
- La subcadena que comienza en 6 es "foobarthe". Es la concatenación de ["foo","bar","the"].
- La subcadena que comienza en 9 es "barthefoo". Es la concatenación de ["bar","the","foo"].
- La subcadena que comienza en 12 es "thefoobar". Es la concatenación de ["the","foo","bar"].

## Restricciones

- 1 <= s.length <= 10^4
- 1 <= words.length <= 5000
- 1 <= words[i].length <= 30
- Tanto `s` como `words[i]` consisten en letras minúsculas del alfabeto inglés.