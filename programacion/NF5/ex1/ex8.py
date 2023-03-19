data = input("Esscriu la teva data (dd/mm/yy): ")
data = data.split("/")

print("Bon dia, vas néixer el dia {} del mes {} de l'any {}".format(data[0], data[1], data[2]))