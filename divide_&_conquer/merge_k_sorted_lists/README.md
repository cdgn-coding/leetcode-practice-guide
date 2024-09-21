# Fusión de k Listas Enlazadas Ordenadas

## Descripción

Se te proporciona un arreglo de `k` listas enlazadas `lists`, donde cada lista enlazada está ordenada de forma ascendente.

Tu tarea es combinar todas las listas enlazadas en una única lista enlazada ordenada y devolverla.

## Ejemplos

### Ejemplo 1:

**Entrada:** lists = [[1,4,5],[1,3,4],[2,6]]
**Salida:** [1,1,2,3,4,4,5,6]
**Explicación:** 
Las listas enlazadas son:
```
[
  1->4->5,
  1->3->4,
  2->6
]
```
Al combinarlas en una lista ordenada, obtenemos:
1->1->2->3->4->4->5->6

### Ejemplo 2:

**Entrada:** lists = []
**Salida:** []

### Ejemplo 3:

**Entrada:** lists = [[]]
**Salida:** []

## Restricciones

- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- Cada lists[i] está ordenada de forma ascendente.
- La suma de las longitudes de todas las listas (lists[i].length) no excederá 10^4.