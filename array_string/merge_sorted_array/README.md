# Combinar Arreglos Ordenados

## Descripción

Se te proporcionan dos arreglos de enteros `nums1` y `nums2`, ordenados de forma no decreciente, y dos enteros `m` y `n`, que representan el número de elementos en `nums1` y `nums2` respectivamente.

Tu objetivo es combinar `nums1` y `nums2` en un solo arreglo ordenado de forma no decreciente.

El arreglo final ordenado no debe ser devuelto por la función, sino que debe almacenarse dentro del arreglo `nums1`. Para acomodar esto, `nums1` tiene una longitud de `m + n`, donde los primeros `m` elementos denotan los elementos que deben combinarse, y los últimos `n` elementos se establecen en 0 y deben ignorarse. `nums2` tiene una longitud de `n`.

## Ejemplos

### Ejemplo 1:

- Entrada: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
- Salida: [1,2,2,3,5,6]
- Explicación: Los arreglos que estamos combinando son [1,2,3] y [2,5,6].
  El resultado de la combinación es [1,2,2,3,5,6], donde los elementos subrayados provienen de nums1.

### Ejemplo 2:

- Entrada: nums1 = [1], m = 1, nums2 = [], n = 0
- Salida: [1]
- Explicación: Los arreglos que estamos combinando son [1] y [].
  El resultado de la combinación es [1].

### Ejemplo 3:

- Entrada: nums1 = [0], m = 0, nums2 = [1], n = 1
- Salida: [1]
- Explicación: Los arreglos que estamos combinando son [] y [1].
  El resultado de la combinación es [1].
  Ten en cuenta que debido a que m = 0, no hay elementos en nums1. El 0 solo está ahí para asegurar que el resultado de la combinación pueda encajar en nums1.

## Restricciones

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

## Seguimiento

¿Puedes idear un algoritmo que se ejecute en tiempo O(m + n)?