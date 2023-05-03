
comptador = 0

def increment():
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

