# Caminos Únicos del Robot II

## Descripción

Se te proporciona una matriz de enteros `grid` de dimensiones `m x n`. Hay un robot inicialmente ubicado en la esquina superior izquierda (es decir, `grid[0][0]`). El robot intenta moverse hacia la esquina inferior derecha (es decir, `grid[m - 1][n - 1]`). En cada momento, el robot solo puede moverse hacia abajo o hacia la derecha.

En la cuadrícula, los obstáculos están marcados con 1 y los espacios libres con 0. El camino que tome el robot no puede incluir ninguna casilla que sea un obstáculo.

Tu tarea es devolver el número de posibles caminos únicos que el robot puede tomar para llegar a la esquina inferior derecha.

Los casos de prueba están generados de tal manera que la respuesta será menor o igual a 2 * 10^9.

## Ejemplos

### Ejemplo 1:

**Entrada:** obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
**Salida:** 2
**Explicación:** Hay un obstáculo en el centro de la cuadrícula 3x3 de arriba.
Existen dos formas de llegar a la esquina inferior derecha:
1. Derecha -> Derecha -> Abajo -> Abajo
2. Abajo -> Abajo -> Derecha -> Derecha

### Ejemplo 2:

**Entrada:** obstacleGrid = [[0,1],[0,0]]
**Salida:** 1

## Restricciones

- m == obstacleGrid.length
- n == obstacleGrid[i].length
- 1 <= m, n <= 100
- obstacleGrid[i][j] es 0 o 1.