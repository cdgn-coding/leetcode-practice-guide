# Resumen de rangos

## Descripción

Se te proporciona un array de enteros únicos y ordenados llamado `nums`.

Un rango [a,b] es el conjunto de todos los enteros desde a hasta b (inclusive).

Tu tarea es devolver la lista más pequeña y ordenada de rangos que cubra exactamente todos los números en el array. Esto significa que cada elemento de `nums` debe estar cubierto por exactamente uno de los rangos, y no debe haber ningún entero x que esté en uno de los rangos pero no en `nums`.

Cada rango [a,b] en la lista debe ser presentado de la siguiente manera:

- "a->b" si a ≠ b
- "a" si a = b

## Ejemplos

### Ejemplo 1:

**Entrada:** nums = [0,1,2,4,5,7]
**Salida:** ["0->2","4->5","7"]
**Explicación:** Los rangos son:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

### Ejemplo 2:

**Entrada:** nums = [0,2,3,4,6,8,9]
**Salida:** ["0","2->4","6","8->9"]
**Explicación:** Los rangos son:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

## Restricciones

- 0 ≤ longitud de nums ≤ 20
- -2³¹ ≤ nums[i] ≤ 2³¹ - 1
- Todos los valores en nums son únicos.
- nums está ordenado en orden ascendente.