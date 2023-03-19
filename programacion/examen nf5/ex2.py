
#primer preguntem quin es el salari actual del trebllador
salari_base = float(input("El teu salari:  "))

#Després preguntem per el percentatge que li augmentarán
per_aument = float(input("El percentatge d'increment: "))

#Finalment fem un print i utilitzant el .format farem també la operació per a mostrar el salari que trindrà el treballador
print("El teu salari amb l'increment és: {}".format(((per_aument * salari_base) /100) + salari_base))

