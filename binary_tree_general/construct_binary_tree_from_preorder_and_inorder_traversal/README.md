# Reconstrucción de Árbol Binario a partir de Recorridos

## Descripción

Dados dos arreglos de enteros `preorden` e `inorden`, donde `preorden` representa el recorrido en preorden de un árbol binario e `inorden` representa el recorrido en inorden del mismo árbol, construye y devuelve el árbol binario correspondiente.

## Ejemplos

### Ejemplo 1:

**Entrada:** 
- preorden = [3,9,20,15,7]
- inorden = [9,3,15,20,7]

**Salida:** [3,9,20,null,null,15,7]

### Ejemplo 2:

**Entrada:**
- preorden = [-1]
- inorden = [-1]

**Salida:** [-1]

## Restricciones

- 1 ≤ longitud de preorden ≤ 3000
- longitud de inorden == longitud de preorden
- -3000 ≤ preorden[i], inorden[i] ≤ 3000
- Tanto preorden como inorden contienen valores únicos.
- Cada valor en inorden también aparece en preorden.
- Se garantiza que preorden es el recorrido en preorden del árbol.
- Se garantiza que inorden es el recorrido en inorden del árbol.