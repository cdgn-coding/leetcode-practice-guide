# Máximo Beneficio en Transacciones Bursátiles

## Descripción

Se te proporciona un array de enteros `precios`, donde `precios[i]` representa el precio de una acción en el día i-ésimo, y un entero `k`.

Tu tarea es encontrar el máximo beneficio que puedes obtener. Puedes realizar como máximo `k` transacciones: es decir, puedes comprar como máximo `k` veces y vender como máximo `k` veces.

**Nota**: No puedes realizar múltiples transacciones simultáneamente (es decir, debes vender la acción antes de comprar nuevamente).

## Ejemplos

### Ejemplo 1:

**Entrada**: k = 2, precios = [2,4,1]
**Salida**: 2
**Explicación**: Compra en el día 1 (precio = 2) y vende en el día 2 (precio = 4), beneficio = 4-2 = 2.

### Ejemplo 2:

**Entrada**: k = 2, precios = [3,2,6,5,0,3]
**Salida**: 7
**Explicación**: Compra en el día 2 (precio = 2) y vende en el día 3 (precio = 6), beneficio = 6-2 = 4. Luego compra en el día 5 (precio = 0) y vende en el día 6 (precio = 3), beneficio = 3-0 = 3.

## Restricciones

- 1 <= k <= 100
- 1 <= precios.length <= 1000
- 0 <= precios[i] <= 1000