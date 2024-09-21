# Suma de Camino

## Descripción

Dado el nodo raíz de un árbol binario y un número entero `sumaObjetivo`, devuelve `true` si el árbol tiene un camino desde la raíz hasta una hoja tal que la suma de todos los valores a lo largo del camino sea igual a `sumaObjetivo`.

Una hoja es un nodo sin hijos.

## Ejemplos

### Ejemplo 1:

**Entrada:** raíz = [5,4,8,11,null,13,4,7,2,null,null,null,1], sumaObjetivo = 22
**Salida:** true
**Explicación:** Se muestra el camino de la raíz a la hoja con la suma objetivo.

### Ejemplo 2:

**Entrada:** raíz = [1,2,3], sumaObjetivo = 5
**Salida:** false
**Explicación:** Hay dos caminos de la raíz a las hojas en el árbol:
(1 --> 2): La suma es 3.
(1 --> 3): La suma es 4.
No existe ningún camino de la raíz a una hoja con suma = 5.

### Ejemplo 3:

**Entrada:** raíz = [], sumaObjetivo = 0
**Salida:** false
**Explicación:** Como el árbol está vacío, no hay caminos de la raíz a las hojas.

## Restricciones

- El número de nodos en el árbol está en el rango [0, 5000].
- -1000 <= Valor del nodo <= 1000
- -1000 <= sumaObjetivo <= 1000