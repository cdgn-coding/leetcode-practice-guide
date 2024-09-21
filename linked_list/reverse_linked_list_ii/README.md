# Inversión Parcial de Lista Enlazada

## Descripción

Dada la cabeza de una lista enlazada simple y dos enteros `izquierda` y `derecha`, donde `izquierda <= derecha`, invierte los nodos de la lista desde la posición `izquierda` hasta la posición `derecha`, y devuelve la lista invertida.

## Ejemplos

### Ejemplo 1:

**Entrada:** cabeza = [1,2,3,4,5], izquierda = 2, derecha = 4
**Salida:** [1,4,3,2,5]

### Ejemplo 2:

**Entrada:** cabeza = [5], izquierda = 1, derecha = 1
**Salida:** [5]

## Restricciones

- El número de nodos en la lista es `n`.
- 1 <= n <= 500
- -500 <= Valor del Nodo <= 500
- 1 <= izquierda <= derecha <= n

## Desafío adicional

¿Podrías resolverlo en una sola pasada?