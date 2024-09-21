# El Ladrón Profesional

## Descripción

Eres un ladrón profesional planeando robar casas a lo largo de una calle. Cada casa tiene una cierta cantidad de dinero guardado. La única restricción que te impide robar todas las casas es que las casas adyacentes tienen sistemas de seguridad conectados entre sí, y se alertará automáticamente a la policía si se entra en dos casas adyacentes la misma noche.

Dado un arreglo de enteros `nums` que representa la cantidad de dinero en cada casa, devuelve la cantidad máxima de dinero que puedes robar esta noche sin alertar a la policía.

## Ejemplos

### Ejemplo 1:

**Entrada:** nums = [1,2,3,1]
**Salida:** 4
**Explicación:** Roba la casa 1 (dinero = 1) y luego roba la casa 3 (dinero = 3).
La cantidad total que puedes robar es 1 + 3 = 4.

### Ejemplo 2:

**Entrada:** nums = [2,7,9,3,1]
**Salida:** 12
**Explicación:** Roba la casa 1 (dinero = 2), roba la casa 3 (dinero = 9) y roba la casa 5 (dinero = 1).
La cantidad total que puedes robar es 2 + 9 + 1 = 12.

## Restricciones

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400