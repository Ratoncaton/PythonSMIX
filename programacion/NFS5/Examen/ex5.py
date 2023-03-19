#Calculadora de la hipotenusa
#11/01/23 
#By Walid El ourfi

import math

catetA = int(input("Introdueixi el catet A: "))
catetB = int(input("Introdeixi el catet B: "))

#La operació comença fent el quadrat de cada catet
catetA = catetA ** 2
catetB = catetB ** 2

#Després es suma els dos catets
sumAB = catetA + catetB

#Per últim es fa l'arrel quadrada amb la llibreria math. math.sqrt(x) 
#També es mostrarà coma a màxim dos digits.
print(round(math.sqrt(sumAB), 2))