#exercici 7 nf7

usuari = input("Introdueix una paraula:")

contador_a = 0

for n in usuari:
    if n == "a" or n == "A":
        contador_a += 1
    elif n == "z" or n == "Z":
        break

print("Hi han {} a, potser hi han més".format(contador_a))