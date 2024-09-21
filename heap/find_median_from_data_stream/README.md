# Buscador de la Mediana

## Descripción

La mediana es el valor central en una lista ordenada de números enteros. Si el tamaño de la lista es par, no hay un valor central único, y la mediana se calcula como la media de los dos valores centrales.

Por ejemplo:
- Para `arr = [2,3,4]`, la mediana es 3.
- Para `arr = [2,3]`, la mediana es (2 + 3) / 2 = 2.5.

Implementa la clase `MedianFinder` con las siguientes funciones:

- `MedianFinder()`: Inicializa el objeto MedianFinder.
- `void addNum(int num)`: Añade el número entero `num` del flujo de datos a la estructura de datos.
- `double findMedian()`: Devuelve la mediana de todos los elementos añadidos hasta el momento. Se aceptarán respuestas con un margen de error de 10^-5 respecto al valor real.

## Ejemplo

```
Entrada
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]

Salida
[null, null, null, 1.5, null, 2.0]

Explicación
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // devuelve 1.5 (es decir, (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // devuelve 2.0
```

## Restricciones

- -10^5 <= num <= 10^5
- Habrá al menos un elemento en la estructura de datos antes de llamar a findMedian.
- Se realizarán como máximo 5 * 10^4 llamadas a addNum y findMedian.

## Desafíos adicionales

1. Si todos los números enteros del flujo están en el rango [0, 100], ¿cómo optimizarías tu solución?
2. Si el 99% de todos los números enteros del flujo están en el rango [0, 100], ¿cómo optimizarías tu solución?