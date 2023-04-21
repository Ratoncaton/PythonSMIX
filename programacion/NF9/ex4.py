

resultat = 0

def suma(suma_1, suma_2):
    resultat = suma_1 + suma_2
    print(resultat)


def main():
    suma_1 = int(input("Introdueix un nombre:\n"))
    suma_2 = int(input("Introdueix un altre nombre:\n"))

    suma(suma_1, suma_2)

if __name__ == "__main__":
    main()