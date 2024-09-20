# Atrapar Agua de Lluvia

## Descripción

Dados `n` enteros no negativos que representan un mapa de elevación donde el ancho de cada barra es 1, calcula cuánta agua puede atrapar después de llover.

## Ejemplos

### Ejemplo 1

- Entrada: `height = [0,1,0,2,1,0,1,3,2,1,2,1]`
- Salida: `6`
- Explicación: El mapa de elevación de arriba (sección negra) está representado por el arreglo `[0,1,0,2,1,0,1,3,2,1,2,1]`. En este caso, 6 unidades de agua de lluvia (sección azul) quedan atrapadas.

### Ejemplo 2

- Entrada: `height = [4,2,0,3,2,5]`
- Salida: `9`

## Restricciones

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`