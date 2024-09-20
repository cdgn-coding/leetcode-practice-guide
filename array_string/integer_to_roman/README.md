# Conversión de Números Enteros a Números Romanos

## Descripción

Siete símbolos diferentes representan los números romanos con los siguientes valores:

Símbolo | Valor
------- | -----
I       | 1
V       | 5
X       | 10
L       | 50
C       | 100
D       | 500
M       | 1000

Los números romanos se forman agregando las conversiones de los valores decimales de mayor a menor. La conversión de un valor decimal a un número romano tiene las siguientes reglas:

1. Si el valor no comienza con 4 o 9, selecciona el símbolo del valor máximo que se puede restar del valor de entrada, agrega ese símbolo al resultado, resta su valor y convierte el resto a un número romano.
2. Si el valor comienza con 4 o 9, utiliza la forma sustractiva representando un símbolo restado del siguiente símbolo. Por ejemplo, 4 es 1 (I) menos que 5 (V): IV, y 9 es 1 (I) menos que 10 (X): IX. Solo se utilizan las siguientes formas sustractivas: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) y 900 (CM).
3. Solo las potencias de 10 (I, X, C, M) se pueden agregar consecutivamente como máximo 3 veces para representar múltiplos de 10. No se pueden agregar 5 (V), 50 (L) o 500 (D) varias veces. Si necesitas agregar un símbolo 4 veces, utiliza la forma sustractiva.

Dado un número entero, conviértelo a un número romano.

## Ejemplos

### Ejemplo 1:

- Entrada: num = 3749
- Salida: "MMMDCCXLIX"

Explicación:
- 3000 = MMM (1000 (M) + 1000 (M) + 1000 (M))
- 700 = DCC (500 (D) + 100 (C) + 100 (C))
- 40 = XL (10 (X) menos que 50 (L))
- 9 = IX (1 (I) menos que 10 (X))

Nota: 49 no es 1 (I) menos que 50 (L) porque la conversión se basa en los lugares decimales.

### Ejemplo 2:

- Entrada: num = 58
- Salida: "LVIII"

Explicación:
- 50 = L
- 8 = VIII

### Ejemplo 3:

- Entrada: num = 1994
- Salida: "MCMXCIV"

Explicación:
- 1000 = M
- 900 = CM
- 90 = XC
- 4 = IV

## Restricciones

- 1 <= num <= 3999