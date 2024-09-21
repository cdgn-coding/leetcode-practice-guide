# Distancia de Edición

## Descripción

Dadas dos cadenas de texto `palabra1` y `palabra2`, devuelve el número mínimo de operaciones necesarias para convertir `palabra1` en `palabra2`.

Se permiten las siguientes tres operaciones en una palabra:

1. Insertar un carácter
2. Eliminar un carácter
3. Reemplazar un carácter

## Ejemplos

### Ejemplo 1:

**Entrada:** palabra1 = "caballo", palabra2 = "ros"
**Salida:** 3
**Explicación:**
caballo -> raballo (reemplazar 'c' por 'r')
raballo -> rallo (eliminar 'b')
rallo -> ros (eliminar 'l')

### Ejemplo 2:

**Entrada:** palabra1 = "intencion", palabra2 = "ejecucion"
**Salida:** 5
**Explicación:**
intencion -> intenion (eliminar 'c')
intenion -> entenion (reemplazar 'i' por 'e')
entenion -> extenion (reemplazar 'n' por 'x')
extenion -> ejecion (reemplazar 't' por 'j')
ejecion -> ejecucion (insertar 'u')

## Restricciones

- 0 <= longitud de palabra1, longitud de palabra2 <= 500
- palabra1 y palabra2 contienen solo letras minúsculas del alfabeto inglés.