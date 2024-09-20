# Contenedor con Más Agua

## Descripción

Se te proporciona un array de enteros `altura` de longitud `n`. Imagina `n` líneas verticales dibujadas de tal manera que los dos extremos de la i-ésima línea están en las coordenadas `(i, 0)` y `(i, altura[i])`.

Tu tarea es encontrar dos líneas que, junto con el eje x, formen un contenedor que pueda almacenar la mayor cantidad de agua posible.

Debes devolver la cantidad máxima de agua que este contenedor puede almacenar.

Ten en cuenta que no puedes inclinar el contenedor.

## Ejemplos

### Ejemplo 1:

**Entrada:** altura = [1,8,6,2,5,4,8,3,7]
**Salida:** 49
**Explicación:** Las líneas verticales mencionadas están representadas por el array [1,8,6,2,5,4,8,3,7]. En este caso, el área máxima de agua (sección azul) que el contenedor puede contener es 49 unidades cuadradas.

### Ejemplo 2:

**Entrada:** altura = [1,1]
**Salida:** 1

## Restricciones

- n == altura.length
- 2 <= n <= 10^5
- 0 <= altura[i] <= 10^4