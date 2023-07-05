"""Clase que permite acceder a las diferentes APIs por medio de funciones"""
import apis.pokemon_api
import apis.wizard_api
import apis.local_api
from abc import ABC, abstractmethod
from functools import cache
from itertoolz import frequencies


class ApiAccess(ABC):
    def __init__(self, nombre_api):
        self.nombre_api = nombre_api

    @abstractmethod
    def traer_datos(self, limit):
        pass

    @abstractmethod
    def traer_elemento(self, id_elemento):
        pass

    @abstractmethod
    def traer_llaves(self):
        pass

    @abstractmethod
    def filtrar_valores_por_llave(self, llave, valor):
        pass

    @abstractmethod
    def contar_por_llave(self):
        pass


class ApiAccessPokemon(ApiAccess):
    def __init__(self):
        super().__init__("pokemon")

    @cache
    def traer_datos(self, limit):
        return apis.pokemon_api.get_pokemon_list(limit)

    @cache
    def traer_elemento(self, id_elemento):
        return apis.pokemon_api.get_pokemon_by_id(id_elemento)

    @cache
    def traer_llaves(self):
        return apis.pokemon_api.get_pokemon_list(1)[0].keys()

    @cache
    def filtrar_valores_por_llave(self, llave, valor):
        datos = self.traer_datos(100)
        resultado = list(filter(lambda x: valor.lower() in x[llave].lower(),
                                datos))
        return resultado

    @cache
    def contar_por_llave(self, llave):
        datos = self.traer_datos(100)
        valores = []
        for dato in datos:
            valores.append(dato[llave])
        return frequencies(valores)


class ApiAccessWizard(ApiAccess):
    def __init__(self):
        super().__init__("wizard")

    @cache
    def traer_datos(self, limit=None):
        datos = apis.wizard_api.get_wizard_list()
        return datos[:limit:]

    @cache
    def traer_elemento(self, id_elemento):
        return apis.wizard_api.get_wizard_by_id(id_elemento)

    @cache
    def traer_llaves(self):
        elemento = self.traer_elemento(
            '0106fb32-b00d-4d70-9841-4b7c2d2cca71')
        llaves = list(filter(lambda x: not isinstance(elemento[x], list),
                             elemento.keys()))
        return llaves

    @cache
    def filtrar_valores_por_llave(self, llave, valor):
        datos = self.traer_datos()
        resultado = list(filter(lambda x: x[llave] is not None
                                and valor in x[llave],
                                datos))
        return resultado

    @cache
    def contar_por_llave(self, llave):
        datos = self.traer_datos(100)
        valores = []
        for dato in datos:
            valores.append(dato[llave])
        return frequencies(valores)


class ApiAccessLocal(ApiAccess):
    def __init__(self):
        super().__init__("local")

    @cache
    def traer_datos(self, limit=None):
        datos = apis.local_api.get_data_csv('apis/data.csv')['data']
        return datos[:limit:]

    @cache
    def traer_elemento(self, id_elemento):
        datos = self.traer_datos()
        return datos[id_elemento]

    @cache
    def traer_llaves(self):
        return self.traer_elemento(1).keys()

    @cache
    def filtrar_valores_por_llave(self, llave, valor):
        datos = self.traer_datos()
        resultado = list(filter(lambda x: valor.lower() in x[llave].lower(),
                                datos))
        return resultado

    @cache
    def contar_por_llave(self, llave):
        datos = self.traer_datos(100)
        valores = []
        for dato in datos:
            valores.append(dato[llave])
        return frequencies(valores)
