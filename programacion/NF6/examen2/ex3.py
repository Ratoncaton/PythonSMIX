import math

decisio = input("Quina àrea vols calcular: (q)uadrat,  (r)ectangle, (c)ercle, (t)riangle\n").upper()

if decisio == "Q":
    
    decisio = "quadrat" #cambiem la variable per el nom complet para el print final
    lCostat = float(input("Quina es la longitud del seu costat: "))
    output = lCostat * lCostat #variable que conté el calcul

elif decisio == "R":
    decisio = "rectangle"
    lBase = float(input("Quina es la longitud de la seva base: "))
    lCostat = float(input("Quina es la longitud del seu costat: "))
    output = lBase * lCostat

elif decisio == "C":
    decisio = "cercle"
    rCercle = float(input("Quin és el radi del cercle: "))
    output = math.pi * (rCercle ** 2)

elif decisio == "T":
    decisio = "triangle"
    lbase = float(input("Quina és la longitud de la base: "))
    lalçada = float(input("Quina és la longitud de la alçada: "))
    output = (lbase * lalçada) / 2

else:
    print("Has introdüit alguna dad incorrecta")

print("L'àrea del {} és de {}".format(decisio, output))
