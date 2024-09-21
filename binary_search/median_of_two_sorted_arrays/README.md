# Mediana de dos arreglos ordenados

## Descripción

Dados dos arreglos ordenados `nums1` y `nums2` de tamaños `m` y `n` respectivamente, devuelve la mediana de los dos arreglos ordenados.

La complejidad temporal del algoritmo debe ser O(log (m+n)).

## Ejemplos

### Ejemplo 1:

**Entrada:** nums1 = [1,3], nums2 = [2]
**Salida:** 2.00000
**Explicación:** El arreglo combinado sería [1,2,3] y la mediana es 2.

### Ejemplo 2:

**Entrada:** nums1 = [1,2], nums2 = [3,4]
**Salida:** 2.50000
**Explicación:** El arreglo combinado sería [1,2,3,4] y la mediana es (2 + 3) / 2 = 2.5.

## Restricciones

- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6