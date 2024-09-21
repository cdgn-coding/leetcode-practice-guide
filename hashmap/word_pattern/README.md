# Patrón y Cadena Coincidente

## Descripción

Dado un patrón y una cadena `s`, determina si `s` sigue el mismo patrón.

Aquí, "seguir" significa una coincidencia completa, de tal manera que existe una correspondencia biyectiva entre una letra en el patrón y una palabra no vacía en `s`. Específicamente:

- Cada letra en el patrón se asocia exactamente con una única palabra en `s`.
- Cada palabra única en `s` se asocia exactamente con una letra en el patrón.
- No hay dos letras que se asocien a la misma palabra, ni dos palabras que se asocien a la misma letra.

## Ejemplos

### Ejemplo 1:

**Entrada:** patrón = "abba", s = "perro gato gato perro"

**Salida:** true

**Explicación:**
La correspondencia biyectiva se puede establecer así:
- 'a' se asocia con "perro".
- 'b' se asocia con "gato".

### Ejemplo 2:

**Entrada:** patrón = "abba", s = "perro gato gato pez"

**Salida:** false

### Ejemplo 3:

**Entrada:** patrón = "aaaa", s = "perro gato gato perro"

**Salida:** false

## Restricciones

- 1 <= longitud del patrón <= 300
- El patrón contiene solo letras minúsculas del alfabeto inglés.
- 1 <= longitud de s <= 3000
- `s` contiene solo letras minúsculas del alfabeto inglés y espacios ' '.
- `s` no contiene espacios al inicio ni al final.
- Todas las palabras en `s` están separadas por un solo espacio.