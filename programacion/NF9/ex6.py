
def user_input():
    a = int(input("Introdueix un nombre: "))
    b = int(input("Introdueix un altre nombre: "))
    return a, b

def comprobacio(a, b):
    printer = False
    for i in range(min(a, b), max(a, b)+1):
        if i == 11:
            printer = True
    
    return printer

def main():
    
    a, b = user_input()

    print(comprobacio(a, b))

    

if __name__ == "__main__":
    main()



