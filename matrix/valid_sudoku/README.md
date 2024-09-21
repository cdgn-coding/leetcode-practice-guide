# Validación de Tablero de Sudoku

## Descripción

Determina si un tablero de Sudoku de 9 x 9 es válido. Solo es necesario validar las celdas llenas según las siguientes reglas:

1. Cada fila debe contener los dígitos del 1 al 9 sin repetición.
2. Cada columna debe contener los dígitos del 1 al 9 sin repetición.
3. Cada una de las nueve subcuadrículas de 3 x 3 del tablero debe contener los dígitos del 1 al 9 sin repetición.

**Nota:**
- Un tablero de Sudoku (parcialmente lleno) puede ser válido pero no necesariamente tener solución.
- Solo es necesario validar las celdas llenas según las reglas mencionadas.

## Ejemplos

### Ejemplo 1:

**Entrada:** 
```
tablero = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
```
**Salida:** true

### Ejemplo 2:

**Entrada:**
```
tablero = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
```
**Salida:** false

**Explicación:** Similar al Ejemplo 1, pero con el 5 en la esquina superior izquierda cambiado por un 8. Como hay dos 8 en la subcuadrícula superior izquierda de 3x3, el tablero no es válido.

## Restricciones

- La longitud del tablero es 9.
- La longitud de cada fila del tablero es 9.
- Cada `tablero[i][j]` es un dígito del 1 al 9 o un punto '.'.