# Incremento de un Número Grande

## Descripción

Se te proporciona un número entero grande representado como un arreglo de enteros llamado `digits`, donde cada `digits[i]` es el i-ésimo dígito del número. Los dígitos están ordenados de izquierda a derecha, del más significativo al menos significativo. El número grande no contiene ceros a la izquierda.

Tu tarea es incrementar este número grande en uno y devolver el arreglo resultante de dígitos.

## Ejemplos

### Ejemplo 1:

**Entrada:** digits = [1,2,3]
**Salida:** [1,2,4]
**Explicación:** El arreglo representa el número 123.
Incrementar en uno resulta en 123 + 1 = 124.
Por lo tanto, el resultado debe ser [1,2,4].

### Ejemplo 2:

**Entrada:** digits = [4,3,2,1]
**Salida:** [4,3,2,2]
**Explicación:** El arreglo representa el número 4321.
Incrementar en uno resulta en 4321 + 1 = 4322.
Por lo tanto, el resultado debe ser [4,3,2,2].

### Ejemplo 3:

**Entrada:** digits = [9]
**Salida:** [1,0]
**Explicación:** El arreglo representa el número 9.
Incrementar en uno resulta en 9 + 1 = 10.
Por lo tanto, el resultado debe ser [1,0].

## Restricciones

- 1 <= longitud de digits <= 100
- 0 <= digits[i] <= 9
- El arreglo digits no contiene ceros a la izquierda.