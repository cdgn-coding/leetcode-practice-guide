# Número Feliz

## Descripción

Escribe un algoritmo para determinar si un número `n` es feliz.

Un número feliz se define mediante el siguiente proceso:

1. Comenzando con cualquier entero positivo, reemplaza el número por la suma de los cuadrados de sus dígitos.
2. Repite el proceso hasta que el número sea igual a 1 (donde se detendrá), o entre en un ciclo infinito que no incluya el 1.

Los números para los cuales este proceso termina en 1 son considerados felices.

Devuelve `true` si `n` es un número feliz, y `false` en caso contrario.

## Ejemplos

### Ejemplo 1:

**Entrada:** n = 19
**Salida:** true
**Explicación:**
1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0² + 0² = 1

### Ejemplo 2:

**Entrada:** n = 2
**Salida:** false

## Restricciones

- 1 <= n <= 2³¹ - 1