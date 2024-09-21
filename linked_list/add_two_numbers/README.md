# Suma de Dos Números

## Descripción

Se te proporcionan dos listas enlazadas no vacías que representan dos números enteros no negativos. Los dígitos están almacenados en orden inverso, y cada nodo de las listas contiene un solo dígito. Tu tarea es sumar estos dos números y devolver el resultado como una nueva lista enlazada.

Puedes asumir que los dos números no contienen ceros a la izquierda, excepto el número 0 en sí mismo.

## Ejemplos

### Ejemplo 1:

**Entrada:** l1 = [2,4,3], l2 = [5,6,4]
**Salida:** [7,0,8]
**Explicación:** 342 + 465 = 807

### Ejemplo 2:

**Entrada:** l1 = [0], l2 = [0]
**Salida:** [0]

### Ejemplo 3:

**Entrada:** l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
**Salida:** [8,9,9,9,0,0,0,1]

## Restricciones

- El número de nodos en cada lista enlazada está en el rango [1, 100].
- 0 <= Valor del nodo <= 9
- Se garantiza que la lista representa un número que no tiene ceros a la izquierda.