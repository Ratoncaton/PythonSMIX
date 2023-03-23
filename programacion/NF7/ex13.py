import os


finnish = False

while not finnish:

    entry = input("Introdueix una paraula: ")

    if entry == entry[::-1]:
        print("La paraula {} és capicua".format(entry))
    
    else:
        print("La paraula {} no és capicua".format(entry))

    choose = input("Vols continuar? (S)í o (N)o\n").upper()

    if choose == "N":
        finnish = True
    
    os.system('cls' if os.name == 'nt' else 'clear')