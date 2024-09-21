# Simplificación de Rutas de Archivo Unix

## Descripción

Se te proporciona una ruta absoluta para un sistema de archivos estilo Unix, que siempre comienza con una barra '/'. Tu tarea es transformar esta ruta absoluta en su versión canónica simplificada.

Las reglas de un sistema de archivos estilo Unix son las siguientes:

- Un punto simple '.' representa el directorio actual.
- Un doble punto '..' representa el directorio anterior/padre.
- Múltiples barras consecutivas como '//' y '///' se tratan como una sola barra '/'.
- Cualquier secuencia de puntos que no coincida con las reglas anteriores debe tratarse como un nombre válido de directorio o archivo. Por ejemplo, '...' y '....' son nombres válidos de directorio o archivo.

La ruta canónica simplificada debe seguir estas reglas:

- La ruta debe comenzar con una sola barra '/'.
- Los directorios dentro de la ruta deben estar separados por exactamente una barra '/'.
- La ruta no debe terminar con una barra '/', a menos que sea el directorio raíz.
- La ruta no debe tener ningún punto simple o doble ('.' y '..') utilizados para denotar directorios actuales o padres.

Devuelve la ruta canónica simplificada.

## Ejemplos

### Ejemplo 1:

Entrada: path = "/home/"
Salida: "/home"
Explicación: Se debe eliminar la barra final.

### Ejemplo 2:

Entrada: path = "/home//foo/"
Salida: "/home/foo"
Explicación: Las barras consecutivas múltiples se reemplazan por una sola.

### Ejemplo 3:

Entrada: path = "/home/user/Documents/../Pictures"
Salida: "/home/user/Pictures"
Explicación: Un doble punto ".." se refiere al directorio un nivel arriba (el directorio padre).

### Ejemplo 4:

Entrada: path = "/../"
Salida: "/"
Explicación: No es posible subir un nivel desde el directorio raíz.

### Ejemplo 5:

Entrada: path = "/.../a/../b/c/../d/./"
Salida: "/.../b/d"
Explicación: "..." es un nombre válido para un directorio en este problema.

## Restricciones

- 1 <= longitud de path <= 3000
- path consiste en letras inglesas, dígitos, punto '.', barra '/' o guión bajo '_'.
- path es una ruta Unix absoluta válida.