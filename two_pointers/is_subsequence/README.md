# Subsecuencia de cadena

## Descripción

Dadas dos cadenas `s` y `t`, devuelve `true` si `s` es una subsecuencia de `t`, o `false` en caso contrario.

Una subsecuencia de una cadena es una nueva cadena que se forma a partir de la cadena original eliminando algunos caracteres (pueden ser ninguno) sin alterar la posición relativa de los caracteres restantes. (Por ejemplo, "ace" es una subsecuencia de "abcde", mientras que "aec" no lo es).

## Ejemplos

### Ejemplo 1:

**Entrada:** s = "abc", t = "ahbgdc"
**Salida:** true

### Ejemplo 2:

**Entrada:** s = "axc", t = "ahbgdc"
**Salida:** false

## Restricciones

- 0 <= s.length <= 100
- 0 <= t.length <= 10^4
- `s` y `t` contienen solo letras minúsculas del alfabeto inglés.

## Desafío adicional

Supongamos que hay muchas cadenas `s` entrantes, digamos s1, s2, ..., sk donde k >= 10^9, y quieres comprobar una por una si `t` tiene cada una como subsecuencia. En este escenario, ¿cómo modificarías tu código?