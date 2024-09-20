# Estaciones de Gasolina Circulares

## Descripción

Hay `n` estaciones de gasolina a lo largo de una ruta circular, donde la cantidad de gasolina en la i-ésima estación es `gas[i]`.

Tienes un auto con un tanque de gasolina ilimitado y cuesta `cost[i]` de gasolina viajar desde la i-ésima estación hasta la siguiente estación `(i + 1)`. Comienzas el viaje con un tanque vacío en una de las estaciones de gasolina.

Dados dos arreglos de enteros `gas` y `cost`, devuelve el índice de la estación de gasolina inicial si puedes viajar alrededor del circuito una vez en el sentido de las agujas del reloj, de lo contrario devuelve `-1`. Si existe una solución, se garantiza que es única.

## Ejemplos

### Ejemplo 1:

- Entrada: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
- Salida: 3
- Explicación:
  - Comienza en la estación 3 (índice 3) y llena con 4 unidades de gasolina. Tu tanque = 0 + 4 = 4
  - Viaja a la estación 4. Tu tanque = 4 - 1 + 5 = 8
  - Viaja a la estación 0. Tu tanque = 8 - 2 + 1 = 7
  - Viaja a la estación 1. Tu tanque = 7 - 3 + 2 = 6
  - Viaja a la estación 2. Tu tanque = 6 - 4 + 3 = 5
  - Viaja a la estación 3. El costo es 5. Tu gasolina es justo suficiente para viajar de vuelta a la estación 3.
  - Por lo tanto, devuelve 3 como el índice inicial.

### Ejemplo 2:

- Entrada: gas = [2,3,4], cost = [3,4,3]
- Salida: -1
- Explicación:
  - No puedes comenzar en la estación 0 o 1, ya que no hay suficiente gasolina para viajar a la siguiente estación.
  - Comencemos en la estación 2 y llenemos con 4 unidades de gasolina. Tu tanque = 0 + 4 = 4
  - Viaja a la estación 0. Tu tanque = 4 - 3 + 2 = 3
  - Viaja a la estación 1. Tu tanque = 3 - 3 + 3 = 3
  - No puedes viajar de vuelta a la estación 2, ya que requiere 4 unidades de gasolina pero solo tienes 3.
  - Por lo tanto, no puedes viajar alrededor del circuito una vez sin importar donde comiences.

## Restricciones

- `n == gas.length == cost.length`
- `1 <= n <= 10^5`
- `0 <= gas[i], cost[i] <= 10^4`