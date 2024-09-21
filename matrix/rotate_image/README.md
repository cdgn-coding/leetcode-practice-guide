# Rotación de Imagen

## Descripción

Se te proporciona una matriz 2D de n x n que representa una imagen. Tu tarea es rotar la imagen 90 grados en sentido horario.

Debes realizar la rotación in situ, lo que significa que tienes que modificar directamente la matriz 2D de entrada. NO se permite asignar otra matriz 2D para realizar la rotación.

## Ejemplos

### Ejemplo 1:

**Entrada:** matriz = [[1,2,3],[4,5,6],[7,8,9]]
**Salida:** [[7,4,1],[8,5,2],[9,6,3]]

### Ejemplo 2:

**Entrada:** matriz = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
**Salida:** [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

## Restricciones

- n == matriz.length == matriz[i].length
- 1 <= n <= 20
- -1000 <= matriz[i][j] <= 1000