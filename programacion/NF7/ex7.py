
entry = input("Introdueix una paraula: ").lower()
a = 0

for n in entry:
    if n == "a":
        a += 1
    elif n == "z":
        break

print("En la paraula hi havien {} lletres (a), potser s'han quedat algunes lletres per comptar".format(a))