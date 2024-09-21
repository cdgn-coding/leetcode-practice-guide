# Mutación mínima de genes

## Descripción

Una cadena genética puede representarse mediante una secuencia de 8 caracteres, utilizando únicamente las letras 'A', 'C', 'G' y 'T'.

Imagina que necesitamos investigar una mutación desde un gen inicial `startGene` hasta un gen final `endGene`. Definimos una mutación como el cambio de un solo carácter en la cadena genética.

Por ejemplo, "AACCGGTT" --> "AACCGGTA" se considera una mutación.

Además, contamos con un banco genético `bank` que registra todas las mutaciones válidas. Para que una cadena genética sea válida, debe estar presente en este banco.

Dado el gen inicial `startGene`, el gen final `endGene` y el banco genético `bank`, debes determinar el número mínimo de mutaciones necesarias para transformar `startGene` en `endGene`. Si no es posible realizar esta transformación, devuelve -1.

Es importante tener en cuenta que el gen inicial se considera válido por defecto, por lo que puede no estar incluido en el banco.

## Ejemplos

### Ejemplo 1:

Entrada: 
- startGene = "AACCGGTT"
- endGene = "AACCGGTA"
- bank = ["AACCGGTA"]

Salida: 1

### Ejemplo 2:

Entrada:
- startGene = "AACCGGTT"
- endGene = "AAACGGTA"
- bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]

Salida: 2

## Restricciones

- 0 <= bank.length <= 10
- startGene.length == endGene.length == bank[i].length == 8
- startGene, endGene y bank[i] contienen únicamente los caracteres ['A', 'C', 'G', 'T'].