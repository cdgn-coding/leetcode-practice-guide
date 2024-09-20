# Invertir las Palabras de una Cadena

## Descripción

Dada una cadena de entrada `s`, invierte el orden de las palabras.

Una palabra se define como una secuencia de caracteres que no son espacios. Las palabras en `s` estarán separadas por al menos un espacio.

Devuelve una cadena con las palabras en orden inverso, concatenadas por un solo espacio.

Ten en cuenta que `s` puede contener espacios al principio, al final o múltiples espacios entre dos palabras. La cadena devuelta debe tener solo un espacio separando las palabras. No incluyas ningún espacio adicional.

## Ejemplos

### Ejemplo 1:

- Entrada: s = "the sky is blue"
- Salida: "blue is sky the"

### Ejemplo 2:

- Entrada: s = "  hello world  "
- Salida: "world hello"
- Explicación: La cadena invertida no debe contener espacios al principio ni al final.

### Ejemplo 3:

- Entrada: s = "a good   example"
- Salida: "example good a"
- Explicación: Debes reducir los múltiples espacios entre dos palabras a un solo espacio en la cadena invertida.

## Restricciones

- 1 <= s.length <= 10^4
- `s` contiene letras en inglés (mayúsculas y minúsculas), dígitos y espacios ' '.
- Hay al menos una palabra en `s`.

## Seguimiento

Si el tipo de dato de cadena es mutable en tu lenguaje, ¿puedes resolver el problema en su lugar con O(1) de espacio adicional?