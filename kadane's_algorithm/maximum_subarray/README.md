# Subarray con la Suma Máxima

## Descripción

Dado un array de enteros `nums`, encuentra el subarray con la suma más grande y devuelve su suma.

## Ejemplos

### Ejemplo 1:

**Entrada:** nums = [-2,1,-3,4,-1,2,1,-5,4]
**Salida:** 6
**Explicación:** El subarray [4,-1,2,1] tiene la suma más grande, que es 6.

### Ejemplo 2:

**Entrada:** nums = [1]
**Salida:** 1
**Explicación:** El subarray [1] tiene la suma más grande, que es 1.

### Ejemplo 3:

**Entrada:** nums = [5,4,-1,7,8]
**Salida:** 23
**Explicación:** El subarray [5,4,-1,7,8] tiene la suma más grande, que es 23.

## Restricciones

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

## Desafío adicional

Si ya has implementado la solución con complejidad O(n), intenta codificar otra solución utilizando el enfoque de "divide y vencerás", que es más sutil.