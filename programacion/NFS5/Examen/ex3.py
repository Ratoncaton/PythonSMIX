#Mostra una frase on es diu el teu nom, cognom i la edat teva de l'any que ve amb _ en menys de espais
#11/01/23 
#By Walid El ourfi


nom = input("Escriu el teu nom: ")
cognom = input("Escriu el teu cognom: ")
edat = int(input("Escriu la teva edat: "))
edatafegit = edat + 1

print("Hola_et_dius_{}_{}_i_l’any_que_ve_tindràs_{}_anys.".format(nom, cognom, edatafegit))
