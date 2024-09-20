# Suma de Tres Números

## Descripción

Dado un array de enteros `nums`, devuelve todos los tripletes `[nums[i], nums[j], nums[k]]` tales que `i != j`, `i != k`, y `j != k`, y `nums[i] + nums[j] + nums[k] == 0`.

Ten en cuenta que el conjunto de soluciones no debe contener tripletes duplicados.

## Ejemplos

### Ejemplo 1:

**Entrada:** nums = [-1,0,1,2,-1,-4]
**Salida:** [[-1,-1,2],[-1,0,1]]
**Explicación:** 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
Los tripletes distintos son [-1,0,1] y [-1,-1,2].
Observa que el orden de la salida y el orden de los tripletes no importa.

### Ejemplo 2:

**Entrada:** nums = [0,1,1]
**Salida:** []
**Explicación:** El único triplete posible no suma 0.

### Ejemplo 3:

**Entrada:** nums = [0,0,0]
**Salida:** [[0,0,0]]
**Explicación:** El único triplete posible suma 0.

## Restricciones

- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5