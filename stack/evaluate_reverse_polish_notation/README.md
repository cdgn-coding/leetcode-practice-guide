# Evaluación de Expresión en Notación Polaca Inversa

## Descripción del Problema

Se te proporciona un array de cadenas `tokens` que representa una expresión aritmética en Notación Polaca Inversa (RPN).

Tu tarea es evaluar la expresión y devolver un entero que represente el valor de la misma.

Consideraciones importantes:

- Los operadores válidos son '+', '-', '*' y '/'.
- Cada operando puede ser un número entero u otra expresión.
- La división entre dos enteros siempre se trunca hacia cero.
- No habrá divisiones por cero.
- La entrada representa una expresión aritmética válida en notación polaca inversa.
- Tanto el resultado final como todos los cálculos intermedios pueden representarse con un entero de 32 bits.

## Ejemplos

### Ejemplo 1:

**Entrada:** tokens = ["2","1","+","3","*"]
**Salida:** 9
**Explicación:** ((2 + 1) * 3) = 9

### Ejemplo 2:

**Entrada:** tokens = ["4","13","5","/","+"]
**Salida:** 6
**Explicación:** (4 + (13 / 5)) = 6

### Ejemplo 3:

**Entrada:** tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
**Salida:** 22
**Explicación:** 
((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

## Restricciones

- 1 <= tokens.length <= 10^4
- Cada elemento tokens[i] es o bien un operador: "+", "-", "*", "/", o un entero en el rango [-200, 200].