#Programa per a calcular les recaudacions del cinema
entry = input("La projecció és (e)strena, (n)ormal o (d)escompte? ").lower()
fila = int(input("Files omplertes: "))
columnes = int(input("Columnes omplertes: "))

#tipus d'entrada posada
type = ""
#valor de la entrada introudida per a calcular
valor_entrada = 0
#Booleano per a verificar si ha hagut algun error
error = False

if entry == "e":
    type = "estrena"
    valor_entrada = 12.00

elif entry == "n":
    type = "normal"
    valor_entrada = 7.50

elif entry == "d":
    type = "descompte"
    valor_entrada = 5.00

else:
    print("Has introudit alguna dada incorrecta")
    error = True

#Condicional per a no escriure el total si hi ha un error
if error == False:
    print("La sala de {} amb un total de {} seients omplerts es recaurdaria un total de {} €".format(type, fila * columnes, fila * columnes * valor_entrada))

