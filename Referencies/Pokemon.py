import random
import os
import readchar

POS_X = 0
POS_Y = 1
NUM_ENTR_MAP = 6

my_position = [1, 1]
map_coach = []
end_game = False
lose_game = False
win = False
pokemon_lenght = 1
pok = []
combat = False

obstacle_definition = """\
       #######################
     #########################
             #################
######     #######     #######
  ###   #####   ####    ######
                              
####          ###     ###    #     
    ####  ###   ###         ##
#  ######  ##        ##  #  ##
        #    ####   ###  ###  
   ####        ###    #  #####
#  #  #  #  #  #  #  #  #  # #
                              
#####   #####  ######   #### #
                              
##############################\
"""

#Create obstacules
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_HEIGHT = len(obstacle_definition)
MAP_WIdTH = len(obstacle_definition)

#Create random coach
while len(map_coach) < NUM_ENTR_MAP:
    new_position = [random.randint(0, MAP_WIdTH - 1), random.randint(0, MAP_HEIGHT - 1)]
    if new_position not in map_coach and new_position != my_position and\
            obstacle_definition[new_position[POS_Y]][new_position[POS_X]]:
        map_coach.append(new_position)
#Main Loop
while not end_game:
    os.system("cls")
    #Draw Map
    print("+" + "-" * MAP_WIdTH * 2 + "+")
    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for cordinate_x in range(MAP_WIdTH):

            char_to_draw = "  "
            object_in_cell = None

            for map_trainers in map_coach:
                if map_trainers[POS_Y] == cordinate_y and map_trainers[POS_X] == cordinate_x:
                    char_to_draw = " &"
                    object_in_cell = map_trainers
            for pokemon_piece in pok:
                if pokemon_piece[POS_Y] == cordinate_y and pokemon_piece[POS_X] == cordinate_x:
                    char_to_draw = " *"
                    pokemon_in_cell = pokemon_piece
            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = " @"

                if object_in_cell:
                    map_coach.remove(object_in_cell)
                    combat = True

            if obstacle_definition[cordinate_y][cordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * MAP_WIdTH * 2 + "+")

    #Ask user where he wants to move

    direction = readchar.readchar().decode()

    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIdTH]
    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIdTH]
    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIdTH, my_position[POS_Y]]
    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIdTH, my_position[POS_Y]]

    elif direction == "r":
        end_game = True
        os.system("cls")

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            pok.insert(0, my_position.copy())
            pok = pok[:pokemon_lenght]
            my_position = new_position

    # Pokemon Combat

    if combat == True:
        os.system("cls")

        VIDA_INICIAL_PIKACHU = 150
        VIDA_INICIAL_SQUIRTLE = 150

        vida_pikachu = VIDA_INICIAL_PIKACHU
        vida_squirtle = VIDA_INICIAL_SQUIRTLE

        titulo = "¡You have started a fight against Squirtle!"
        print(titulo + "\n" + "-"*len(titulo) + "\n")

        while vida_squirtle > 0 and vida_pikachu > 0:

            #Turno squirtle

            print("Squirtle turn")
            squirtle_attack = random.randint(1, 5)
            if squirtle_attack == 1:
                vida_pikachu -= 10
                print("¡Squirtle has attacked with Water Gun!")
            elif squirtle_attack == 2:
                vida_pikachu -= 15
                print("¡Squirtle has attacked with HydroPump!")
            elif squirtle_attack == 3:
                vida_pikachu -= 5
                print("¡Squirtle has attacked with Bubble!")
            else:
                vida_squirtle += 8
                print("¡Squirtle has healed!")

            if vida_squirtle < 0:
                vida_squirtle = 0
            if vida_pikachu < 0:
                vida_squirtle = 0

            barra_vida_pika = int(vida_pikachu * 10 / VIDA_INICIAL_PIKACHU)
            print("Pikachu:   [{}{}] ({}/{})".format("*" * barra_vida_pika, " " * (10-barra_vida_pika), vida_pikachu, VIDA_INICIAL_PIKACHU))

            barra_vida_squirtle = int(vida_squirtle * 10 / VIDA_INICIAL_SQUIRTLE)
            print("Squirtle:   [{}{}] ({}/{})".format("*" * barra_vida_squirtle, " " * (10 - barra_vida_squirtle), vida_squirtle, VIDA_INICIAL_SQUIRTLE))

            input("Press enter to continue...\n\n")
            os.system("cls")

            #Turno pikachu
            pikachu_attack = None
            while pikachu_attack not in ["T", "W", "E", "H", "N"]:
                print("It's Pikachu's turn")
                pikachu_attack = input("¿What move do you want to do?: ([T]hunderShock, Thunder[W]ave, [E]lectroBall, [H]ealing, [N]othing): ")

            if pikachu_attack == "T":
                vida_squirtle -= 15
                print("¡Pikachu has attacked with ThunderShock!")
            elif pikachu_attack == "W":
                vida_squirtle -= 5
                print("¡Pikachu has attacked with ThunderWave!")
            elif pikachu_attack == "E":
                vida_squirtle -= 10
                print("¡Pikachu has attacked with ElectroBall!")
            elif pikachu_attack == "H":
                vida_pikachu += 8
                print("¿Pikachu has healed!")
            elif pikachu_attack == "N":
                print("You have done nothing")

            if vida_squirtle < 0:
                vida_squirtle = 0
            if vida_pikachu < 0:
                vida_squirtle = 0
            if vida_squirtle > 150:
                vida_squirtle = 150
            if vida_pikachu > 150:
                vida_pikachu = 150

            barra_vida_pika = int(vida_pikachu * 10 / VIDA_INICIAL_PIKACHU)
            print("Pikachu:   [{}{}] ({}/{})".format("*" * barra_vida_pika, " " * (10 - barra_vida_pika), vida_pikachu,
                                                     VIDA_INICIAL_PIKACHU))

            barra_vida_squirtle = int(vida_squirtle * 10 / VIDA_INICIAL_SQUIRTLE)
            print("Squirtle:   [{}{}] ({}/{})".format("*" * barra_vida_squirtle, " " * (10 - barra_vida_squirtle),
                                                      vida_squirtle, VIDA_INICIAL_SQUIRTLE))

            input("Press enter to continue...\n\n")
            os.system("cls")

        if vida_pikachu > vida_squirtle:
            combat = False
            print("You've won")
            os.system("cls")
        else:
            end_game = True
            lose_game = True

if lose_game == True:
    print("You have lost :(")
    end_game = True

elif end_game == True:
    print("You have exited the game")
elif win == True:
    print("¡You've won!")
    end_game = True






















