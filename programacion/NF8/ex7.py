#exercici 8 nf7

vocals = ["a", "o", "e", "i", "u"]

usuari = input("Introdueix una paraula: ")

for n in usuari:
    if n in vocals:
        print("", end="")
        continue
    print(n, end="")

print()