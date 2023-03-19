y = int(input("Ingrese un año: "))

if y > 1582:
    if y % 4 != 0:
        print("Año común")
    else:
        print("Año bisiesto")

else:
    print("No dentro del calendario gregoriano ")