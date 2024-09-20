# Palíndromo Válido

## Descripción

Una frase es un palíndromo si, después de convertir todas las letras mayúsculas a minúsculas y eliminar todos los caracteres no alfanuméricos, se lee igual de izquierda a derecha y de derecha a izquierda. Los caracteres alfanuméricos incluyen letras y números.

Dada una cadena `s`, devuelve `true` si es un palíndromo, o `false` en caso contrario.

## Ejemplos

### Ejemplo 1:

**Entrada:** s = "A man, a plan, a canal: Panama"
**Salida:** true
**Explicación:** "amanaplanacanalpanama" es un palíndromo.

### Ejemplo 2:

**Entrada:** s = "race a car"
**Salida:** false
**Explicación:** "raceacar" no es un palíndromo.

### Ejemplo 3:

**Entrada:** s = " "
**Salida:** true
**Explicación:** Después de eliminar los caracteres no alfanuméricos, s es una cadena vacía "". Como una cadena vacía se lee igual en ambos sentidos, es un palíndromo.

## Restricciones

- 1 <= s.length <= 2 * 10^5
- s contiene solo caracteres ASCII imprimibles.