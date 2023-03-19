preguntes = 30
nota_pregunta = 10/preguntes
nota_ri = nota_pregunta*25/100


RC = int(input("Respostes correctes: "))
RI = int(input("Respostes incorrectes: "))
RB = int(input("Respostes en blanc: "))

suma_RC = RC*nota_pregunta
suma_RI = RI*nota_ri

nota = suma_RC - suma_RI
print(nota)
