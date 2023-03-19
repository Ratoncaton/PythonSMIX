#cost en euro per quilometre
euro_km = 2

#quiloemtres que vol fer l'usuari
print("Cost actual del viatge {}€ el quilòmetre".format(euro_km))
km_usuari = float(input("Introdueixi els quilòmetres que vol recòrre: "))

#es mostra el cost final utilitzant un .format on a dins està el calcul on es rondejarà a dos xifres
print("El cost final del viatge és {}€".format(round(euro_km * km_usuari, 2)))