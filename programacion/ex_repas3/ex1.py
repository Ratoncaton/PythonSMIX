per_nota1_2_3 = 16.67

per_nota_ex = 50

nota_1 = 4.9 
nota_2 = 8.7
nota_3 = 9.2
nota_4 = 2.5


p1 = per_nota1_2_3 * nota_1
p2 = per_nota1_2_3 * nota_2
p3 = per_nota1_2_3 * nota_3
p4 = per_nota_ex * nota_4

div_1 = p1 + p2 + p3 + p4
div2 = per_nota1_2_3 + per_nota1_2_3 + per_nota1_2_3 + per_nota_ex
nota_final = round(div_1/div2, 2)

if nota_final > 5:
    print("Has aprovat amb un {}".format(nota_final))

else:
    print("No has aprovat, has tret un {}".format(nota_final, 2))