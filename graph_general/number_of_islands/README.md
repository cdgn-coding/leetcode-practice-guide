# Número de Islas

## Descripción

Dado un mapa representado por una cuadrícula binaria 2D de tamaño m x n, donde '1' representa tierra y '0' representa agua, devuelve el número de islas.

Una isla está rodeada de agua y se forma conectando terrenos adyacentes horizontal o verticalmente. Puedes asumir que los cuatro bordes de la cuadrícula están rodeados de agua.

## Ejemplos

### Ejemplo 1:

**Entrada:**
```
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
```
**Salida:** 1

### Ejemplo 2:

**Entrada:**
```
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
```
**Salida:** 3

## Restricciones

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] es '0' o '1'.