# Máximo de puntos en una línea recta

## Descripción

Se te proporciona un array de puntos donde `points[i] = [xi, yi]` representa un punto en el plano cartesiano X-Y. Tu tarea es determinar el número máximo de puntos que se encuentran en una misma línea recta.

## Ejemplos

### Ejemplo 1:

**Entrada:** points = [[1,1],[2,2],[3,3]]
**Salida:** 3

### Ejemplo 2:

**Entrada:** points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
**Salida:** 4

## Restricciones

- 1 <= points.length <= 300
- points[i].length == 2
- -10^4 <= xi, yi <= 10^4
- Todos los puntos son únicos.

## Notas

- Considera cómo manejar eficientemente las pendientes entre puntos.
- Ten en cuenta los casos especiales, como líneas verticales o puntos coincidentes.
- La precisión en los cálculos puede ser crucial para la correcta resolución del problema.