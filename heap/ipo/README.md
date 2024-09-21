# Maximización del Capital para IPO

## Descripción

Supongamos que LeetCode está a punto de lanzar su Oferta Pública Inicial (IPO). Para vender sus acciones a un buen precio a los Capitalistas de Riesgo, LeetCode quiere trabajar en algunos proyectos para aumentar su capital antes de la IPO. Dado que sus recursos son limitados, solo puede completar como máximo k proyectos distintos antes de la IPO. Ayuda a LeetCode a diseñar la mejor manera de maximizar su capital total después de completar, como máximo, k proyectos distintos.

Se te proporcionan n proyectos, donde el i-ésimo proyecto tiene un beneficio neto de profits[i] y requiere un capital mínimo de capital[i] para iniciarlo.

Inicialmente, tienes un capital w. Cuando terminas un proyecto, obtienes su beneficio neto y este se suma a tu capital total.

Selecciona una lista de, como máximo, k proyectos distintos de los proyectos dados para maximizar tu capital final, y devuelve el capital máximo final.

Se garantiza que la respuesta cabe en un entero con signo de 32 bits.

## Ejemplos

### Ejemplo 1:

**Entrada:** k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
**Salida:** 4
**Explicación:** 
Como tu capital inicial es 0, solo puedes comenzar el proyecto en el índice 0.
Después de terminarlo, obtendrás un beneficio de 1 y tu capital será 1.
Con un capital de 1, puedes iniciar el proyecto en el índice 1 o el proyecto en el índice 2.
Como puedes elegir como máximo 2 proyectos, necesitas terminar el proyecto en el índice 2 para obtener el máximo capital.
Por lo tanto, el capital máximo final es 0 + 1 + 3 = 4.

### Ejemplo 2:

**Entrada:** k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
**Salida:** 6

## Restricciones

- 1 <= k <= 10^5
- 0 <= w <= 10^9
- n == profits.length
- n == capital.length
- 1 <= n <= 10^5
- 0 <= profits[i] <= 10^4
- 0 <= capital[i] <= 10^9