pes_nota1_2 = 40
pes_nota_3 = 40
pes_nota_4 = 20

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 3: "))


p1 = nota1 * pes_nota1_2
p2 = nota2 * pes_nota1_2
p3 = nota3 * pes_nota_3
p4 = nota4 * pes_nota_4


div1 = p1 + p2 + p3 + p4
div2 = pes_nota1_2 + pes_nota1_2 + pes_nota_3 + pes_nota_4

div = div1/div2

print(div)

