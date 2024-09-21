# Captura de Regiones Rodeadas

## Descripción

Se te proporciona una matriz `board` de dimensiones m x n que contiene las letras 'X' y 'O'. Tu tarea es capturar las regiones que están rodeadas, siguiendo estas reglas:

- **Conexión**: Una celda está conectada a las celdas adyacentes horizontal o verticalmente.
- **Región**: Una región se forma conectando todas las celdas 'O' adyacentes.
- **Rodeada**: Una región está rodeada por celdas 'X' si puedes conectar la región con celdas 'X' y ninguna de las celdas de la región está en el borde del tablero.

Una región rodeada se captura reemplazando todas las 'O' por 'X' en la matriz de entrada `board`.

## Ejemplos

### Ejemplo 1:

**Entrada**: 
```
board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
]
```

**Salida**: 
```
[
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","O","X","X"]
]
```

**Explicación**: En el diagrama anterior, la región inferior no se captura porque está en el borde del tablero y no puede ser rodeada.

### Ejemplo 2:

**Entrada**: 
```
board = [["X"]]
```

**Salida**: 
```
[["X"]]
```

## Restricciones

- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] es 'X' o 'O'.