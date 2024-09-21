# Calculadora Básica

## Descripción

Se te proporciona una cadena `s` que representa una expresión matemática válida. Implementa una calculadora básica para evaluarla y devuelve el resultado de la evaluación.

Nota: No está permitido utilizar ninguna función integrada que evalúe cadenas como expresiones matemáticas, como por ejemplo `eval()`.

## Ejemplos

### Ejemplo 1:

**Entrada:** s = "1 + 1"
**Salida:** 2

### Ejemplo 2:

**Entrada:** s = " 2-1 + 2 "
**Salida:** 3

### Ejemplo 3:

**Entrada:** s = "(1+(4+5+2)-3)+(6+8)"
**Salida:** 23

## Restricciones

- La longitud de s está entre 1 y 3 * 10^5.
- s contiene dígitos, '+', '-', '(', ')', y espacios.
- s representa una expresión válida.
- '+' no se usa como operación unaria (es decir, "+1" y "+(2 + 3)" no son válidos).
- '-' puede usarse como operación unaria (es decir, "-1" y "-(2 + 3)" son válidos).
- No habrá dos operadores consecutivos en la entrada.
- Todos los números y cálculos intermedios cabrán en un entero de 32 bits con signo.