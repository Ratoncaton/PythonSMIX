entry = input("Introdueix una paraula o frase: ")
fphrase = []
vocals = ["a", "o", "e", "i", "u"]

for n in entry:
    if n not in vocals:
        fphrase.append(n)

print("La frase final és: {}".format(fphrase))

