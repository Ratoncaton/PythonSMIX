
numeroC = int(input("Introdueix un nombre del 0 al 10:"))
numSuma = 1
numero = 1

if numeroC == 5:
    numSuma -= 5

while numero != numeroC:
    if numSuma == 5:
        numSuma -= 5
    
    numSuma += numero

    numero += 1

print(numSuma)