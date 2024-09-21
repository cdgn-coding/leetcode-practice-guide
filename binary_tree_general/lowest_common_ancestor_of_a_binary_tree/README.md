# Ancestro Común Más Cercano de un Árbol Binario

## Descripción

Dado un árbol binario, encuentra el ancestro común más cercano (LCA, por sus siglas en inglés) de dos nodos dados en el árbol.

Según la definición de LCA en Wikipedia: "El ancestro común más cercano se define entre dos nodos p y q como el nodo más bajo en T que tiene tanto a p como a q como descendientes (donde permitimos que un nodo sea descendiente de sí mismo)."

## Ejemplos

### Ejemplo 1:

**Entrada:** raíz = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
**Salida:** 3
**Explicación:** El LCA de los nodos 5 y 1 es 3.

### Ejemplo 2:

**Entrada:** raíz = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
**Salida:** 5
**Explicación:** El LCA de los nodos 5 y 4 es 5, ya que un nodo puede ser descendiente de sí mismo según la definición de LCA.

### Ejemplo 3:

**Entrada:** raíz = [1,2], p = 1, q = 2
**Salida:** 1

## Restricciones

- El número de nodos en el árbol está en el rango [2, 10^5].
- -10^9 <= Node.val <= 10^9
- Todos los valores de Node.val son únicos.
- p != q
- p y q existirán en el árbol.