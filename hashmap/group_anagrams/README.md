# Agrupación de Anagramas

## Descripción

Dado un arreglo de cadenas `strs`, agrupa los anagramas juntos. Puedes devolver la respuesta en cualquier orden.

Un anagrama es una palabra o frase formada al reorganizar las letras de otra palabra o frase, utilizando todas las letras originales exactamente una vez.

## Ejemplos

### Ejemplo 1:

**Entrada:** strs = ["eat","tea","tan","ate","nat","bat"]

**Salida:** [["bat"],["nat","tan"],["ate","eat","tea"]]

**Explicación:**
- No hay ninguna cadena en strs que pueda ser reorganizada para formar "bat".
- Las cadenas "nat" y "tan" son anagramas ya que pueden ser reorganizadas para formar una a la otra.
- Las cadenas "ate", "eat" y "tea" son anagramas ya que pueden ser reorganizadas para formar una a la otra.

### Ejemplo 2:

**Entrada:** strs = [""]

**Salida:** [[""]]

### Ejemplo 3:

**Entrada:** strs = ["a"]

**Salida:** [["a"]]

## Restricciones

- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consiste en letras minúsculas del alfabeto inglés.