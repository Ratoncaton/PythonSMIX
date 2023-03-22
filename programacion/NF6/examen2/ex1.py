
fletxa = "-->" #variable per a decoració en el print

CtaxiNit = 1.68 #Tarifa dia
CtaxiDia = 1.58 #tarifa nit

Cbus = 0.08 #tarifa bus

Ctren = 0.05 #tarifa tren

kmInput = float(input("Cuants kilòmetres vols fer?\n"))

Pdia = input("En quin moment del día (d)ia (n)it: ").upper()

bus = 1000000 #variable del cost del bus, es fica aquest nombre per als condicionals
tren = 1000000 #variable del cost del tren, es fica aquest nombre per als condicionals

if Pdia == "D":
    taxi = kmInput * CtaxiDia  
    
    #condicionals per no fer prints de més, al no arribar al mínim de km no es calcularà
    if kmInput >= 20:
        bus = kmInput * Cbus
    
    if kmInput >= 100:
        tren = kmInput * Ctren


    if taxi < bus and taxi < tren:
        print("---- Tickets ----\n")

        print("{} taxi:{}€".format(fletxa, round(taxi, 2)))
        
        #condicionals per si els preus del bus i tren conten i el taxi és més barat
        if bus != 1000000:
            print("bus:{}€".format(round(bus, 2)))
        if tren != 1000000:
            print("tren:{}€".format(round(tren, 2)))

        print("\n---- Avís ----")
        print("El ticket més barat és mostrarà amb una fletxa")
        print("Els transports els quals no arribis a la trayectoria mínima no es mostraran")

    elif bus < taxi and bus < tren:
        print("---- Tickets ----\n")

        print("taxi:{}€".format(round(taxi, 2)))
        print("{}bus:{}€".format(fletxa, round(bus, 2)))
        
        #Com el bus és el més barat, si en algun cas és més barat que el tren sortirà el tren sino no 
        if tren != 1000000:
            print("tren:{}€".format(tren))

        print("\n---- Avís ----")
        print("El ticket més barat és mostrarà amb una fletxa")
        print("Els transports els quals no arribis a la trayectoria mínima no es mostraran")
    
    elif tren < taxi and tren < bus:
        print("---- Tickets ----\n")

        print("taxi:{}€".format(round(taxi, 2)))
        print("bus:{}€".format(round(bus, 2)))
        print("{}tren:{}€".format(fletxa, round(tren, 2)))

        print("\n---- Avís ----")
        print("El ticket més barat és mostrarà amb una fletxa")
        print("Els transports els quals no arribis a la trayectoria mínima no es mostraran")
    
    else:
        print("---- Tickets ----\n")

        print("{} taxi:{}€".format(fletxa, round(taxi, 2)))
        if bus != 1000000:
            print("bus:{}€".format(round(bus, 2)))
        if tren != 1000000:
            print("tren:{}€".format(round(tren, 2)))

        print("\n---- Avís ----")
        print("El ticket més barat és mostrarà amb una fletxa")
        print("Els transports els quals no arribis a la trayectoria mínima no es mostraran")


elif Pdia == "N":
    taxi = kmInput * CtaxiNit 

    if kmInput >= 20:
        bus = kmInput * Cbus
    
    if kmInput >= 100:
        tren = kmInput * Ctren

    if taxi < bus and taxi < tren:
        print("---- Tickets ----\n")

        print("{} taxi:{}€".format(fletxa, round(taxi, 2)))
        if bus != 1000000:
            print("bus:{}€".format(round(bus, 2)))
        if tren != 1000000:
            print("tren:{}€".format(round(tren, 2)))

        print("\n---- Avís ----")
        print("El ticket més barat és mostrarà amb una fletxa")
        print("Els transports els quals no arribis a la trayectoria mínima no es mostraran")

    elif bus < taxi and bus < tren:
        print("---- Tickets ----\n")

        print("taxi:{}€".format(round(taxi, 2)))
        print("{}bus:{}€".format(fletxa, round(bus, 2)))
        if tren != 1000000:
            print("tren:{}€".format(tren))

        print("\n---- Avís ----")
        print("El ticket més barat és mostrarà amb una fletxa")
        print("Els transports els quals no arribis a la trayectoria mínima no es mostraran")
    
    elif tren < taxi and tren < bus:
        print("---- Tickets ----\n")

        print("taxi:{}€".format(round(taxi, 2)))
        print("bus:{}€".format(round(bus, 2)))
        print("{}tren:{}€".format(fletxa, round(tren, 2)))

        print("\n---- Avís ----")
        print("El ticket més barat és mostrarà amb una fletxa")
        print("Els transports els quals no arribis a la trayectoria mínima no es mostraran")
    
    else:
        print("---- Tickets ----\n")

        print("{} taxi:{}€".format(fletxa, round(taxi, 2)))
        if bus != 1000000:
            print("bus:{}€".format(round(bus, 2)))
        if tren != 1000000:
            print("tren:{}€".format(round(tren, 2)))

        print("\n---- Avís ----")
        print("Poden haver dos o més tickets amb el preu igualat")

else:
    print("Has introdüit alguna dada incorrecta")
