**Ejercicios Prácticos:**

- Implementa una función para el llamado de una API especificada (PokeAPI, WizardAPI, LocalAPI).
- Utiliza la función `cache` o `lru_cache` para decorar la función y almacenar en caché el resultado para entradas de argumentos repetidos.
- Crea una función que filtre los datos retornados por la API dado una llave y un valor (key: value) dado.
- Crea funciones parciales con los filtros mas comunes.
- Crea una función que dado una llave, retorne un diccionario con los valores que puede tomar esa llave y la cantidad de cada uno de ellos que hay en la respuesta de la API. Ej. count_by_key("difficulty") R/ {"Unknown": 3, "Advanced": 8, "Moderate": 1}