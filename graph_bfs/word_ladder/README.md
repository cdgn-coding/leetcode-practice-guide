# Secuencia de Transformación de Palabras

## Descripción del Problema

Se define una secuencia de transformación desde una palabra inicial `palabraInicial` hasta una palabra final `palabraFinal` utilizando un diccionario `listaPalabras` como una serie de palabras `palabraInicial -> s1 -> s2 -> ... -> sk` que cumple las siguientes condiciones:

- Cada par de palabras adyacentes difiere en una sola letra.
- Cada `si` para 1 ≤ i ≤ k está en `listaPalabras`. Nótese que `palabraInicial` no necesita estar en `listaPalabras`.
- `sk` es igual a `palabraFinal`.

Dadas dos palabras, `palabraInicial` y `palabraFinal`, y un diccionario `listaPalabras`, devuelve el número de palabras en la secuencia de transformación más corta desde `palabraInicial` hasta `palabraFinal`, o 0 si no existe tal secuencia.

## Ejemplos

### Ejemplo 1:

**Entrada:** 
- palabraInicial = "hit"
- palabraFinal = "cog"
- listaPalabras = ["hot","dot","dog","lot","log","cog"]

**Salida:** 5

**Explicación:** Una secuencia de transformación más corta es "hit" -> "hot" -> "dot" -> "dog" -> "cog", que tiene una longitud de 5 palabras.

### Ejemplo 2:

**Entrada:**
- palabraInicial = "hit"
- palabraFinal = "cog"
- listaPalabras = ["hot","dot","dog","lot","log"]

**Salida:** 0

**Explicación:** La palabra final "cog" no está en listaPalabras, por lo tanto, no existe una secuencia de transformación válida.

## Restricciones

- 1 ≤ longitud de palabraInicial ≤ 10
- longitud de palabraFinal == longitud de palabraInicial
- 1 ≤ longitud de listaPalabras ≤ 5000
- longitud de listaPalabras[i] == longitud de palabraInicial
- palabraInicial, palabraFinal, y listaPalabras[i] consisten en letras minúsculas del alfabeto inglés.
- palabraInicial ≠ palabraFinal
- Todas las palabras en listaPalabras son únicas.