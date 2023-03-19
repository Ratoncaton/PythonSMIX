from time import sleep
import os

finnish = False

PRODUCT = ["fairy", "desinfectante", "extintor", "gambas", "patatas fritas", "pizza", 
           "naranjas", "platanos", "berenjena", "lomo", "carne picada", "albondigas"]

price = [4.34, 2.78, 15, 6.78, 3.12, 2.57, 3, 4, 2, 3.78, 3.56, 3.34]

products = []
units = []
user_price = []
user_total = 0

user_column = []

while not finnish:
    print("""
    ----BIENVENIDO A SUPERMERCADOS LERISA----

    CUIDADO DEL HOGAR:     |              CONGELADOS:
                           |
    Fairy - 4.34 €         |           Gambas - 6.78 €
    Desinfectante - 2.78 € |  Patatas fritas - 3.12 €
    Extintor - 15 €        |           Pizza - 2.57 €
    ---------------------------------------------------
    FRUTAS Y VERDURAS:     |               CARNICERIA:
                           | 
    Naranjas - 3 €         |             Lomo - 3.78 €
    Platanos - 4 €         |     Carne picada - 3.56 €
    Berenjena - 2 €        |       Albondigas - 3.34 €               
    """)
    products.append(input("Quin producte vols introduir? \n").lower())
    if products[-1] in PRODUCT:
        units.append(int(input("Quantas unidades quiere? \n")))
        suma = 0
        for i in PRODUCT:
            if i not in products[-1]:
                suma += 1
            else:
                break
        user_price.append(price[suma])
        print("Usted a introducido {} {} por {} la unidad, en total són {} euros".format(units[-1], products[-1], price[suma], user_price[-1] * units[-1]))
        inp = input("Confirma la introduccion del producto a tu cesta de la compra? (S/N) \n").upper()
        if inp == "N":
            products.pop(-1)
            units.pop(-1)
            user_price.pop(-1)
        else:
            user_total += user_price[-1] * units[-1]
        
        user_column.append("{} {} {} euros".format(units[-1], products[-1], user_price[-1] * units[-1]))

        inp = input("Quieres introducir más productos? (S/N) \n").upper()
        if inp == "N":
            finnish = True
            sleep(2)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("No has introducido un producto valido")
        sleep(2)
        products.pop(-1)
        os.system('cls' if os.name == 'nt' else 'clear')

print(user_column)

