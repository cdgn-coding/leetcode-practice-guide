# Segmentación de Cadena

## Descripción

Dada una cadena `s` y un diccionario de cadenas `wordDict`, devuelve `true` si `s` puede segmentarse en una secuencia de palabras del diccionario separadas por espacios.

Ten en cuenta que la misma palabra del diccionario puede utilizarse varias veces en la segmentación.

## Ejemplos

### Ejemplo 1:

**Entrada:** s = "leetcode", wordDict = ["leet","code"]
**Salida:** true
**Explicación:** Devuelve true porque "leetcode" puede segmentarse como "leet code".

### Ejemplo 2:

**Entrada:** s = "applepenapple", wordDict = ["apple","pen"]
**Salida:** true
**Explicación:** Devuelve true porque "applepenapple" puede segmentarse como "apple pen apple".
Nota que se permite reutilizar las palabras del diccionario.

### Ejemplo 3:

**Entrada:** s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
**Salida:** false

## Restricciones

- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- `s` y `wordDict[i]` contienen solo letras minúsculas del alfabeto inglés.
- Todas las cadenas en `wordDict` son únicas.