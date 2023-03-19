n1 = float(input("Introduzca un numero: "))
n2 = float(input("Introduzca otro numero: "))

if n1 == 0 or n2 == 0:
    print("Los numeros no son divisibles ente 0")

else:
    print("{} / {} = {}".format(n1, n2, n1 / n2))

