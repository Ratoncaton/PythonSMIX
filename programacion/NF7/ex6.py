
nombre = input("Introdueix una frase: ")
numN = -1
nombreR = []
while numN >= -len(nombre):
    
    nombreR.append(nombre[numN])
    numN -= 1

print(nombreR)


