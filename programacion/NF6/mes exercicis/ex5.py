entry = input("Introduzca un caràcter: ").lower()

consonant = ["q", "w",  "r",  "t",  "y", "p",  "s", "d", "f", "g", "h", "j", "k", "l", "ñ", "z", "x", "c", "v", "b", "n", "m"]
vocal = ["a", "e", "i", "o", "u"]
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

if entry in consonant:
    print("El caràcter es una consonant")

elif entry in vocal:
    print("El caràcter es una vocal")

elif entry in num:
    print("El caràcter es un numero")

else:
    print("El caràcter es un altre caràcter")
