# Implementación de Potencia (pow)

## Descripción

Implementa la función pow(x, n), que calcula x elevado a la potencia n (es decir, x^n).

## Ejemplos

### Ejemplo 1:

**Entrada:** x = 2.00000, n = 10
**Salida:** 1024.00000

### Ejemplo 2:

**Entrada:** x = 2.10000, n = 3
**Salida:** 9.26100

### Ejemplo 3:

**Entrada:** x = 2.00000, n = -2
**Salida:** 0.25000
**Explicación:** 2^(-2) = 1/2^2 = 1/4 = 0.25

## Restricciones

- -100.0 < x < 100.0
- -2^31 <= n <= 2^31 - 1
- n es un número entero.
- O bien x no es cero, o n es mayor que 0.
- -10^4 <= x^n <= 10^4