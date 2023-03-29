import random

finnish = False
random_n = 10
n_choosen = int(input("Escolleix un nombre entre 0 i 100: \n"))

while n_choosen != random_n:

    print("Has fallat, el nombre {} no és el correcte".format(n_choosen))
    
    n_choosen = int(input("Escolleix un nombre entre 0 i 100: \n"))

else:
    print("Ho has encertat, el nombre verdader és el {}".format(random_n))

    
    