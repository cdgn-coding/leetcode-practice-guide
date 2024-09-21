# Cadenas Isomórficas

## Descripción

Dadas dos cadenas `s` y `t`, determina si son isomórficas.

Dos cadenas `s` y `t` son isomórficas si los caracteres en `s` pueden ser reemplazados para obtener `t`.

Todas las ocurrencias de un carácter deben ser reemplazadas por otro carácter, manteniendo el orden original. No se permite que dos caracteres diferentes se asignen al mismo carácter, pero un carácter puede asignarse a sí mismo.

## Ejemplos

### Ejemplo 1:

**Entrada:** s = "egg", t = "add"

**Salida:** true

**Explicación:**
Las cadenas s y t pueden hacerse idénticas mediante:
- Asignar 'e' a 'a'.
- Asignar 'g' a 'd'.

### Ejemplo 2:

**Entrada:** s = "foo", t = "bar"

**Salida:** false

**Explicación:**
Las cadenas s y t no pueden hacerse idénticas, ya que 'o' necesitaría ser asignado tanto a 'a' como a 'r'.

### Ejemplo 3:

**Entrada:** s = "paper", t = "title"

**Salida:** true

## Restricciones

- 1 <= s.length <= 5 * 10^4
- t.length == s.length
- s y t están compuestas por cualquier carácter ASCII válido.