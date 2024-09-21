# Reventando globos con flechas

## Descripción del problema

En una pared plana que representa el plano XY, hay pegados unos globos esféricos. Los globos se representan como un array bidimensional de enteros llamado `points`, donde `points[i] = [xstart, xend]` denota un globo cuyo diámetro horizontal se extiende desde `xstart` hasta `xend`. No se conocen las coordenadas y exactas de los globos.

Se pueden disparar flechas verticalmente hacia arriba (en la dirección y positiva) desde diferentes puntos a lo largo del eje x. Un globo con `xstart` y `xend` es reventado por una flecha disparada en x si `xstart <= x <= xend`. No hay límite en el número de flechas que se pueden disparar. Una flecha disparada sigue viajando hacia arriba indefinidamente, reventando cualquier globo en su camino.

Dado el array `points`, devuelve el número mínimo de flechas que deben dispararse para reventar todos los globos.

## Ejemplos

### Ejemplo 1:

**Entrada:** points = [[10,16],[2,8],[1,6],[7,12]]
**Salida:** 2
**Explicación:** Los globos pueden ser reventados con 2 flechas:
- Disparar una flecha en x = 6, reventando los globos [2,8] y [1,6].
- Disparar una flecha en x = 11, reventando los globos [10,16] y [7,12].

### Ejemplo 2:

**Entrada:** points = [[1,2],[3,4],[5,6],[7,8]]
**Salida:** 4
**Explicación:** Se necesita disparar una flecha por cada globo, para un total de 4 flechas.

### Ejemplo 3:

**Entrada:** points = [[1,2],[2,3],[3,4],[4,5]]
**Salida:** 2
**Explicación:** Los globos pueden ser reventados con 2 flechas:
- Disparar una flecha en x = 2, reventando los globos [1,2] y [2,3].
- Disparar una flecha en x = 4, reventando los globos [3,4] y [4,5].

## Restricciones

- 1 <= points.length <= 10^5
- points[i].length == 2
- -2^31 <= xstart < xend <= 2^31 - 1