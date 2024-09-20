# Índice H de un investigador

## Descripción

Dado un array de enteros `citations` donde `citations[i]` representa el número de citas que un investigador recibió por su i-ésimo artículo, devuelve el índice h del investigador.

De acuerdo con la definición de índice h en Wikipedia: El índice h se define como el máximo valor de h tal que el investigador dado ha publicado al menos h artículos que han sido citados al menos h veces cada uno.

## Ejemplos

### Ejemplo 1:

- Entrada: `citations = [3,0,6,1,5]`
- Salida: `3`
- Explicación: `[3,0,6,1,5]` significa que el investigador tiene 5 artículos en total y cada uno de ellos recibió 3, 0, 6, 1, 5 citas respectivamente. Dado que el investigador tiene 3 artículos con al menos 3 citas cada uno y los dos restantes con no más de 3 citas cada uno, su índice h es 3.

### Ejemplo 2:

- Entrada: `citations = [1,3,1]`
- Salida: `1`

## Restricciones

- `n == citations.length`
- `1 <= n <= 5000`
- `0 <= citations[i] <= 1000`