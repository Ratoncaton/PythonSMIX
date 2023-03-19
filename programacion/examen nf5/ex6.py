#creem una variable per saber si continuem o tanquem programa
finish = False

#variable para saber els tipus de bitllets permesos
tipus_bitllets = [5, 10, 20, 50, 100, 500]

#variable per saber quan de import porta en cada suma l'usuari
import_usuari = 0

#bucle el qual agafa la variable finnish per continuar o surtirse
while not finish:
    bitllets = int(input("Introdueixi quin tipus de bitllet disposa: "))
    
    #condicional per si s'equivoca de bitllet si el posa bé es continúa el programa, sinó es repeteix el input
    if bitllets in tipus_bitllets:
        quantitat = int(input("Introdueixi quants bitllets disposa: "))

        #suma a la variable del import de l'usuari para saber l'import total
        import_usuari += bitllets * quantitat

        print("Vostè té {}€".format(import_usuari))

        #preguntem a l'usuari si vol continuar sumant bitllets o no
        final = input("Vol continuar sumant bitllets? (s/n): ")

        #per tancar el programa a de escriure explicitament n o no
        if final == "n" or "no":
            print("Tancant programa...")
            finish = True
        
        #si escriu una altra cosa o fa enter es continuarà sumant
        elif final == "s" or "si": 
            finish = False
    
    #per si escriu un bitllet que no està permes s'advertix a l'usuari i es torna a pregunrar
    else:
        print("Tipus de bitllet incorrecte, provi amb els bitllets {}".format(tipus_bitllets))