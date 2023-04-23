
def bucle(usuari, vocals):
    for n in usuari:
        if n in vocals:
            print("", end="")
            continue
        print(n, end="")

def main():
    vocals = ["a", "o", "e", "i", "u"]

    usuari = input("Introdueix una paraula: ")

    bucle(usuari, vocals)
    
    print()

if __name__ == "__main__":
    main()