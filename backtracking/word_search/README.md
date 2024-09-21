# Búsqueda de Palabra en una Cuadrícula

## Descripción

Dada una cuadrícula de caracteres `board` de dimensiones m x n y una cadena `word`, devuelve `true` si la palabra existe en la cuadrícula.

La palabra puede construirse a partir de letras de celdas adyacentes secuencialmente, donde las celdas adyacentes son vecinas horizontal o verticalmente. La misma celda no puede utilizarse más de una vez.

## Ejemplos

### Ejemplo 1:

**Entrada:** 
- board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
- word = "ABCCED"

**Salida:** true

### Ejemplo 2:

**Entrada:**
- board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
- word = "SEE"

**Salida:** true

### Ejemplo 3:

**Entrada:**
- board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
- word = "ABCB"

**Salida:** false

## Restricciones

- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- `board` y `word` contienen solo letras mayúsculas y minúsculas del alfabeto inglés.

## Desafío adicional

¿Podrías utilizar técnicas de poda en la búsqueda para hacer que tu solución sea más rápida con una cuadrícula más grande?