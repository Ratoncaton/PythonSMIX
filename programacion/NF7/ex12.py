entry = input("Introdueix un nombre: ")

math = 0

for n in entry:
    math += int(n) ** 3

if math == int(entry):
    print("El nombre {} és armstrong".format(entry))

else:
    print("El nombre {} no és armstrong".format(entry))