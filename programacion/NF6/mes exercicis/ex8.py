print("""
      OPCIONS DE CALCULADORA
- Suma
- Resta
- Multiplicacio
- Divisió
- Percentatge
""")

entry = input("Introdueix la opció desitjada: ")

n1 = float(input("Introduex un nombre: "))
n2 = float(input("Introduex un altre nombre: "))

if entry.upper() == "SUMA":
    print("{} + {} = {}".format(n1, n2, n1 + n2))

elif entry.upper() == "RESTA":
    print("{} - {} = {}".format(n1, n2, n1 - n2))

elif entry.upper() == "MULTIPLICACIO":
    print("{} * {} = {}".format(n1, n2, n1 * n2))

elif entry.upper() == "DIVISIO":
    print("{} / {} = {}".format(n1, n2, n1 / n2))

else:
    print("{}% \de {} = {}".format(n1, n2, (n1 * n2) / 100))