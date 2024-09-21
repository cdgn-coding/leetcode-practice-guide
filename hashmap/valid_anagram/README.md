# Anagramas Válidos

## Descripción

Dadas dos cadenas de texto `s` y `t`, determina si `t` es un anagrama de `s`. Devuelve `true` si lo es, y `false` en caso contrario.

Un anagrama es una palabra o frase formada al reorganizar las letras de otra palabra o frase, utilizando todas las letras originales exactamente una vez.

## Ejemplos

### Ejemplo 1:

**Entrada:** 
- s = "anagram"
- t = "nagaram"

**Salida:** true

### Ejemplo 2:

**Entrada:**
- s = "rat"
- t = "car"

**Salida:** false

## Restricciones

- 1 <= longitud de s, longitud de t <= 5 * 10^4
- `s` y `t` contienen solo letras minúsculas del alfabeto inglés.

## Pregunta adicional

¿Qué pasaría si las entradas contuvieran caracteres Unicode? ¿Cómo adaptarías tu solución a este caso?