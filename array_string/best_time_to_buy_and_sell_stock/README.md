# Máximo Beneficio en Compra y Venta de Acciones

## Descripción

Se te proporciona un arreglo `prices` donde `prices[i]` representa el precio de una acción dada en el i-ésimo día.

Tu objetivo es maximizar tus ganancias eligiendo un día para comprar una acción y otro día diferente en el futuro para vender esa acción.

Devuelve la ganancia máxima que puedes obtener de esta transacción. Si no puedes obtener ninguna ganancia, devuelve 0.

## Ejemplos

### Ejemplo 1:

- Entrada: `prices = [7,1,5,3,6,4]`
- Salida: 5
- Explicación: Compra el día 2 (precio = 1) y vende el día 5 (precio = 6), obteniendo una ganancia de 6 - 1 = 5.
  Ten en cuenta que no está permitido comprar el día 2 y vender el día 1, ya que debes comprar antes de vender.

### Ejemplo 2:

- Entrada: `prices = [7,6,4,3,1]`
- Salida: 0
- Explicación: En este caso, no se realiza ninguna transacción y la ganancia máxima es 0.

## Restricciones

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`