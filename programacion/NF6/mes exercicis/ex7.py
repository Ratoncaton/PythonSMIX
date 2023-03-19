n1 = float(input("Introduzca la nota: "))
n2 = float(input("Introduzca la nota: "))
n3 = float(input("Introduzca la nota: "))
n4 = float(input("Introduzca la nota: "))
n5 = float(input("Introduzca la nota: "))

n = [n1, n2, n3, n4, n5]

if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
    n.pop(0)

elif n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
    n.pop(1)

elif n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
    n.pop(2)

elif n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
    n.pop(3)

else:
    n.pop(4)

nota = (n[0] + n[1] + n[2] + n[3]) / 4

print("La nota final serà {}".format(nota))
