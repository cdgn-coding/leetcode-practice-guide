# Representación de una Matriz como Quad-Tree

## Descripción

Dada una matriz cuadrada `grid` de tamaño n x n compuesta únicamente por 0's y 1's, queremos representarla mediante un Quad-Tree.

Tu tarea es devolver la raíz del Quad-Tree que representa la matriz `grid`.

Un Quad-Tree es una estructura de datos en forma de árbol donde cada nodo interno tiene exactamente cuatro hijos. Además, cada nodo tiene dos atributos:

- `val`: Verdadero si el nodo representa una cuadrícula de 1's o Falso si representa una cuadrícula de 0's. Ten en cuenta que puedes asignar `val` como Verdadero o Falso cuando `isLeaf` es Falso, y ambos son aceptados en la respuesta.
- `isLeaf`: Verdadero si el nodo es una hoja del árbol o Falso si el nodo tiene cuatro hijos.

```java
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
```

Podemos construir un Quad-Tree a partir de un área bidimensional siguiendo estos pasos:

1. Si la cuadrícula actual tiene el mismo valor en todas sus celdas (todos 1's o todos 0's), establece `isLeaf` como Verdadero, `val` como el valor de la cuadrícula, los cuatro hijos como Nulo y detén el proceso.
2. Si la cuadrícula actual tiene valores diferentes, establece `isLeaf` como Falso, `val` como cualquier valor, y divide la cuadrícula actual en cuatro sub-cuadrículas.
3. Repite el proceso de forma recursiva para cada uno de los hijos con la sub-cuadrícula correspondiente.

Para más información sobre Quad-Trees, puedes consultar la Wikipedia.

## Formato del Quad-Tree

No es necesario que leas esta sección para resolver el problema. Esto es solo si quieres entender el formato de salida.

La salida representa el formato serializado de un Quad-Tree utilizando un recorrido por niveles, donde `null` indica un terminador de camino donde no existe ningún nodo debajo.

Es muy similar a la serialización de un árbol binario. La única diferencia es que el nodo se representa como una lista `[isLeaf, val]`.

Si el valor de `isLeaf` o `val` es Verdadero, lo representamos como 1 en la lista `[isLeaf, val]`, y si es Falso, lo representamos como 0.

## Ejemplos

### Ejemplo 1:

**Entrada:** grid = [[0,1],[1,0]]
**Salida:** [[0,1],[1,0],[1,1],[1,1],[1,0]]
**Explicación:** La explicación de este ejemplo se muestra en la imagen. Ten en cuenta que 0 representa Falso y 1 representa Verdadero en la foto que representa el Quad-Tree.

### Ejemplo 2:

**Entrada:** grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
**Salida:** [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
**Explicación:** No todos los valores en la cuadrícula son iguales. Dividimos la cuadrí