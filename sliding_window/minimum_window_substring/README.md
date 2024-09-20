# Subcadena de Ventana Mínima

## Descripción

Dadas dos cadenas `s` y `t` de longitudes `m` y `n` respectivamente, devuelve la subcadena de ventana mínima de `s` que contiene todos los caracteres de `t` (incluyendo duplicados). Si no existe tal subcadena, devuelve una cadena vacía "".

Se garantiza que los casos de prueba generarán una respuesta única.

## Ejemplos

### Ejemplo 1:

**Entrada:** s = "ADOBECODEBANC", t = "ABC"
**Salida:** "BANC"
**Explicación:** La subcadena de ventana mínima "BANC" incluye 'A', 'B' y 'C' de la cadena t.

### Ejemplo 2:

**Entrada:** s = "a", t = "a"
**Salida:** "a"
**Explicación:** La cadena s completa es la ventana mínima.

### Ejemplo 3:

**Entrada:** s = "a", t = "aa"
**Salida:** ""
**Explicación:** Ambas 'a' de t deben estar incluidas en la ventana. Como la ventana más grande de s solo tiene una 'a', se devuelve una cadena vacía.

## Restricciones

- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- s y t consisten en letras mayúsculas y minúsculas del alfabeto inglés.

## Desafío adicional

¿Podrías encontrar un algoritmo que se ejecute en tiempo O(m + n)?