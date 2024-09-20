# Producto de Array Excepto el Propio

## Descripción

Dado un array de enteros `nums`, devuelve un array `answer` tal que `answer[i]` sea igual al producto de todos los elementos de `nums` excepto `nums[i]`.

El producto de cualquier prefijo o sufijo de `nums` está garantizado que cabe en un entero de 32 bits.

Debes escribir un algoritmo que se ejecute en tiempo O(n) y sin usar la operación de división.

## Ejemplos

### Ejemplo 1:

- Entrada: `nums = [1,2,3,4]`
- Salida: `[24,12,8,6]`

### Ejemplo 2:

- Entrada: `nums = [-1,1,0,-3,3]`
- Salida: `[0,0,9,0,0]`

## Restricciones

- `2 <= nums.length <= 105`
- `-30 <= nums[i] <= 30`
- El producto de cualquier prefijo o sufijo de `nums` está garantizado que cabe en un entero de 32 bits.

## Seguimiento

¿Puedes resolver el problema con una complejidad de espacio adicional O(1)? (El array de salida no cuenta como espacio adicional para el análisis de complejidad de espacio).