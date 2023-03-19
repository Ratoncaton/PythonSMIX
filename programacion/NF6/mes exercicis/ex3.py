e1 = input("Introduzca una palabra o frase: ")
e2 = input("Introduzca otra palabra o frase: ")


if len(e1) > len(e2):
    print(e1, "es mas largo con", len(e1), "palabras")

elif len(e1) == len(e2):
    print("Empate")

else:
    print(e2, "es mas largo con", len(e2), "palabras")
