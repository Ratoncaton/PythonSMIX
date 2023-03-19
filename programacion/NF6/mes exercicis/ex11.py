

print("""
       LA POLITANA MENÚ

VERDURES (A) |  PIZZES (B) 
""")

menu = ""
postre = ""

inp_ver_pizz = input("Escolleix quin tipus de menú vols").lower()

if inp_ver_pizz == "a":
    print("""
    VERDURES:
    (A) Crema de carbassa 
    (B) Ratatouille
    (C) Pic de gall
    """)

    inp_verd = input("Que vol escollir? ").lower()
    if inp_verd == "a":
        menu = "Crema de carbassa"
    
    elif inp_verd == "b":
        menu = "Ratatouille"
    
    elif inp_verd == "c":
        menu = "Pic de gall"
    
    else:
        print("Has desat una resposta incorrecta")
    
elif inp_ver_pizz == "b":
    print("""
    PIZZES:
    (A) Carbonara
    (B) 4 formatges
    (C) Pinya
    """)

    inp_pizz = input("Que vols escollir? ").lower()
    
    if inp_pizz == "a":
        menu = "Pizza carbonara"
    
    elif inp_pizz == "b":
        menu = "Pizza 4 formatges"
    
    elif inp_pizz == "c":
        menu = "Pizza de pinya"
    
    else:
        print("Has desat una resposta incorrecta")

else:
    print("Has desat una resposta incorrecta")


print("""
      POSTRES

SALUDABLES (A) | NO SALUDABLES (B)
""")

inp_post_inic = input("Escull unb postre: ").lower()

if inp_post_inic == "a":
    print("""
    POSTRES SALUDABLES:
    (A) Yogur de fresa casolà
    (B) Dolç de sandia
    (C) Fruites de temporada
    """)

    inp_post = input("Que vols escollir? ")

    if inp_post == "a":
        postre = "Yogur de fresa casolà"
    
    elif inp_post == "b":
        postre = "Dolç de sandia"
    
    elif inp_post == "c":
        postre = "Fruites de temporada"
    
    else:
        print("Has desat una resposta incorrecta")

elif inp_post_inic == "b":
    print("""
    POSTRES NO SALUDABLES:
    (A) Gelat
    (B) Natilla
    (C) Pastís sorpresa
    """)

    inp_post = input("Que vols escollir? ")
    if inp_post == "a":
        postre = "Gelat"
    
    elif inp_post == "b":
        postre = "Natilla"
    
    elif inp_post == "c":
        postre = "Pastís sorpresa"
    
    else:
        print("Has desat una resposta incorrecta")


print("La seva ordre es {} i de postre {}".format(menu,postre))

inp_anal = input("Vol que analitzessim la seva ordre? (S/N) \n").lower()  #anal de analisis jaja

menu_sal = True
postre_sal = True

if inp_anal == "s":
    if inp_ver_pizz == "b":
        menu_sal = False
    
    if inp_post_inic == "b":
        postre_sal = False

if menu_sal == True and postre_sal == False:
    print("Un menjar bastant equilibrat, interesant.")

elif menu_sal == False and postre_sal == True:
    print("Has triat un bon postre, sol falta canviar la pizza per algo millor.")

elif menu_sal == False and postre == False:
    print("Posa't algo més saludable, com a recomanació")

else:
    print("Ets una persona molt saludable, per això tens un 5 percent de descompte")