
Tjoc = 30000 #temps de joc a l'anys

Dlaboral = 63 #temps de joc en dia laboral

Dvacances = 127 # temps de joc en dia festiu

dies = int(input("Dies festius: "))

mlaborals = Dlaboral * (365 - dies) #dies on juga 63 min ja que son laborals

mvacances = Dvacances * dies #dies on juga 127 min ja que no son laborals

mrestants = Tjoc - (mvacances + mlaborals) #minuts que falten per arriba a 30.000

# si encara falten minuts per arribar a 30k aquest sempre serà major a 0 per tant dorm bé
if mrestants > 0:
    print("Tom dorm bé. {} minuts menys per jugar".format(mrestants))

#com hem jugat de més amb tom el numero serà negatiu per tant menor a 0
elif mrestants < 0:
    print("Tom fugirà. {} minuts més per jugar".format(-(mrestants))) # - * - = +

