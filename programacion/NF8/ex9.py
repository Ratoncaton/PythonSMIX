#ex 12 NF7

user = input("Introdueix un nombre: \n")

total = 0

for i in user:
    total += int(i) ** 3

if str(total) == user:
    print("És armstrong")

else:
    print("No ho és")