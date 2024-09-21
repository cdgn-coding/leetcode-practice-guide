# Suma de Números de Raíz a Hoja

## Descripción

Se te proporciona la raíz de un árbol binario que contiene únicamente dígitos del 0 al 9.

Cada camino desde la raíz hasta una hoja en el árbol representa un número.

Por ejemplo, el camino de raíz a hoja 1 -> 2 -> 3 representa el número 123.

Tu tarea es calcular la suma total de todos los números formados por los caminos de raíz a hoja. Los casos de prueba están diseñados de manera que la respuesta quepa en un entero de 32 bits.

Un nodo hoja es aquel que no tiene hijos.

## Ejemplos

### Ejemplo 1:

**Entrada:** raíz = [1,2,3]
**Salida:** 25
**Explicación:**
El camino de raíz a hoja 1->2 representa el número 12.
El camino de raíz a hoja 1->3 representa el número 13.
Por lo tanto, la suma es 12 + 13 = 25.

### Ejemplo 2:

**Entrada:** raíz = [4,9,0,5,1]
**Salida:** 1026
**Explicación:**
El camino de raíz a hoja 4->9->5 representa el número 495.
El camino de raíz a hoja 4->9->1 representa el número 491.
El camino de raíz a hoja 4->0 representa el número 40.
Por lo tanto, la suma es 495 + 491 + 40 = 1026.

## Restricciones

- El número de nodos en el árbol está en el rango [1, 1000].
- 0 <= Valor del nodo <= 9
- La profundidad del árbol no excederá 10.