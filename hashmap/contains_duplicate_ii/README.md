# Duplicados Cercanos

## Descripción

Dado un arreglo de enteros `nums` y un entero `k`, devuelve `true` si existen dos índices distintos `i` y `j` en el arreglo tales que `nums[i] == nums[j]` y `|i - j| <= k`.

## Ejemplos

### Ejemplo 1:

**Entrada:** nums = [1,2,3,1], k = 3
**Salida:** true

### Ejemplo 2:

**Entrada:** nums = [1,0,1,1], k = 1
**Salida:** true

### Ejemplo 3:

**Entrada:** nums = [1,2,3,1,2,3], k = 2
**Salida:** false

## Restricciones

- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 0 <= k <= 10^5