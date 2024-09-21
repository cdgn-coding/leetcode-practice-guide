# Máximo Cuadrado de Unos

## Descripción

Dada una matriz binaria de dimensiones m x n compuesta por '0's y '1's, encuentra el cuadrado más grande que contenga únicamente '1's y devuelve su área.

## Ejemplos

### Ejemplo 1:

**Entrada:** 
```
matriz = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
```
**Salida:** 4

### Ejemplo 2:

**Entrada:** 
```
matriz = [
  ["0","1"],
  ["1","0"]
]
```
**Salida:** 1

### Ejemplo 3:

**Entrada:** 
```
matriz = [["0"]]
```
**Salida:** 0

## Restricciones

- m == número de filas de la matriz
- n == número de columnas de la matriz
- 1 <= m, n <= 300
- Cada elemento matriz[i][j] es '0' o '1'.