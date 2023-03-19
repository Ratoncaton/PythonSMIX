age = int(input("Introduzca tu edad: "))
gender = input("Introduzca su genero: ").lower()

if age == 18:
    print("En un mes no habra canvios en tu vida")

elif gender == "hombre" or gender == "chico":
    print("Seras un drogadicto, nah locura")

elif age == 17:
    print("El año que viene te legalizas")

elif gender == "mujer" or gender == "chica":
    print("En los 50 años tendras un paro cardíaco")

else:
    print("Seguro eres otaku.... Dúchate guarro")