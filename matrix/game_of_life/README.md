# El Juego de la Vida

## Descripción

Según el artículo de Wikipedia: "El Juego de la Vida, también conocido simplemente como Vida, es un autómata celular diseñado por el matemático británico John Horton Conway en 1970".

El tablero está compuesto por una cuadrícula de m x n células, donde cada célula tiene un estado inicial: viva (representada por un 1) o muerta (representada por un 0). Cada célula interactúa con sus ocho vecinos (horizontal, vertical, diagonal) siguiendo estas cuatro reglas:

1. Cualquier célula viva con menos de dos vecinos vivos muere por soledad.
2. Cualquier célula viva con dos o tres vecinos vivos sobrevive a la siguiente generación.
3. Cualquier célula viva con más de tres vecinos vivos muere por sobrepoblación.
4. Cualquier célula muerta con exactamente tres vecinos vivos se convierte en una célula viva, como por reproducción.

El siguiente estado se crea aplicando estas reglas simultáneamente a cada célula en el estado actual, donde los nacimientos y muertes ocurren al mismo tiempo. Dada la configuración actual del tablero de m x n, debes devolver el siguiente estado.

## Ejemplos

### Ejemplo 1:

**Entrada:** tablero = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
**Salida:** [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

### Ejemplo 2:

**Entrada:** tablero = [[1,1],[1,0]]
**Salida:** [[1,1],[1,1]]

## Restricciones

- m == tablero.length
- n == tablero[i].length
- 1 <= m, n <= 25
- tablero[i][j] es 0 o 1.

## Desafío adicional

1. ¿Podrías resolver el problema in situ? Recuerda que el tablero debe actualizarse simultáneamente: no puedes actualizar algunas células primero y luego usar sus valores actualizados para actualizar otras células.

2. En este problema, representamos el tablero usando un array 2D. En principio, el tablero es infinito, lo que causaría problemas cuando el área activa se acerca al borde del array (es decir, las células vivas alcanzan el borde). ¿Cómo abordarías estos problemas?