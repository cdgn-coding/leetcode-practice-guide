# Nota de Rescate

## Descripción

Dadas dos cadenas de texto, `notaRescate` y `revista`, determina si es posible construir `notaRescate` utilizando las letras de `revista`. Devuelve `true` si es posible, y `false` en caso contrario.

Cada letra de `revista` solo puede ser utilizada una vez en `notaRescate`.

## Ejemplos

### Ejemplo 1:

**Entrada:** notaRescate = "a", revista = "b"
**Salida:** false

### Ejemplo 2:

**Entrada:** notaRescate = "aa", revista = "ab"
**Salida:** false

### Ejemplo 3:

**Entrada:** notaRescate = "aa", revista = "aab"
**Salida:** true

## Restricciones

- 1 <= longitud de notaRescate, longitud de revista <= 10^5
- Tanto `notaRescate` como `revista` contienen únicamente letras minúsculas del alfabeto inglés.