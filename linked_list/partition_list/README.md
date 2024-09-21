# Partición de Lista Enlazada

## Descripción

Dada la cabeza de una lista enlazada y un valor x, reorganiza la lista de manera que todos los nodos con valores menores que x aparezcan antes que los nodos con valores mayores o iguales a x.

Debes mantener el orden relativo original de los nodos en cada una de las dos particiones.

## Ejemplos

### Ejemplo 1:

**Entrada:** cabeza = [1,4,3,2,5,2], x = 3
**Salida:** [1,2,2,4,3,5]

### Ejemplo 2:

**Entrada:** cabeza = [2,1], x = 2
**Salida:** [1,2]

## Restricciones

- El número de nodos en la lista está en el rango [0, 200].
- -100 <= Valor del nodo <= 100
- -200 <= x <= 200