# Construcción de un Árbol Binario a partir de Recorridos en Orden y Postorden

## Descripción

Se te proporcionan dos arreglos de enteros, `inorden` y `postorden`, que representan los recorridos en orden y postorden de un árbol binario, respectivamente. Tu tarea es reconstruir y devolver el árbol binario original.

## Ejemplos

### Ejemplo 1:

**Entrada:** 
- inorden = [9,3,15,20,7]
- postorden = [9,15,7,20,3]

**Salida:** [3,9,20,null,null,15,7]

### Ejemplo 2:

**Entrada:**
- inorden = [-1]
- postorden = [-1]

**Salida:** [-1]

## Restricciones

- 1 <= longitud de inorden <= 3000
- longitud de postorden == longitud de inorden
- -3000 <= inorden[i], postorden[i] <= 3000
- Los arreglos inorden y postorden contienen valores únicos.
- Cada valor en postorden también aparece en inorden.
- Se garantiza que inorden es el recorrido en orden del árbol.
- Se garantiza que postorden es el recorrido postorden del árbol.