# Número Palíndromo

## Descripción

Dado un número entero `x`, devuelve `true` si `x` es un palíndromo, y `false` en caso contrario.

Un número es un palíndromo cuando se lee igual de izquierda a derecha que de derecha a izquierda.

## Ejemplos

### Ejemplo 1:

**Entrada:** x = 121
**Salida:** true
**Explicación:** 121 se lee igual de izquierda a derecha y de derecha a izquierda.

### Ejemplo 2:

**Entrada:** x = -121
**Salida:** false
**Explicación:** De izquierda a derecha se lee -121. De derecha a izquierda se convierte en 121-. Por lo tanto, no es un palíndromo.

### Ejemplo 3:

**Entrada:** x = 10
**Salida:** false
**Explicación:** Se lee 01 de derecha a izquierda. Por lo tanto, no es un palíndromo.

## Restricciones

- -2^31 <= x <= 2^31 - 1

## Desafío adicional

¿Podrías resolver este problema sin convertir el número entero a una cadena de texto?