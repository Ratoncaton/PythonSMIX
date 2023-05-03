
comptador = 0

def increment():
<<<<<<< HEAD
    comptador += int(input("Quants segons vols incrementar el comptador:\n"))
    

def initial():
    comptador = int(input("Quin valor vols iniciar el comptador"))

def printer():
    print(comptador)

def main():
    initial()
    increment()
    printer()

if __name__ == "__main__":
    main()

=======
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
    
>>>>>>> e7506ef6bb19a31235ea34e04a000c5c7c3f468b
