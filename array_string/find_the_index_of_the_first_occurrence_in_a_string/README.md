# Encontrar el Índice de la Primera Aparición de una Subcadena

## Descripción

Dadas dos cadenas `needle` (aguja) y `haystack` (pajar), devuelve el índice de la primera aparición de `needle` en `haystack`, o `-1` si `needle` no es parte de `haystack`.

## Ejemplos

### Ejemplo 1:

- Entrada:
  - `haystack = "sadbutsad"`
  - `needle = "sad"`
- Salida: `0`
- Explicación: "sad" aparece en los índices 0 y 6. La primera aparición está en el índice 0, por lo que devolvemos 0.

### Ejemplo 2:

- Entrada:
  - `haystack = "leetcode"`
  - `needle = "leeto"`
- Salida: `-1`
- Explicación: "leeto" no aparece en "leetcode", por lo que devolvemos -1.

## Restricciones

- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` y `needle` consisten únicamente en caracteres en minúscula del alfabeto inglés.