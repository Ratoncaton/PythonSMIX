entry = float(input("Introdueix un numero: "))

answ = ""

if entry <=10:
    answ = input("Disme un color: ").lower()
    if answ == "blau":
        answ = input("De quina tonalitat: ").lower()

elif entry >10 and entry <= 20:
    answ = input("Disme un nom: ")
    answ = input("Disme el sexe: ")

else:
    print("No has entes la pregunta")

print("")