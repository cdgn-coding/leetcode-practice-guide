# Eliminar duplicados de un arreglo ordenado

## Descripción

Dado un arreglo de enteros `nums` ordenado en orden no decreciente, elimina los duplicados en el lugar de tal manera que cada elemento único aparezca solo una vez. El orden relativo de los elementos debe mantenerse igual. Luego, devuelve el número de elementos únicos en `nums`.

Considera que el número de elementos únicos de `nums` es `k`. Para ser aceptado, debes hacer lo siguiente:

- Cambiar el arreglo `nums` de tal manera que los primeros `k` elementos de `nums` contengan los elementos únicos en el orden en que estaban presentes inicialmente en `nums`. Los elementos restantes de `nums` no son importantes, así como el tamaño de `nums`.
- Devolver `k`.

## Juez personalizado

El juez probará tu solución con el siguiente código:

```java
int[] nums = [...]; // Arreglo de entrada
int[] expectedNums = [...]; // La respuesta esperada con la longitud correcta

int k = removeDuplicates(nums); // Llama a tu implementación

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

Si todas las aserciones pasan, entonces tu solución será aceptada.

## Ejemplos

### Ejemplo 1:

- Entrada: `nums = [1,1,2]`
- Salida: `2, nums = [1,2,_]`
- Explicación: Tu función debe devolver `k = 2`, con los primeros dos elementos de `nums` siendo `1` y `2` respectivamente. No importa lo que dejes más allá de la `k` devuelta (por eso son guiones bajos).

### Ejemplo 2:

- Entrada: `nums = [0,0,1,1,1,2,2,3,3,4]`
- Salida: `5, nums = [0,1,2,3,4,_,_,_,_,_]`
- Explicación: Tu función debe devolver `k = 5`, con los primeros cinco elementos de `nums` siendo `0`, `1`, `2`, `3` y `4` respectivamente. No importa lo que dejes más allá de la `k` devuelta (por eso son guiones bajos).

## Restricciones

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` está ordenado en orden no decreciente.