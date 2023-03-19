import os
import random
import readchar

POS_X = 0
POS_Y = 1
NUM_MAP_OBJ = 11

obstacle_definition = """"\
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

my_position = [6, 3]
map_objects = []
tail_length = 0
tail = []
end_game = False
died = False

# Create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_HEIGHT = len(obstacle_definition)
MAP_WIdTH = len(obstacle_definition)

#Main Loop
while not end_game:
    os.system("cls")

    # Generate random objects in the map
    while len(map_objects) < NUM_MAP_OBJ:
        new_position = [random.randint(0, MAP_WIdTH - 1), random.randint(0, MAP_HEIGHT - 1)]
        if new_position not in map_objects != my_position \
                and obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            map_objects.append(new_position)

    # Draw Map
    print("+" + "-" * MAP_WIdTH * 2 + "+")
    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for cordinate_x in range(MAP_WIdTH):

            char_to_draw = "  "
            object_in_cell = None
            tail_in_cell = None

            for map_object in map_objects:

                if map_object[POS_X] == cordinate_x and map_object[POS_Y] == cordinate_y:
                    char_to_draw = " *"
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[POS_X] == cordinate_x and tail_piece[POS_Y] == cordinate_y:
                    char_to_draw = " @"
                    tail_in_cell = tail_piece

            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = " @"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1

                if tail_in_cell:
                    end_game = True
                    died = True

            if obstacle_definition[cordinate_y][cordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * MAP_WIdTH * 2 + "+")

    # Ask user where he wants to move:

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

    elif direction == "t":
        end_game = True
    os.system("cls")

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position = new_position
if died:
    print("Has muerto")
