# Cambio Mínimo

## Descripción

Se te proporciona un array de enteros `monedas` que representa monedas de diferentes denominaciones y un entero `cantidad` que representa una cantidad total de dinero.

Devuelve el menor número de monedas necesarias para formar esa cantidad. Si no es posible formar la cantidad con ninguna combinación de las monedas disponibles, devuelve -1.

Puedes asumir que tienes una cantidad infinita de cada tipo de moneda.

## Ejemplos

### Ejemplo 1:

**Entrada:** monedas = [1,2,5], cantidad = 11
**Salida:** 3
**Explicación:** 11 = 5 + 5 + 1

### Ejemplo 2:

**Entrada:** monedas = [2], cantidad = 3
**Salida:** -1

### Ejemplo 3:

**Entrada:** monedas = [1], cantidad = 0
**Salida:** 0

## Restricciones

- 1 <= monedas.length <= 12
- 1 <= monedas[i] <= 2^31 - 1
- 0 <= cantidad <= 10^4