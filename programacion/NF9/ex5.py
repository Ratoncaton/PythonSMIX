
comptador = 0

def increment():
    a = int(input("Quant vols incrementsr?\n"))
    return comptador + a

def assignament():
    user = int(input("Quin valor inicial vols assignar?\n"))
    return user

def imprimir(comptador):
    print(comptador)

def main(comptador):
    comptador = assignament()
    comptador += increment()
    imprimir(comptador)

if __name__ == "__main__":
    main(comptador)
    