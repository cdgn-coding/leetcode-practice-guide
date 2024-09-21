# Combinaciones de Letras de un Número de Teléfono

## Descripción

Dada una cadena que contiene dígitos del 2 al 9 inclusive, devuelve todas las posibles combinaciones de letras que el número podría representar. Puedes devolver la respuesta en cualquier orden.

Se proporciona un mapeo de dígitos a letras (similar a los botones de un teléfono) a continuación. Ten en cuenta que el 1 no corresponde a ninguna letra.

![Teclado telefónico](https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

## Ejemplos

### Ejemplo 1:

**Entrada:** digits = "23"
**Salida:** ["ad","ae","af","bd","be","bf","cd","ce","cf"]

### Ejemplo 2:

**Entrada:** digits = ""
**Salida:** []

### Ejemplo 3:

**Entrada:** digits = "2"
**Salida:** ["a","b","c"]

## Restricciones

- 0 <= longitud de digits <= 4
- Cada dígito en digits está en el rango ['2', '9'].