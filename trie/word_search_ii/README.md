# Búsqueda de Palabras en Tablero

## Descripción

Dado un tablero de caracteres de dimensiones m x n y una lista de palabras, devuelve todas las palabras que se pueden encontrar en el tablero.

Cada palabra debe formarse utilizando letras de celdas adyacentes secuencialmente, donde las celdas adyacentes son las vecinas horizontal o verticalmente. La misma celda no puede utilizarse más de una vez para formar una palabra.

## Ejemplos

### Ejemplo 1:

**Entrada:** 
- Tablero:
```
[["o","a","a","n"],
 ["e","t","a","e"],
 ["i","h","k","r"],
 ["i","f","l","v"]]
```
- Palabras: ["oath", "pea", "eat", "rain"]

**Salida:** ["eat", "oath"]

### Ejemplo 2:

**Entrada:**
- Tablero:
```
[["a","b"],
 ["c","d"]]
```
- Palabras: ["abcb"]

**Salida:** []

## Restricciones

- m == número de filas del tablero
- n == número de columnas del tablero
- 1 <= m, n <= 12
- board[i][j] es una letra minúscula del alfabeto inglés
- 1 <= cantidad de palabras <= 3 * 10^4
- 1 <= longitud de cada palabra <= 10
- Cada palabra consiste en letras minúsculas del alfabeto inglés
- Todas las palabras en la lista son únicas