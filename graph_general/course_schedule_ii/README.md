# Orden de Cursos

## Descripción

Tienes que tomar un total de `numCursos` cursos, numerados del 0 al `numCursos - 1`. Se te proporciona un array `prerequisitos` donde `prerequisitos[i] = [ai, bi]` indica que debes tomar el curso `bi` antes de poder tomar el curso `ai`.

Por ejemplo, el par [0, 1] indica que para tomar el curso 0, primero debes completar el curso 1.

Tu tarea es devolver el orden en el que deberías tomar los cursos para completarlos todos. Si hay varias respuestas válidas, devuelve cualquiera de ellas. Si es imposible completar todos los cursos, devuelve un array vacío.

## Ejemplos

### Ejemplo 1:

**Entrada:** numCursos = 2, prerequisitos = [[1,0]]
**Salida:** [0,1]
**Explicación:** Hay un total de 2 cursos para tomar. Para tomar el curso 1, debes haber terminado el curso 0. Por lo tanto, el orden correcto de los cursos es [0,1].

### Ejemplo 2:

**Entrada:** numCursos = 4, prerequisitos = [[1,0],[2,0],[3,1],[3,2]]
**Salida:** [0,2,1,3]
**Explicación:** Hay un total de 4 cursos para tomar. Para tomar el curso 3, debes haber terminado los cursos 1 y 2. Ambos cursos 1 y 2 deben tomarse después de haber terminado el curso 0. Un orden correcto de los cursos es [0,1,2,3]. Otro orden correcto es [0,2,1,3].

### Ejemplo 3:

**Entrada:** numCursos = 1, prerequisitos = []
**Salida:** [0]

## Restricciones

- 1 <= numCursos <= 2000
- 0 <= prerequisitos.length <= numCursos * (numCursos - 1)
- prerequisitos[i].length == 2
- 0 <= ai, bi < numCursos
- ai != bi
- Todos los pares [ai, bi] son distintos.