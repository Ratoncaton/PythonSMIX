a = float(input("Ingresa un valor: "))

b = float(input("Ingresa un altre valor: "))



print("La suma es: ", a + b) 

print("La resta es: ", a - b)

print("La multiplicació es: ", a * b)

try: 
    print("La divisió és: ", a/b)

except ZeroDivisionError:
    print("No es pot dividir per zero")



print("\n¡Eso es todo, amigos!")


