# Detectar Ciclo en una Lista Enlazada

## Descripción

Dado `head`, el nodo inicial de una lista enlazada, determina si la lista contiene un ciclo.

Se considera que existe un ciclo en una lista enlazada si hay algún nodo en la lista al que se puede volver siguiendo continuamente el puntero "siguiente". Internamente, `pos` se utiliza para denotar el índice del nodo al que se conecta el puntero "siguiente" del último nodo. Ten en cuenta que `pos` no se pasa como parámetro.

Devuelve `true` si existe un ciclo en la lista enlazada. De lo contrario, devuelve `false`.

## Ejemplos

### Ejemplo 1:

**Entrada:** head = [3,2,0,-4], pos = 1
**Salida:** true
**Explicación:** Existe un ciclo en la lista enlazada, donde el último nodo se conecta al segundo nodo (índice 1).

### Ejemplo 2:

**Entrada:** head = [1,2], pos = 0
**Salida:** true
**Explicación:** Existe un ciclo en la lista enlazada, donde el último nodo se conecta al primer nodo (índice 0).

### Ejemplo 3:

**Entrada:** head = [1], pos = -1
**Salida:** false
**Explicación:** No hay ciclo en la lista enlazada.

## Restricciones

- El número de nodos en la lista está en el rango [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos es -1 o un índice válido en la lista enlazada.

## Desafío adicional

¿Puedes resolver este problema utilizando O(1) (es decir, constante) de memoria?