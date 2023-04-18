# exercici 4 nf7

user = int(input("Introdueix un nombre: "))
while user <= 10:

    suma = 0

    for i in range (1, user+1):
        if i == 5:
            suma -= i
        else:
            suma += i
    
    print(suma)

else:
    print("S'ha de posar un nombre més petit a 10...")
        
    