# Salto a Posición

## Descripción

Se te proporciona un arreglo de enteros llamado `nums`. Inicialmente estás posicionado en el primer índice del arreglo, y cada elemento del arreglo representa la longitud máxima de salto que puedes realizar desde esa posición.

Debes determinar si es posible llegar al último índice del arreglo. Retorna `true` si puedes alcanzar el último índice, o `false` en caso contrario.

## Ejemplos

### Ejemplo 1:

- Entrada: `nums = [2,3,1,1,4]`
- Salida: `true`
- Explicación: Puedes saltar 1 paso desde el índice 0 al 1, luego 3 pasos hasta el último índice.

### Ejemplo 2:

- Entrada: `nums = [3,2,1,0,4]`
- Salida: `false`
- Explicación: Siempre llegarás al índice 3, sin importar los saltos que realices. La longitud máxima de salto en ese índice es 0, lo que hace imposible alcanzar el último índice.

## Restricciones

- El arreglo `nums` tendrá una longitud entre 1 y 10^4 (inclusive).
- Cada elemento de `nums` estará entre 0 y 10^5 (inclusive).