print("""
          Ingredients:
A totes les pizzes: Mozzarella | Tomàquet
Vegetariàna: (1)Pebrot | (2)Tofu
No vegetariàna: (3)Peperoni | (4)Pernil | (5)Salmó""")

entry = int(input("Què vols afegir? "))
ingredients = ""

if entry == 1:
    ingredients = ", Pebrot"

elif entry == 2:
    ingredients = ", Tofu"

elif entry == 3:
    ingredients = ", Peperoni"

elif entry == 4:
    ingredients = ", Pernil"

elif entry == 5:
    ingredients = ", Salmó"


print("Ingredients seleccionats: Mozzarella, Tomàquet{}.".format(ingredients))