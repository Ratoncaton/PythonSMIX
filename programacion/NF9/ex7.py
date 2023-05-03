import random

def corrector_numeros():
    user = input("Escriu una frase:\n")
    for i in user:
        if i == " ":
            continue
        
        print(i)


def adivinidaor():
    aleatori = random.randint(1, 100)
    finnish = False

    while not finnish:
        user = int(input("Introdueix el nombre: \n"))
        if user == aleatori:
            print("L'has adivinat! Era {}".format(aleatori))
            finnish == True
        
        elif user > aleatori:
            print("Has escollit un numero massa gran...")
        
        else:
            print("Has escollit un nombre massa petit...")

def pregunta_1():
    #pregunta 1 del test caracol
    
    puntuacion = 0
    opcion = input("Pregunta 1: ¿Vas lent o rapid en la carretera?\n"
               "A:Lent, que si no passa el que passa.\n"
               "B:A vegades, un poquet de velocitat sempre va be.\n"
               "C:Sempre vaig a tota pastilla.\n")

    if opcion == "A":
        puntuacion += 0
    elif opcion == "B":
        puntuacion += 5
    elif opcion == "C":
        puntuacion += 10
    else:
        print("Les opcions dispnibles son A, B, y C.")
    
    return puntuacion

def pregunta_2():
    #pregunta 2 dekltest caracol
    
    puntuacion = 0
    opcion = input("Pregunta 2: ¿T'agrada la lechuga?\n"
               "A:No, vaya asco.\n"
               "B:Alguna que altra fulla me menjaria.\n"
               "C:Si, m'encanta.\n")

    if opcion == "A":
        puntuacion += 0
    elif opcion == "B":
        puntuacion += 5
    elif opcion == "C":
        puntuacion += 10
    else:
        print("Les opcions dispnibles son A, B, y C.")
    
    return puntuacion


def pregunta_3():
    #pregunta 3 del test caracol

    puntuacion = 0
    opcion = input("Pregunta 3: ¿T'agrada la pluja?\n"
               "A:No, no hem deixa sortir a disfrutar del dia.\n"
               "B:A vegades està be per relaxar-se.\n"
               "C:Si, m'encanta.\n")

    if opcion == "A":
        puntuacion += 0
    elif opcion == "B":
        puntuacion += 5
    elif opcion == "C":
        puntuacion += 10
    else:
        print("Les opcions dispnibles son A, B, y C.")
    
    return puntuacion


def caracol():
    puntuacio  = 0

    puntuacio += pregunta_1()

    puntuacio += pregunta_2()

    puntuacio += pregunta_3()

    if puntuacio > 15:
        print("No ets un cargol...")
    
    elif puntuacio > 15 and  puntuacio < 30:
        print("T'estas convertint en un cargol") 

    else:
        print("Felicitats! Ets un cargol") 

def main():

    quit = False

    while not quit:

        print("""
        --- VARIETY MENÚ ---
        
        1. Corrector de numeros (posa els numeros en ordre)
        2. Adivinador (adivina el numero)
        3. Quin tipus de cargol ets?
        4. Sortir
        
        --------------------""")
        user = input("\nQuina opció vol fer?\n")

        if user == "1":
            corrector_numeros()
        
        elif user == "2":
            adivinidaor()
        
        elif user == "3":
            caracol()
        
        elif user == "4":
            quit = True

if __name__ == "__main__":
    main()