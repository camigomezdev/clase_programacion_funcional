# Programación Funcional con Python

# Clase 1
Temas:
- Paradigmas de programación.
- Programación Funcional.
- Python como lenguaje Funcional.
- Lambdas.
- Maps y filters.

[Presentación Clase 1](https://drive.google.com/file/d/1H5lPeatAi-zg6bMCKXtR2YtC8yMNLIUI/view?usp=sharing)

**Ejercicios Prácticos:**

1. Implementa una función que tome una lista de números y devuelva una nueva lista
donde cada elemento sea el doble del valor original.
2. Implementa una función que tome una lista de palabras y devuelva una nueva lista que
contenga sólo las palabras que tienen más de 5 caracteres.
3. Implementa una función recursiva que calcula el factorial de un número dado.
4. Implementa una función que tome una lista de números y devuelva True si todos los
elementos son mayores que 0, y False en caso contrario.
5. Implementa una función que genere una secuencia de números Fibonacci utilizando
recursión.

# Clase 2
Temas:
- [Itertools](https://docs.python.org/3/library/itertools.html).
- [Functools](https://docs.python.org/3/library/functools.html).
- [Toolz](https://toolz.readthedocs.io/en/latest/api.html).

[Presentación Clase 2](https://drive.google.com/file/d/1mPpZdGrb1RXFpcUK_tkwHuo69RTICTKk/view?usp=sharing)

**Ejercicios Prácticos:**

- Implementa una función para el llamado de una API especificada (PokeAPI, WizardAPI, LocalAPI).
- Utiliza la función `cache` o `lru_cache` para decorar la función y almacenar en caché el resultado para entradas de argumentos repetidos.
- Crea una función que filtre los datos retornados por la API dado una llave y un valor (key: value) dado.
- Crea funciones parciales con los filtros mas comunes.
- Crea una función que dado una llave, retorne un diccionario con los valores que puede tomar esa llave y la cantidad de cada uno de ellos que hay en la respuesta de la API. Ej. count_by_key("difficulty") R/ {"Unknown": 3, "Advanced": 8, "Moderate": 1}
