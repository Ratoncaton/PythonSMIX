abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", 
       "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

name = input("Introduex el vostre nom: ").lower()
gender = input("Introdueix el vostre gènere (H)ome (D)ona: ").upper()

if gender == "D" and name[0:1] in abc[0:13] or gender == "H" and name[0:1] in abc[13:-1]:
    print("Estàs al grup A")

else:
    print("Estàs al grup B")