""" Este módulo contiene las funciones de ejercicios de práctica
    de la clase de programación funcional pt.1
"""


def doble(lista: list) -> list:
    """ Función que toma una lista de números y devuelve una
        nueva lista donde cada elemento sea el doble del valor original.

    Args:
        lista (list): Una lista de números

    Returns:
        list: Una lista con el doble de los valores de la lista original

    Ejemplos de uso:
    >>> doble([1, 2, 3, 4, 5])
    [2, 4, 6, 8, 10]
    """
    return list(map((lambda x: x*2), lista))


def mas_de_5_caracteres(lista: list) -> list:
    """ Función que toma una lista de palabras y devuelve
    una nueva lista que contiene sólo las palabras que tienen más de 5
    caracteres.

    Args:
        lista (list): lista con palabras

    Returns:
        list: lista que contiene sólo las palabras de más de 5 caracteres

    Ejemplos de uso:
    >>> mas_de_5_caracteres(['hola', 'parametro', 'lista', 'caracter'])
    ['parametro', 'caracter']
    """
    return list(filter((lambda x: len(x) > 5), lista))


def factorial(numero: int) -> int:
    """ Función recursiva que calcula el factorial de un número dado.

    Args:
        numero (int): número a calcular su factorial

    Returns:
        int: el factorial del número dado

    Ejemplos de uso:
    >>> factorial(5)
    120
    """
    if numero < 1:
        return 1
    else:
        return numero * factorial(numero - 1)


def todos_mayores_a_cero(lista: list) -> bool:
    """ Función que toma una lista de números y devuelve True si todos
        los elementos son mayores que 0, y False en caso contrario.

    Args:
        lista (list): lista de números.

    Returns:
        bool: True si todos los elementos son mayores a 0, False si no.

    Ejemplos de uso:
    >>> todos_mayores_a_cero([1, 2, 3, 4, 5])
    True
    """
    return len(lista) == len(list(filter((lambda x: x > 0), lista)))


def fibonacci(lugar_en_secuencia: int,
              diccionario_memoizacion: dict({0: 0, 1: 1})) -> int:
    """ Función que genera una secuencia de números Fibonacci utilizando
        recursión.

    Args:
        lugar_en_secuencia (int): un número indicando el último lugar en
        la secuencia Fibonacci que se calculará
        diccionario_memoizacion (dict): un diccionario para guardar los valores
        ya calculados en la secuencia, debe ser inicializado con {0: 0, 1: 1}

    Returns:
        int: el número en el lugar indicado de la secuencia Fibonacci

    Ejemplos de uso:
    >>> fibonacci(11, {0: 0, 1: 1})
    89
    """

    if lugar_en_secuencia in diccionario_memoizacion:
        return diccionario_memoizacion[lugar_en_secuencia]
    else:
        resultado = fibonacci(lugar_en_secuencia - 1,
                              diccionario_memoizacion) + fibonacci(
                                            lugar_en_secuencia - 2,
                                            diccionario_memoizacion)
        diccionario_memoizacion[lugar_en_secuencia] = resultado
        return resultado
