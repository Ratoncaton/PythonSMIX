n1 = int(input("Introduzca un numero: "))
n2 = int(input("Introduzca otro numero: "))
n3 = int(input("Introduzca otro numero: "))

if n1 + n2 == n3:
    print("{} + {} = {}".format(n1, n2, n3))

elif n1 + n3 == n2:
    print("{} + {} = {}".format(n1, n3, n2))

elif n2 + n3 == n1:
    print("{} + {} = {}".format(n2, n3, n1))

else:
    print("Diferents")