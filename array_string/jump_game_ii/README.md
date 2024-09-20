# Saltos Mínimos

## Descripción

Se te proporciona un arreglo de enteros `nums` de longitud `n`, indexado desde 0. Inicialmente, estás posicionado en `nums[0]`.

Cada elemento `nums[i]` representa la longitud máxima de un salto hacia adelante desde el índice `i`. En otras palabras, si estás en `nums[i]`, puedes saltar a cualquier `nums[i + j]` donde:

- 0 <= j <= nums[i]
- i + j < n

Devuelve el número mínimo de saltos necesarios para alcanzar `nums[n - 1]`. Los casos de prueba se generan de tal manera que puedas llegar a `nums[n - 1]`.

## Ejemplos

### Ejemplo 1

**Entrada:** nums = [2,3,1,1,4]
**Salida:** 2
**Explicación:** El número mínimo de saltos para llegar al último índice es 2. Salta 1 paso desde el índice 0 al 1, luego 3 pasos hasta el último índice.

### Ejemplo 2

**Entrada:** nums = [2,3,0,1,4]
**Salida:** 2

## Restricciones

- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 1000
- Se garantiza que puedes alcanzar `nums[n - 1]`.