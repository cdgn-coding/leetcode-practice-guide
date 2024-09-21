# Suma Máxima de Camino en Árbol Binario

## Descripción

En un árbol binario, un camino es una secuencia de nodos donde cada par de nodos adyacentes en la secuencia está conectado por una arista. Cada nodo puede aparecer en la secuencia como máximo una vez. Es importante notar que el camino no necesita pasar por la raíz del árbol.

La suma de un camino se define como la suma de los valores de todos los nodos que forman parte de ese camino.

Dado el nodo raíz de un árbol binario, tu tarea es encontrar y devolver la suma máxima de cualquier camino no vacío en el árbol.

## Ejemplos

### Ejemplo 1:

**Entrada:** raíz = [1,2,3]
**Salida:** 6
**Explicación:** El camino óptimo es 2 -> 1 -> 3, con una suma de 2 + 1 + 3 = 6.

### Ejemplo 2:

**Entrada:** raíz = [-10,9,20,null,null,15,7]
**Salida:** 42
**Explicación:** El camino óptimo es 15 -> 20 -> 7, con una suma de 15 + 20 + 7 = 42.

## Restricciones

- El número de nodos en el árbol está en el rango [1, 3 * 10^4].
- El valor de cada nodo está entre -1000 y 1000, ambos inclusive.