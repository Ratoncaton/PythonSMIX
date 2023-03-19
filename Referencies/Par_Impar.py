def es_impar(n):
    impar = False
    if n%2 == 0:
        impar = False
        print("El numero es par")
    else:
        impar = True
        print("El numero es impar")

def main():
    es_impar(10)


if __name__ == "__main__":
    main()
