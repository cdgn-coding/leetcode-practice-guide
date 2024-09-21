# Inversión de Bits

## Descripción

Invierte los bits de un entero sin signo de 32 bits dado.

**Nota:**
En algunos lenguajes, como Java, no existe el tipo de entero sin signo. En estos casos, tanto la entrada como la salida se darán como enteros con signo. Esto no debería afectar tu implementación, ya que la representación binaria interna del entero es la misma, sea con o sin signo.

En Java, el compilador representa los enteros con signo utilizando la notación de complemento a dos. Por lo tanto, en el Ejemplo 2, la entrada representa el entero con signo -3 y la salida representa el entero con signo -1073741825.

## Ejemplos

### Ejemplo 1:

**Entrada:** n = 00000010100101000001111010011100
**Salida:**    964176192 (00111001011110000010100101000000)
**Explicación:** La cadena binaria de entrada 00000010100101000001111010011100 representa el entero sin signo 43261596, por lo que se devuelve 964176192, cuya representación binaria es 00111001011110000010100101000000.

### Ejemplo 2:

**Entrada:** n = 11111111111111111111111111111101
**Salida:**   3221225471 (10111111111111111111111111111111)
**Explicación:** La cadena binaria de entrada 11111111111111111111111111111101 representa el entero sin signo 4294967293, por lo que se devuelve 3221225471, cuya representación binaria es 10111111111111111111111111111111.

## Restricciones

- La entrada debe ser una cadena binaria de longitud 32.

## Optimización

**Pregunta adicional:** Si esta función se llama muchas veces, ¿cómo la optimizarías?