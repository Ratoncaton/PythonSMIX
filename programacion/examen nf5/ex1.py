#Aquest codi ha sigut agafat i remodelat del model del exercici 1 de una carpeta amb exercicis fets a classe

#variable del percentatge de la nota de practiques
per_nota_practiques = 40

#variable del percentatge de la nota d'examen
per_nota_examen = 60

#variables en input para saber la nota del examen
print("Escriu la nota de les pràctiques (1/3)")
nota_practica1 = float(input("->"))
print("Escriu la nota de les pràctiques (2/3)")
nota_practica2 = float(input("->"))
print("Escriu la nota de les pràctiques (3/3)")
nota_practica3 = float(input("->"))
print("Escriu la nota del examen")
nota_examen = float(input("->"))

#multiplicacions para fer una part del calcul de la mitjana on pp es part practica i pe part examen
pp1 = per_nota_practiques * nota_practica1
pp2 = per_nota_practiques * nota_practica2
pp3 = per_nota_practiques * nota_practica3
pe = per_nota_examen * nota_examen

#divisions per fer l'altra part del calcul
div_1 = pp1 + pp2 + pp3 + pe
div2 = per_nota_practiques + per_nota_practiques + per_nota_practiques + per_nota_examen
nota_final = round(div_1/div2, 2)

if nota_final > 5:
    print("Has aprovat amb un {}".format(nota_final))

else:
    print("No has aprovat, has tret un {}".format(nota_final, 2))


#El .format es una comanda la qual fica el que hi ha dins dels parentesis dins 
# de les {} de forma ordenada, osigue si hi han mes d'una {} en el .format 
# s'haurà de posar el que volem que es mostri separats en comes de forma que 
# el primer {} es posarà el que hi al primer apartat del .format, per diferenciar 
# els apartats s'utilitzen comes