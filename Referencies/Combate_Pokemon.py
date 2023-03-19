import random
import os


VIDA_INICIAL_PIKACHU = 90
VIDA_INICIAL_SQUIRTLE = 80

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

print("¡Bienvenido al combate pokemon!")
titulo = "Ahora te enfrentaras con tu oponente, ¡Un pikachu!"
print(titulo + "\n" + "-"*len(titulo) + "\n")

while vida_squirtle > 0 and vida_pikachu > 0:
    #Combates
    print("Turno de pikachu")
    ataque_pikachu = random.randint(1, 2)
    if ataque_pikachu == 1:
        print("¡Pikachu ataca con Bola Voltio!")
        vida_squirtle -= 10
    else:
        print("¡Pikachu ataca con Onda trueno!")
        vida_squirtle -= 8

    if vida_squirtle < 0:
        vida_squirtle = 0
    if vida_pikachu <0:
        vida_squirtle = 0

    barra_vida_pika = int(vida_pikachu * 10 / VIDA_INICIAL_PIKACHU)
    print("Pikachu:   [{}{}] ({}/{})".format("*" * barra_vida_pika, " " * (10-barra_vida_pika), vida_pikachu, VIDA_INICIAL_PIKACHU))

    barra_vida_squirtle = int(vida_squirtle * 10 / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:   [{}{}] ({}/{})".format("*" * barra_vida_squirtle, " " * (10 - barra_vida_squirtle), vida_squirtle, VIDA_INICIAL_SQUIRTLE))


    input("Pulsa enter para continuar...\n\n")
    os.system("cls")




    #Turno squirtle

    ataque_squirtle = None
    while ataque_squirtle not in ["P", "A", "B", "N"]:
        ataque_squirtle = input("¿Que ataque desea realizar? [P]lacaje, Pistola [A]gua, [B]urbuja, [N]ada: ")

    if ataque_squirtle == "P":
        print("¡Squirtle ataca con Placaje!")
        vida_pikachu -= 8
    if ataque_squirtle == "A":
        print("¡Squirtle ataca con Pistola agua!")
        vida_pikachu -= 12
    if ataque_squirtle == "B":
        print("¡Squirtle ataca con Burbuja!")
        vida_pikachu -= 7
    if ataque_squirtle == "N":
        print("No has hecho nada")

    if vida_squirtle < 0:
        vida_squirtle = 0
    if vida_pikachu < 0:
        vida_squirtle = 0

    barra_vida_pika = int(vida_pikachu * 10 / VIDA_INICIAL_PIKACHU)
    print("Pikachu:   [{}{}] ({}/{})".format("*" * barra_vida_pika, " " * (10 - barra_vida_pika), vida_pikachu, VIDA_INICIAL_PIKACHU))

    barra_vida_squirtle = int(vida_squirtle * 10 / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:   [{}{}] ({}/{})".format("*" * barra_vida_squirtle, " " * (10 - barra_vida_squirtle), vida_squirtle, VIDA_INICIAL_SQUIRTLE))


    input("Pulsa enter para continuar...\n\n")
    os.system("cls")


if vida_pikachu > vida_squirtle:
    print("¡Ha ganado Pikachu!")
else:
    print("¡Ha ganado squirtle!")