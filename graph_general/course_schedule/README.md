# Finalizando Cursos

## Descripción

Tienes que completar un total de `numCursos` cursos, numerados de 0 a `numCursos - 1`. Se te proporciona un arreglo `requisitos` donde `requisitos[i] = [ai, bi]` indica que debes tomar el curso `bi` antes de poder tomar el curso `ai`.

Por ejemplo, el par [0, 1] indica que para tomar el curso 0, primero debes completar el curso 1.

Devuelve `true` si es posible completar todos los cursos. En caso contrario, devuelve `false`.

## Ejemplos

### Ejemplo 1:

**Entrada:** numCursos = 2, requisitos = [[1,0]]
**Salida:** true
**Explicación:** Hay un total de 2 cursos para tomar. Para tomar el curso 1, debes haber terminado el curso 0. Por lo tanto, es posible.

### Ejemplo 2:

**Entrada:** numCursos = 2, requisitos = [[1,0],[0,1]]
**Salida:** false
**Explicación:** Hay un total de 2 cursos para tomar. Para tomar el curso 1, debes haber terminado el curso 0, y para tomar el curso 0, también debes haber terminado el curso 1. Por lo tanto, es imposible.

## Restricciones

- 1 <= numCursos <= 2000
- 0 <= requisitos.length <= 5000
- requisitos[i].length == 2
- 0 <= ai, bi < numCursos
- Todos los pares en requisitos[i] son únicos.