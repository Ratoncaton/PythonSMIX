#exerici 11 NF7 i ex 13 NF7

user = input("Introdueix un nombre: \n")
revere_user = user[::-1]
position = 0
auth = 0

for n in revere_user:
    if n == user[position]:
        auth += 1
    position += 1

if auth == len(user):
    print("És palindrom")
else:
    print("No es palindrom")
