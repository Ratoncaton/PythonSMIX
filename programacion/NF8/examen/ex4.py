
#lista per agrupar la sequencia de fibonacci
fibonacci_sequence = [1, 1]

#l'ultim nombre de la sequencia
first_number_sequence = fibonacci_sequence[-1]

#penultim nombre de la sequencia
seconf_number_sequence = fibonacci_sequence[-2]

for i in range(1, 10):

    #la suma del ultim i penultim nombre de la lista formen el nou nombre de la sequencia
    fibonacci_sequence.append(first_number_sequence + seconf_number_sequence)

    #actualitzem les variables per a que no sigui un bucle del mateix nombre
    first_number_sequence = fibonacci_sequence[-1]
    seconf_number_sequence = fibonacci_sequence[-2]

print(fibonacci_sequence)


#Made By Walid El Ourfi 1 SMX B 
    