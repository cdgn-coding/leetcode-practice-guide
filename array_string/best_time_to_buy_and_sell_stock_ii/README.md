# Mejor Ganancia en el Comercio de Acciones II

## Descripción

Se te proporciona un arreglo de enteros `prices` donde `prices[i]` representa el precio de una acción dada en el i-ésimo día.

En cada día, puedes decidir comprar y/o vender la acción. Solo puedes mantener como máximo una acción en cualquier momento. Sin embargo, puedes comprarla y luego venderla inmediatamente en el mismo día.

Encuentra y devuelve la ganancia máxima que puedes obtener.

## Ejemplos

### Ejemplo 1:

- Entrada: `prices = [7,1,5,3,6,4]`
- Salida: `7`
- Explicación: 
  - Compra el día 2 (precio = 1) y vende el día 3 (precio = 5), ganancia = 5-1 = 4.
  - Luego, compra el día 4 (precio = 3) y vende el día 5 (precio = 6), ganancia = 6-3 = 3.
  - La ganancia total es 4 + 3 = 7.

### Ejemplo 2:

- Entrada: `prices = [1,2,3,4,5]`
- Salida: `4`
- Explicación:
  - Compra el día 1 (precio = 1) y vende el día 5 (precio = 5), ganancia = 5-1 = 4.
  - La ganancia total es 4.

### Ejemplo 3:

- Entrada: `prices = [7,6,4,3,1]`
- Salida: `0`
- Explicación:
  - No hay forma de obtener una ganancia positiva, por lo que nunca compramos la acción para obtener la ganancia máxima de 0.

## Restricciones

- `1 <= prices.length <= 3 * 10^4`
- `0 <= prices[i] <= 10^4`