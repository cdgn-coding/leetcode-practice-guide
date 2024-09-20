# Conversión de Números Romanos a Enteros

## Descripción

Los números romanos están representados por siete símbolos diferentes: I, V, X, L, C, D y M.

| Símbolo | Valor |
|---------|-------|
| I       | 1     |
| V       | 5     |
| X       | 10    |
| L       | 50    |
| C       | 100   |
| D       | 500   |
| M       | 1000  |

Por ejemplo, el número 2 se escribe como II en números romanos, simplemente dos unos sumados. El número 12 se escribe como XII, que es simplemente X + II. El número 27 se escribe como XXVII, que es XX + V + II.

Los números romanos generalmente se escriben de izquierda a derecha, de mayor a menor. Sin embargo, el número cuatro no se escribe como IIII. En su lugar, el número cuatro se escribe como IV. Debido a que el uno está antes del cinco, lo restamos, obteniendo cuatro. El mismo principio se aplica al número nueve, que se escribe como IX. Hay seis casos en los que se utiliza la sustracción:

- I puede colocarse antes de V (5) y X (10) para formar 4 y 9.
- X puede colocarse antes de L (50) y C (100) para formar 40 y 90.
- C puede colocarse antes de D (500) y M (1000) para formar 400 y 900.

Dado un número romano, conviértelo a un entero.

## Ejemplos

### Ejemplo 1:

- Entrada: s = "III"
- Salida: 3
- Explicación: III = 3.

### Ejemplo 2:

- Entrada: s = "LVIII"
- Salida: 58
- Explicación: L = 50, V = 5, III = 3.

### Ejemplo 3:

- Entrada: s = "MCMXCIV"
- Salida: 1994
- Explicación: M = 1000, CM = 900, XC = 90 y IV = 4.

## Restricciones

- 1 <= s.length <= 15
- s contiene solo los caracteres ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- Se garantiza que s es un número romano válido en el rango [1, 3999].