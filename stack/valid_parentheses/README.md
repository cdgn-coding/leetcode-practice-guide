# Validación de Paréntesis

## Descripción

Dada una cadena `s` que contiene únicamente los caracteres '(', ')', '{', '}', '[' y ']', determina si la cadena de entrada es válida.

Una cadena de entrada se considera válida si:

1. Los paréntesis abiertos deben cerrarse con el mismo tipo de paréntesis.
2. Los paréntesis abiertos deben cerrarse en el orden correcto.
3. Cada paréntesis de cierre tiene un paréntesis de apertura correspondiente del mismo tipo.

## Ejemplos

### Ejemplo 1:

**Entrada:** s = "()"
**Salida:** true

### Ejemplo 2:

**Entrada:** s = "()[]{}"
**Salida:** true

### Ejemplo 3:

**Entrada:** s = "(]"
**Salida:** false

### Ejemplo 4:

**Entrada:** s = "([)]"
**Salida:** false

### Ejemplo 5:

**Entrada:** s = "([])"
**Salida:** true

## Restricciones

- 1 <= s.length <= 10^4
- `s` solo contiene paréntesis de los tipos '()', '[]' y '{}'.