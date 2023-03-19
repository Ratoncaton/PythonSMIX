age = int(input("Introduzca su edad: "))
salary = float(input("Introduzca su salario bruto anual: "))

if age >= 18 and salary >= 25000:
    print("Sus impuestos seran de  {} euros".format(salary * 12 / 100))

else:
    print("Usted no alcanza los requisitos minimos")