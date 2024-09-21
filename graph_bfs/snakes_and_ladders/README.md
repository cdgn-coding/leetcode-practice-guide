# Serpientes y Escaleras: El Camino Más Corto

## Descripción

Se te proporciona una matriz cuadrada de enteros `tablero` de tamaño n x n, donde las casillas están etiquetadas del 1 al n² en estilo bustrófedon, comenzando desde la esquina inferior izquierda del tablero (es decir, `tablero[n - 1][0]`) y alternando la dirección en cada fila.

Comienzas en la casilla 1 del tablero. En cada movimiento, partiendo de la casilla actual `curr`, haces lo siguiente:

1. Eliges una casilla de destino `next` con una etiqueta en el rango [curr + 1, min(curr + 6, n²)].
   - Esto simula el resultado de lanzar un dado de 6 caras estándar: siempre hay como máximo 6 destinos posibles, independientemente del tamaño del tablero.
2. Si `next` tiene una serpiente o una escalera, debes moverte al destino de esa serpiente o escalera. De lo contrario, te mueves a `next`.

El juego termina cuando llegas a la casilla n².

Una casilla del tablero en la fila r y columna c tiene una serpiente o una escalera si `tablero[r][c] != -1`. El destino de esa serpiente o escalera es `tablero[r][c]`. Las casillas 1 y n² no son puntos de inicio de ninguna serpiente o escalera.

Ten en cuenta que solo tomas una serpiente o escalera como máximo por movimiento. Si el destino de una serpiente o escalera es el inicio de otra serpiente o escalera, no sigues la serpiente o escalera subsiguiente.

Por ejemplo, supongamos que el tablero es [[-1,4],[-1,3]], y en el primer movimiento, tu casilla de destino es 2. Sigues la escalera a la casilla 3, pero no sigues la escalera subsiguiente a 4.

Devuelve el menor número de movimientos necesarios para llegar a la casilla n². Si no es posible llegar a la casilla, devuelve -1.

## Ejemplos

### Ejemplo 1:

**Entrada:** tablero = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
**Salida:** 4
**Explicación:** 
Al principio, comienzas en la casilla 1 (en la fila 5, columna 0).
Decides moverte a la casilla 2 y debes tomar la escalera a la casilla 15.
Luego decides moverte a la casilla 17 y debes tomar la serpiente a la casilla 13.
Después decides moverte a la casilla 14 y debes tomar la escalera a la casilla 35.
Finalmente decides moverte a la casilla 36, terminando el juego.
Este es el menor número posible de movimientos para llegar a la última casilla, por lo que se devuelve 4.

### Ejemplo 2:

**Entrada:** tablero = [[-1,-1],[-1,3]]
**Salida:** 1

## Restricciones

- n == tablero.length == tablero[i].length
- 2 <= n <= 20
- tablero[i][j] es -1 o está en el rango [1, n²].
- Las casillas etiquetadas como 1 y n² no son puntos de inicio de ninguna serpiente o escalera.