import requests

# Wizard API docs: https://wizard-world-api.herokuapp.com/swagger/index.html

def get_wizard_list():
    url = f"https://wizard-world-api.herokuapp.com/elixirs"
    response = requests.get(url)

    if response.status_code == 200:
        wizard_data = response.json()
        return list(wizard_data)
    else:
        print("Error al obtener la lista de Pokémones.")
        return None

def get_wizard_by_id(wizard_id):
    url = f"https://wizard-world-api.herokuapp.com/elixirs/{wizard_id}"
    response = requests.get(url)

    if response.status_code == 200:
        wizard_data = response.json()
        return wizard_data
    else:
        print(f"Error al obtener los datos del Pokémon {wizard_id}.")
        return None


if __name__ == "__main__":
    wizard_id = "0106fb32-b00d-4d70-9841-4b7c2d2cca71"
    wizard_data = get_wizard_by_id(wizard_id)
    print(wizard_data)

    limit = 10
    wizard_list = get_wizard_list()
    print(wizard_list)
