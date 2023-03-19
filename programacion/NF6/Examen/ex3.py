#Programa per a decidir on anar de viatge
pressupost = float(input("Introdueix el pressupost esperat: "))
temporada = input("Introdueix la temporada de vacances: ").lower()

#Pressupost per a bulgària
if pressupost == 100 or pressupost < 100 and pressupost > 0:
    if temporada == "estiu":
        print("En algún lloc d'acampada per Bulgària per {} euros".format(round((pressupost * 30.00) / 100.00, 2)))
    
    elif temporada == "hivern":
        print("En algun hotel de Bulgària per {} euros".format(round((pressupost * 70.00) / 100.00, 2)))
    
    else:
        print("Has introduit alguna dada incorrecta")

#Pressupost per als balcans
elif pressupost > 100 and pressupost < 1000:
    if temporada == "estiu":
        print("En algún lloc d'acampada dels Balcans per {} euros".format(round((pressupost * 40.00) / 100.00, 2)))
    
    elif temporada == "hivern":
        print("En algun hotel dels Balcans per {} euros".format(round((pressupost * 80.00) / 100.00, 2)))
    
    else:
        print("Has introduit alguna dada incorrecta")

#Pressupost per a europa
elif pressupost > 1000:
    print("En algun hotel d'Europa per {} euros".format(round((pressupost * 90.00) / 100.00, 2)))

else:
    print("Has introduit alguna dada incorrecta")
