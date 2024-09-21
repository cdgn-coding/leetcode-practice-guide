# Entrelazado de Cadenas

## Descripción

Dadas las cadenas s1, s2 y s3, determina si s3 se puede formar mediante el entrelazado de s1 y s2.

Un entrelazado de dos cadenas s y t es una configuración donde s y t se dividen en n y m subcadenas respectivamente, de tal manera que:

- s = s1 + s2 + ... + sn
- t = t1 + t2 + ... + tm
- |n - m| <= 1

El entrelazado resultante es s1 + t1 + s2 + t2 + s3 + t3 + ... o t1 + s1 + t2 + s2 + t3 + s3 + ...

Nota: a + b representa la concatenación de las cadenas a y b.

## Ejemplos

### Ejemplo 1:

**Entrada:** s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
**Salida:** true
**Explicación:** Una forma de obtener s3 es:
Dividir s1 en s1 = "aa" + "bc" + "c", y s2 en s2 = "dbbc" + "a".
Entrelazando las dos divisiones, obtenemos "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Como s3 se puede obtener entrelazando s1 y s2, devolvemos true.

### Ejemplo 2:

**Entrada:** s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
**Salida:** false
**Explicación:** Observa que es imposible entrelazar s2 con cualquier otra cadena para obtener s3.

### Ejemplo 3:

**Entrada:** s1 = "", s2 = "", s3 = ""
**Salida:** true

## Restricciones

- 0 <= s1.length, s2.length <= 100
- 0 <= s3.length <= 200
- s1, s2 y s3 contienen solo letras minúsculas del alfabeto inglés.

## Desafío adicional

¿Podrías resolver este problema utilizando solo O(s2.length) de espacio adicional en memoria?