# Eliminar Elemento

## Descripción

Dado un arreglo de enteros `nums` y un entero `val`, elimina todas las apariciones de `val` en `nums` en su lugar. El orden de los elementos puede ser cambiado. Luego, devuelve el número de elementos en `nums` que no son iguales a `val`.

Considera que el número de elementos en `nums` que no son iguales a `val` es `k`. Para que tu solución sea aceptada, debes hacer lo siguiente:

- Cambiar el arreglo `nums` de tal manera que los primeros `k` elementos de `nums` contengan los elementos que no son iguales a `val`. Los elementos restantes de `nums` no son importantes, así como el tamaño de `nums`.
- Devolver `k`.

### Juez Personalizado

El juez probará tu solución con el siguiente código:

```java
int[] nums = [...]; // Arreglo de entrada
int val = ...; // Valor a eliminar
int[] expectedNums = [...]; // La respuesta esperada con la longitud correcta.
                            // Está ordenada sin valores iguales a val.

int k = removeElement(nums, val); // Llama a tu implementación

assert k == expectedNums.length;
sort(nums, 0, k); // Ordena los primeros k elementos de nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
```

Si todas las aserciones pasan, entonces tu solución será aceptada.

## Ejemplos

### Ejemplo 1:

- Entrada: nums = [3,2,2,3], val = 3
- Salida: 2, nums = [2,2,_,_]
- Explicación: Tu función debe devolver k = 2, con los primeros dos elementos de nums siendo 2. No importa lo que dejes más allá de la k devuelta (de ahí los guiones bajos).

### Ejemplo 2:

- Entrada: nums = [0,1,2,2,3,0,4,2], val = 2
- Salida: 5, nums = [0,1,4,0,3,_,_,_]
- Explicación: Tu función debe devolver k = 5, con los primeros cinco elementos de nums conteniendo 0, 0, 1, 3 y 4. Ten en cuenta que los cinco elementos pueden ser devueltos en cualquier orden. No importa lo que dejes más allá de la k devuelta (de ahí los guiones bajos).

## Restricciones

- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100