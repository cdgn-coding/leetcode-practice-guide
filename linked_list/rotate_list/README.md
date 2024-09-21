# Rotación de Lista Enlazada

## Descripción

Dada la cabeza de una lista enlazada, rota la lista hacia la derecha k posiciones.

## Ejemplos

### Ejemplo 1:

**Entrada:** cabeza = [1,2,3,4,5], k = 2
**Salida:** [4,5,1,2,3]

### Ejemplo 2:

**Entrada:** cabeza = [0,1,2], k = 4
**Salida:** [2,0,1]

## Restricciones

- El número de nodos en la lista está en el rango [0, 500].
- -100 <= Valor del nodo <= 100
- 0 <= k <= 2 * 10^9

## Notas

Este problema requiere manipular una estructura de datos de lista enlazada. La rotación implica mover los últimos k elementos al principio de la lista, manteniendo su orden relativo y el orden de los elementos restantes.