import string

#Les lletres amb accents, la ñ i la ç els identifica com a caracters especials.

user_input = input("Introdueix una paraula:\n")

for letter in user_input:
    #si la lletra coincideix en alguna lletra de la variable de lletres minuscules ho canvia a majuscules
    if letter in string.ascii_lowercase:
        print(letter.upper(), end="")
    
    #si la lletra coincideix en alguna lletra de la variable de lletres majuscules ho canvia a minuscules
    elif letter in string.ascii_uppercase:
        print(letter.lower(), end="")
    
    else:
        print(letter, end="")

print("")


#Made By Walid El Ourfi 1 SMX B 