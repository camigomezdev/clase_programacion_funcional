import requests

# Api docs: https://pokeapi.co/

def get_pokemon_list(limit):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_list = pokemon_data["results"]
        return pokemon_list
    else:
        print("Error al obtener la lista de Pokémones.")
        return None

def get_pokemon_by_id(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        data = {
            "name": pokemon_data["name"],
            "id": pokemon_data["id"],
            "types": pokemon_data["types"],
        }
        return data
    else:
        print(f"Error al obtener los datos del Pokémon {pokemon_id}.")
        return None


if __name__ == "__main__":
    pokemon_id = 25  # ID del Pokémon Pikachu
    pokemon_data = get_pokemon_by_id(pokemon_id)
    print(pokemon_data)

    limit = 10
    pokemon_list = get_pokemon_list(limit)
    print(pokemon_list)
