# Conversión Zigzag

## Descripción

La cadena "PAYPALISHIRING" se escribe en un patrón zigzag en un número dado de filas de la siguiente manera (es posible que desees mostrar este patrón en una fuente de ancho fijo para una mejor legibilidad):

P   A   H   N
A P L S I I G
Y   I   R

Y luego se lee línea por línea: "PAHNAPLSIIGYIR"

Escribe el código que tome una cadena y realice esta conversión dado un número de filas:

```cpp
string convert(string s, int numRows);
```

## Ejemplos

### Ejemplo 1:

- Entrada: s = "PAYPALISHIRING", numRows = 3
- Salida: "PAHNAPLSIIGYIR"

### Ejemplo 2:

- Entrada: s = "PAYPALISHIRING", numRows = 4
- Salida: "PINALSIGYAHRPI"
- Explicación:
  P     I    N
  A   L S  I G
  Y A   H R
  P     I

### Ejemplo 3:

- Entrada: s = "A", numRows = 1
- Salida: "A"

## Restricciones

- 1 <= s.length <= 1000
- s consiste en letras inglesas (minúsculas y mayúsculas), ',' y '.'.
- 1 <= numRows <= 1000