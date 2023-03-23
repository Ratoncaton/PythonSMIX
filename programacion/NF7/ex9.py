import os


finnish = False

while not finnish:
    entry = int(input("Introdueix un nombre: "))

    prime = entry % 2

    if prime == 1:
        print("El nombre {} és primer".format(entry))
    
    else:
        print("El nombre {} no és primer".format(entry))

    choose = input("Vols continuar probant números? (S)í o (N)o\n").lower()

    if choose == "n":
        finnish = True
    
    os.system('cls' if os.name == 'nt' else 'clear')
    