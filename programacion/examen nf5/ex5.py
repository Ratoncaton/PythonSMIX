#importem una llibreria per a fer operacions aleatories
import random

#preguntem a l'usuari dos numeros enters
numero1 = int(input("Introdueixi un numero: "))
numero2 = int(input("Introdueixi un altre numero: "))

#mostrem les sumes i multiplicaciones dels dos numeros presentats
print("Els dos numeros sumats donen {}".format(numero1 + numero2))
print("Els dos numeros restats donen {}".format(numero1 - numero2))
print("Els dos numeros multiplicats donen {}".format(numero1 * numero2))
print("Els dos numeros dividits donen {}".format(numero1 / numero2))
print("Els dos numeros dividits mostran el residu donen {}".format(numero1 % numero2))

#mostra un numero aleatori entre els dos numeros, si el numero 1 es mes gran que el 
# numero 2 dona error, el except agafa el error i en menys de mostrar-ho canvia el print 

try:
    print("Un número aleatori entre els dos és {}".format(random.randint(numero1, numero2)))
except ValueError:
    print("Un número aleatori entre els dos és {}".format(random.randint(numero2, numero1)))