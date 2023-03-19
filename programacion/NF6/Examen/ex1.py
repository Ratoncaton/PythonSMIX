#Programa per a identificar si ets un senyor, senyoret, senyora o senyoreta

gender = input("Introdueix el vostre gènere (H / D): ").upper()
age = int(input("Introdueix la vostra edat: "))

#Condicionals per al gènere masculí
if gender == "H":
    if age > 16:
        print("Senyor")
    
    elif age < 16 and age > 0:
        print("Senyoret")
    
    else:
        print("Has desat alguna dada incorrecta")

#Condicionals per al gènere femení
elif gender == "D":
    if age > 16:
        print("Senyora")
    
    elif age < 16 and age > 0:
        print("Senyoreta")

    else:
        print("Has desat alguna dada incorrecta")   

#Per als errors d'escritura en el gènere
else:
    print("Has escrit alguna dada de incorrecta")