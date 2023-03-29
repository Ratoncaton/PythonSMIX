#(C) Code By Walid El Ourfi. All rights reserved 

import random
import time

num_aleatori = random.randint(1, 100)

num_usuari = 100

contador = 0

while num_aleatori != num_usuari:
    num_usuari = int(input("Introdueix un nombre per encertar: "))

    contador += 1

    #Condicionals principals (sortida, anims i indicadors)
    if num_usuari == 0:
        break

    elif contador == 5:
        print("Estas a punt de conseguir-ho, no paris!!")
        time.sleep(1)
        continue

    elif num_aleatori != num_usuari:
        print("Has fallat no era aquest nombre...")
        time.sleep(1)
        
        # Indicadors de nombre (si es mes gran o petit)
        if num_usuari > num_aleatori:
            print("El nombre és més petit del que has posat")
        
        elif num_usuari < num_aleatori:
            print("El nombre és més gran del que has posat")
    
else:
    print("Molt bé, el nombre era {}".format(num_aleatori))
    print("Per averiguar-ho t'ha costat {} intent(s)".format(contador))

time.sleep(1)
print("Tancant joc....")
time.sleep(2)