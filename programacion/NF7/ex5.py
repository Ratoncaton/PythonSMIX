
numeroC = int(input("Introdueix un nombre: "))
numero = numeroC - 1
nF = numeroC

while numero != 0:
    
    nF = nF * numero
    numero -= 1

print(nF)