# Camino de Suma Mínima

## Descripción

Dado un tablero de `m x n` casillas lleno de números no negativos, encuentra un camino desde la esquina superior izquierda hasta la esquina inferior derecha que minimice la suma de todos los números a lo largo de su recorrido.

**Nota:** En cada paso, solo puedes moverte hacia abajo o hacia la derecha.

## Ejemplos

### Ejemplo 1:

**Entrada:** tablero = [[1,3,1],[1,5,1],[4,2,1]]
**Salida:** 7
**Explicación:** El camino 1 → 3 → 1 → 1 → 1 minimiza la suma.

### Ejemplo 2:

**Entrada:** tablero = [[1,2,3],[4,5,6]]
**Salida:** 12

## Restricciones

- m == tablero.length
- n == tablero[i].length
- 1 <= m, n <= 200
- 0 <= tablero[i][j] <= 200