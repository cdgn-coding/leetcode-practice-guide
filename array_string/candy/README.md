# Repartiendo Caramelos

## Descripción

Hay n niños de pie en una fila. A cada niño se le asigna un valor de calificación dado en el arreglo de enteros `ratings`.

Estás repartiendo caramelos a estos niños sujeto a los siguientes requisitos:

- Cada niño debe tener al menos un caramelo.
- Los niños con una calificación más alta obtienen más caramelos que sus vecinos.

Devuelve el número mínimo de caramelos que necesitas tener para distribuir los caramelos a los niños.

## Ejemplos

### Ejemplo 1:

- Entrada: ratings = [1,0,2]
- Salida: 5
- Explicación: Puedes asignar al primer, segundo y tercer niño 2, 1 y 2 caramelos respectivamente.

### Ejemplo 2:

- Entrada: ratings = [1,2,2]
- Salida: 4
- Explicación: Puedes asignar al primer, segundo y tercer niño 1, 2 y 1 caramelos respectivamente. El tercer niño obtiene 1 caramelo porque satisface las dos condiciones anteriores.

## Restricciones

- `n == ratings.length`
- `1 <= n <= 2 * 10^4`
- `0 <= ratings[i] <= 2 * 10^4`