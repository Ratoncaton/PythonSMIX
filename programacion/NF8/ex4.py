#exercici 5 nf7

usuari = int(input("Introdueix el nombre per a fer factorial: "))

fact = 1 #variable posar el nombre en factorial

for n in range (usuari , 1, -1):
    fact *= n

print(fact)
