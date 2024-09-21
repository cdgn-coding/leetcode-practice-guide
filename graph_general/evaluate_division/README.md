# Evaluación de División

## Descripción

Se te proporciona un array de pares de variables `ecuaciones` y un array de números reales `valores`, donde `ecuaciones[i] = [Ai, Bi]` y `valores[i]` representan la ecuación `Ai / Bi = valores[i]`. Cada `Ai` o `Bi` es una cadena que representa una variable única.

También se te dan algunas consultas, donde `consultas[j] = [Cj, Dj]` representa la j-ésima consulta en la que debes encontrar la respuesta para `Cj / Dj = ?`.

Devuelve las respuestas a todas las consultas. Si no se puede determinar una única respuesta, devuelve -1.0.

**Nota:** La entrada siempre es válida. Puedes asumir que la evaluación de las consultas no resultará en una división por cero y que no hay contradicciones.

**Nota:** Las variables que no aparecen en la lista de ecuaciones están indefinidas, por lo que no se puede determinar la respuesta para ellas.

## Ejemplos

### Ejemplo 1:

**Entrada:** 
- ecuaciones = [["a","b"],["b","c"]]
- valores = [2.0,3.0]
- consultas = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

**Salida:** [6.00000,0.50000,-1.00000,1.00000,-1.00000]

**Explicación:** 
Dado: a / b = 2.0, b / c = 3.0
Las consultas son: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
Se devuelve: [6.0, 0.5, -1.0, 1.0, -1.0]
Nota: x está indefinida => -1.0

### Ejemplo 2:

**Entrada:**
- ecuaciones = [["a","b"],["b","c"],["bc","cd"]]
- valores = [1.5,2.5,5.0]
- consultas = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

**Salida:** [3.75000,0.40000,5.00000,0.20000]

### Ejemplo 3:

**Entrada:**
- ecuaciones = [["a","b"]]
- valores = [0.5]
- consultas = [["a","b"],["b","a"],["a","c"],["x","y"]]

**Salida:** [0.50000,2.00000,-1.00000,-1.00000]

## Restricciones

- 1 <= ecuaciones.length <= 20
- ecuaciones[i].length == 2
- 1 <= Ai.length, Bi.length <= 5
- valores.length == ecuaciones.length
- 0.0 < valores[i] <= 20.0
- 1 <= consultas.length <= 20
- consultas[i].length == 2
- 1 <= Cj.length, Dj.length <= 5
- Ai, Bi, Cj, Dj consisten en letras minúsculas del inglés y dígitos.