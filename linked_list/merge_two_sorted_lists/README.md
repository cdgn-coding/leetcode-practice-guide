# Fusión de Dos Listas Enlazadas Ordenadas

## Descripción

Se te proporcionan las cabeceras de dos listas enlazadas ordenadas, `lista1` y `lista2`.

Tu tarea es combinar estas dos listas en una sola lista ordenada. La nueva lista debe crearse uniendo los nodos de las dos listas originales.

Debes devolver la cabecera de la lista enlazada resultante después de la fusión.

## Ejemplos

### Ejemplo 1:

**Entrada:** lista1 = [1,2,4], lista2 = [1,3,4]
**Salida:** [1,1,2,3,4,4]

### Ejemplo 2:

**Entrada:** lista1 = [], lista2 = []
**Salida:** []

### Ejemplo 3:

**Entrada:** lista1 = [], lista2 = [0]
**Salida:** [0]

## Restricciones

- El número de nodos en ambas listas está en el rango [0, 50].
- El valor de cada nodo está entre -100 y 100, inclusive.
- Tanto `lista1` como `lista2` están ordenadas de forma no decreciente.