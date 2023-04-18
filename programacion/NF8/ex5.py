#exercici 6 nf7

usuari = input("Introdueix una paraula: ")

paraula_inversa = [""]
contador = -1


for n in range(len(usuari)):
    paraula_inversa.append(usuari[contador])
    contador -= 1

print(paraula_inversa)