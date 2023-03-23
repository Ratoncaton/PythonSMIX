import os

finnish = False

while not finnish:
    entry = input("Introdueix un nombre: ")
    if entry == entry[::-1]:
        print("El nombre {} és palíndrom".format(entry))

    else:
        print("El nombre {} no és palíndrom".format(entry))
    
    choose = input("Vols continuar? (S)í o (N)o\n").upper()

    if choose == "N":
        finnish = True
    
    os.system('cls' if os.name == 'nt' else 'clear')

