c1 = float(input("Introduzca un lado del triangulo: "))
c2 = float(input("Introduzca otro lado del triangulo: "))
c3 = float(input("Introduzca otro lado del triangulo: "))

if c1 == c2 == c3:
    print("El triangulo es equilater")

elif c1 != c2 != c3:
    print("El triangulo es escale")

else:
    print("El triangulo es isosceles")