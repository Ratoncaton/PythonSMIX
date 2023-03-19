entry = int(input("Introduzca la edad: "))
entry_cost = ""

if entry < 4:
    entry_cost = "Gratuita"

elif entry >= 4 and entry < 18:
    entry_cost = "5€"

else:
    entry_cost = "10€"

print("La entrada serà {}".format(entry_cost))