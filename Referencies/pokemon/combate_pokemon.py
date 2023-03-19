from ast import Return
from pprint import pprint
from pokeload import get_all_pokemons
import random
from time import sleep
import os


def get_player_profile(pokemon_list):
    return {
        "player_name": input("¿Cual es tu nombre? "),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)],
        "combats": 0,
        "pokeballs": 0,
        "health_potions": 0
    }


def any_player_pokemon_lives(player_profile):
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0


def choose_pokemon(player_profile):
    chosen = None

    while not chosen:
        print("Elige con que pokemon lucharas")
        for index in range(len(player_profile["pokemon_inventory"])):
            print("{} - {}".format(index, get_pokemon_info(player_profile["pokemon_inventory"][index])))
        
        try:
            return player_profile["pokemon_inventory"][int(input("¿Cual eliges? "))]
        
        except (ValueError, IndexError):
            print("Opcion invalida")
    


def get_pokemon_info(pokemon):
    return "{} | lvl {} | HP {}/{}".format(pokemon["name"], 
                                           pokemon["level"], 
                                           pokemon["current_health"], 
                                           pokemon["base_health"])


def player_attack(player_profile, player_pokemon, enemy_pokemon):

    for a in player_pokemon["attacks"]:
        attack_name = a["name"]
        attack_type = a["type"]
        attack_damage = a["damage"]
        attack_level = a["main_level"]

        print("Nombre: {} | Daño: {} | Tipo: {} | Nivel: {}".format(attack_name, attack_damage, attack_type, attack_level))
    
    choosen = None
    while not choosen:
        choosen = input("Ataque que quieras elegir: ").capitalize
        if choosen == a["name"]:
            choosen_pokemon = a
            enemy_pokemon["current_health"] -= choosen_pokemon["damage"]
            
        print(enemy_pokemon["current_health"])



        

    
    
    

def enemy_attack(enemy_pokemon, player_pokemon):
    for a in enemy_pokemon["attacks"]:
        attack_enemy = random.choice(a)

    input("¡{} ha atacado con {}!".format(enemy_pokemon["name"], attack_enemy["name"]))
    input("¡Te ha hecho {} de daño!".format(attack_enemy["damage"]))

    player_pokemon["current_health"] -= attack_enemy["damage"]




def assign_expirience(attack_history):
    for pokemon in attack_history:
        points = random.randint(1, 5)
        pokemon["current_exp"] += points

    while pokemon["current_exp"] > 20:
        pokemon["current_exp"] -= 20
        pokemon["level"] += 1
        pokemon["current_health"] = pokemon["base_health"]

        print("Tu pokemon ha subido de nivel {}".format(get_pokemon_info(pokemon)))


def capture_with_pokeball(player_profile, enemy_pokemon):
    end_capture = False
    if player_profile["pokeballs"] > 0:
        while not end_capture:
            print("Tienes {} pokeballs".format(player_profile["pokeballs"]))
            throw = input("Pulsa L para lanzar o pulsa C para cancelar la accion")
            while throw not in ["L", "C"]:
                throw = input("Pulsa L para lanzar o pulsa C para cancelar la accion")
            if throw == "C":
                end_capture = True
                break
            else:
                if enemy_pokemon["current_health"] == 100:
                    gotcha = little_probability(player_profile, enemy_pokemon)

                elif enemy_pokemon["current_health"] > 50 and enemy_pokemon["current_health"] < 80:
                    gotcha = mid_probability(player_profile, enemy_pokemon)

                else:
                    gotcha = big_probability(player_profile, enemy_pokemon)
    else:
        gotcha = False
        input("No tienes pokeballs para lanzar.... ")
    return gotcha

def little_probability(player_profile, enemy_pokemon):
    probability = range(5)
    if probability == random.choice(range(100)):
        print("¡El pokemon ha sido atrapado!")
        player_profile["pokemon_inventory"].append(enemy_pokemon)
        capture = True
        return capture
    else:
        print("No lo has capturado")
        if player_profile["pokeballs"] > 0:
            choose = input("Tienes {} pokeballs, ¿quieres seguir intentando? (S/N) ".format(player_profile["pokeballs"]))
            while choose not in ["S", "N"]:
                choose = input("Tienes {} pokeballs, ¿quieres seguir intentando? (S/N) ".format(player_profile["pokeballs"]))
            if choose == "S":    
                capture_with_pokeball(player_profile, enemy_pokemon)
            else:
                end_capture = True
        else:
            end_capture = True


def mid_probability(player_profile, enemy_pokemon):
    probability = range(25)
    if probability == random.choice(range(100)):
        print("¡El pokemon ha sido capturado!")
        player_profile["pokemon_inventory"].append(enemy_pokemon)
        capture = True
        return capture
    else:
        print("No lo has capturado")
        if player_profile["pokeballs"] > 0:
            choose = input("Tienes {} pokeballs, ¿quieres seguir intentando? (S/N) ".format(player_profile["pokeballs"]))
            while choose not in ["S", "N"]:
                choose = input("Tienes {} pokeballs, ¿quieres seguir intentando? (S/N) ".format(player_profile["pokeballs"]))
            if choose == "S":    
                capture_with_pokeball(player_profile, enemy_pokemon)
            else:
                end_capture = True
        else:
            end_capture = True


def big_probability(player_profile, enemy_pokemon):
    probability = range(6)
    if probability == random.choice(range(10)):
        print("¡El pokemon ha sido atrapado!")
        player_profile["pokemon_inventory"].append(enemy_pokemon)
        capture = True
        return capture
    else:
        print("No lo has capturado")
        if player_profile["pokeballs"] > 0:
            choose = input("Tienes {} pokeballs, ¿quieres seguir intentando? (S/N) ".format(player_profile["pokeballs"]))
            while choose not in ["S", "N"]:
                choose = input("Tienes {} pokeballs, ¿quieres seguir intentando? (S/N) ".format(player_profile["pokeballs"]))
            if choose == "S":    
                capture_with_pokeball(player_profile, enemy_pokemon)
            else:
                end_capture = True
        else:
            end_capture = True



def fight(player_profile, enemy_pokemon):
    print("-- NUEVO COMBATE --")
    player_pokemon = choose_pokemon(player_profile)
    print("Contrincantes: {} VS {}".format(get_pokemon_info(player_pokemon),
                                           get_pokemon_info(enemy_pokemon)))
    
    attack_history = []
    capture = False
    while any_player_pokemon_lives(player_profile) and enemy_pokemon["current_health"] > 0 and not capture:
        action = None
        while action not in ["A", "P", "V", "C"]:
            action = input("Que desea hacer: [A]tacar, [P]okeball, Pocion de [V]ida, [C]ambiar")
        
        if action == "A":
            player_attack(player_profile, player_pokemon, enemy_pokemon)
            attack_history.append(player_pokemon)
            enemy_attack(enemy_pokemon, player_pokemon)
        
        elif action == "P":
            #Si el usuario tiene pokeballs en el inventario se tira una, hay probabilidad de capturar
            #dependiendo de la salud del pokemon, si se captura se pasa al inventario con la misma vida
            capture = capture_with_pokeball(player_profile, enemy_pokemon)
        
        elif action == "V":
            cure_pokemon(player_profile, player_pokemon)
        
        elif action == "C":
            player_pokemon = choose_pokemon(player_profile)

        if player_pokemon["current_health"] == 0 and any_player_pokemon_lives(player_profile):
            player_pokemon = choose_pokemon(player_profile)
    
    if enemy_pokemon["current_health"] == 0:
        print("Has ganado")
        assign_expirience(attack_history)


    print("-- FIN DEL COMBATE --")

    input("Presiona ENTER para continuar")


def cure_pokemon(player_profile, player_pokemon):
    if player_profile["health_potions"] > 0:
        sleep(1)
        print("¡Tu pokemon se ha curado!")

        player_pokemon["current_health"] += 50
        if player_pokemon["current_health"] > player_pokemon["base_health"]:
            player_pokemon["current_health"] = player_pokemon["base_health"]


def item_lottery(player_profile):
    pokeball_probability = [15, 19, 3]
    health_probability = [6, 7, 8]

    input("Pulsa ENTER para girar la ruleta ")

    lucky_object = random.choice(range(20))
    if lucky_object == pokeball_probability:
        sleep(5)
        print("¡Te ha tocado una pokeball!")
        player_profile["pokeballs"] += 1
        input("Pulsa ENTER para continuar")
    
    elif lucky_object == health_probability:
        sleep(5)
        print("¡Te ha tocado una cura!")
        player_profile["health_potions"]
        input("Pulsa ENTER para continuar")
    
    else:
        sleep(5)
        print("No te ha tocado nada...")
        input("Pulsa ENTER para continuar")


def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)

    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(pokemon_list)
        os.system("cls")
        fight(player_profile, enemy_pokemon)
        item_lottery(player_profile)
    
    print("Has perdido en el combate numero {}".format(player_profile["combats"]))


if __name__ == '__main__':
    main()