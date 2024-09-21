# Inversión de nodos en grupos de k en una lista enlazada

## Descripción

Dada la cabeza de una lista enlazada, invierte los nodos de la lista en grupos de k elementos y devuelve la lista modificada.

k es un número entero positivo y es menor o igual que la longitud de la lista enlazada. Si el número de nodos no es múltiplo de k, los nodos restantes al final deben permanecer sin cambios.

No se permite alterar los valores de los nodos, solo se pueden modificar los nodos en sí mismos.

## Ejemplos

### Ejemplo 1:

**Entrada:** cabeza = [1,2,3,4,5], k = 2
**Salida:** [2,1,4,3,5]

### Ejemplo 2:

**Entrada:** cabeza = [1,2,3,4,5], k = 3
**Salida:** [3,2,1,4,5]

## Restricciones

- El número de nodos en la lista es n.
- 1 <= k <= n <= 5000
- 0 <= Valor del nodo <= 1000

## Desafío adicional

¿Puedes resolver el problema utilizando O(1) de espacio adicional en memoria?