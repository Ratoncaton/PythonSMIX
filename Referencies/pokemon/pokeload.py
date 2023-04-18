import os
import pickle
from requests_html import HTMLSession

pokemon_base = {
    "name": "",
    "type": None,
    "current_health": 100,
    "base_health": 100,
    "level": 1,
    "current_exp": 0,
    "attacks": None
}

URL_BASE = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk="

def get_pokemon(index):
    url = "{}{}".format(URL_BASE, index)
    session = HTMLSession()

    new_pokemon = pokemon_base.copy()
    pokemon_page = session.get(url)

    #get pokemon name
    new_pokemon["name"] = pokemon_page.html.find(".mini", first=True).text.split("\n")[0]

    #get pokemon type
    new_pokemon["type"] = []
    for img in pokemon_page.html.find(".pkmain", first=True).find(".bordeambos", first=True).find("img"):
        new_pokemon["type"].append(img.attrs["alt"])
    
    #get pokemon attacks
    new_pokemon["attacks"] = []
    for attack_item in pokemon_page.html.find(".pkmain")[-1].find("tr .check3"):
        attack = {
            "name": attack_item.find("td", first=True).find("a", first=True).text,
            "type": attack_item.find("td")[1].find("img", first=True).attrs["alt"],
            "damage": int(attack_item.find("td")[3].text.replace("--", "0")),
            "main_level": attack_item.find("th", first=True).text
        }
        new_pokemon["attacks"].append(attack)

    return new_pokemon


def get_all_pokemons():
    try:
        print("Cargando archivo de pokemons...")
        with open("pokefile.pkl", "rb") as pokefile:
            all_pokemons = pickle.load(pokefile)

    except FileNotFoundError:
        print("Archivo no encontrado, cargando de internet...")
        all_pokemons = []
        pokeloaded = 0
        for index in range(151):
            all_pokemons.append(get_pokemon(index + 1))
            pokeloaded += 1
            print(pokeloaded)
        
        with open("pokefile.txt", "wb") as pokefile:
            pickle.dump(all_pokemons, pokefile)

        print("\nTodos los pokemons han sido descargados")
    
    print("¡Lista de pokemons cargada!")
    return all_pokemons

def main():
    get_all_pokemons()

if __name__ == "__main__":
    main()
