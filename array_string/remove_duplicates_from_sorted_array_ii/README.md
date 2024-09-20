# Eliminar Duplicados II

## Descripción

Dado un array de enteros `nums` ordenado en orden no decreciente, elimina algunos duplicados in-place de manera que cada elemento único aparezca como máximo dos veces. El orden relativo de los elementos debe mantenerse igual.

Dado que en algunos lenguajes es imposible cambiar la longitud del array, en su lugar debes colocar el resultado en la primera parte del array `nums`. Más formalmente, si hay `k` elementos después de eliminar los duplicados, entonces los primeros `k` elementos de `nums` deben contener el resultado final. No importa lo que dejes más allá de los primeros `k` elementos.

Retorna `k` después de colocar el resultado final en las primeras `k` posiciones de `nums`.

No asignes espacio adicional para otro array. Debes hacer esto modificando el array de entrada in-place con O(1) de memoria adicional.

## Juez Personalizado

El juez probará tu solución con el siguiente código:

```java
int[] nums = [...]; // Array de entrada
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
- Entrada: `nums = [1,1,1,2,2,3]`
- Salida: `5, nums = [1,1,2,2,3,_]`
- Explicación: Tu función debe retornar `k = 5`, con los primeros cinco elementos de `nums` siendo 1, 1, 2, 2 y 3 respectivamente. No importa lo que dejes más allá de `k` (de ahí los guiones bajos).

### Ejemplo 2:
- Entrada: `nums = [0,0,1,1,1,1,2,3,3]`
- Salida: `7, nums = [0,0,1,1,2,3,3,_,_]`
- Explicación: Tu función debe retornar `k = 7`, con los primeros siete elementos de `nums` siendo 0, 0, 1, 1, 2, 3 y 3 respectivamente. No importa lo que dejes más allá de `k` (de ahí los guiones bajos).

## Restricciones
- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` está ordenado en orden no decreciente.