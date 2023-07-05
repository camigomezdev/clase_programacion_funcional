"""
Módulo principal para interactuar con las APIs
"""
from api_access import ApiAccessPokemon, ApiAccessLocal, ApiAccessWizard
from functools import partial


if __name__ == '__main__':
    opcion = ''
    opcion2 = ''
    while opcion != 'q':
        print("\n¿Qué API quieres leer?")
        opcion = ''
        opcion2 = ''
        print("\n1) PokeAPI")
        print("2) WizardAPI")
        print("3) LocalAPI")
        print("q) Salir")
        while opcion != "q" and (not opcion.isdecimal()
                                 or int(opcion) > 3 or int(opcion) < 1):
            opcion = input("\nElige una opción del 1 al 3: ")
        match opcion:
            case "1":
                api = ApiAccessPokemon()
                busqueda_por_nombre = partial(
                    api.filtrar_valores_por_llave,
                    'name')
            case "2":
                api = ApiAccessWizard()
                busqueda_por_nombre = partial(
                    api.filtrar_valores_por_llave,
                    'name')
            case "3":
                api = ApiAccessLocal()
                busqueda_por_nombre = partial(
                    api.filtrar_valores_por_llave,
                    'nombre')
            case "q":
                break
        while opcion2 != 'a':
            opcion2 = ''
            print("\n1) Filtrar por nombre")
            print("2) Filtrado por llave custom")
            print("3) Conteo de valores por llave")
            print("a) Regresar al menu anterior")
            while opcion2 != "a" and (not opcion2.isdecimal()
                                      or int(opcion2) > 3 or int(opcion2) < 1):
                opcion2 = input("\nElige una opción del 1 al 3: ")
            match opcion2:
                case "1":
                    nombre = input("\nIntroduce el nombre a buscar: ")
                    print("\nResultados: ")
                    for resultado in busqueda_por_nombre(nombre):
                        print(resultado)
                    input("\nPresiona Enter para regresar al menú...\n")
                case "2":
                    print("\nElige una llave a filtrar:")
                    llaves = list(api.traer_llaves())
                    for llave in llaves:
                        print(f"{llaves.index(llave)+1}) {llave}")
                    print("a) Regresar al menu anterior")
                    opcion3 = ''
                    while opcion3 != "a" and (not opcion3.isdecimal()
                                              or int(opcion3) > len(
                                                  llaves) or int(
                                                      opcion3) < 1):
                        opcion3 = input("\nElige una llave a filtrar: ")
                    if opcion3 != 'a':
                        valor = input(f"\nIntroduce '{llaves[int(opcion3)-1]}'\
 a buscar: ")
                        for resultado in api.filtrar_valores_por_llave(
                                llaves[int(opcion3)-1], valor):
                            print(resultado)
                        input("\nPresiona Enter para regresar al menú...\n")
                case "3":
                    llaves = list(api.traer_llaves())
                    for llave in llaves:
                        print(f"{llaves.index(llave)+1}) {llave}")
                    print("a) Regresar al menu anterior")
                    opcion3 = ''
                    while opcion3 != "a" and (not opcion3.isdecimal()
                                              or int(opcion3) > len(
                                                  llaves) or int(
                                                      opcion3) < 1):
                        opcion3 = input("\nElige una llave: ")
                    if opcion3 != 'a':
                        print(api.contar_por_llave(llaves[int(opcion3)-1]))
                        input("\nPresiona Enter para regresar al menú...\n")
