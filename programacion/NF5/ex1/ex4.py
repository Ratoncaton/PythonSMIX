paAvui = float(input("Quan costa el pa avui: "))
paAhir = (40*3.40)/100
estalvi = paAvui - paAhir
paVenut = int(input("Quants pans s'ha venut: "))

print("Comprant {} barres de pa del dia anterior s'haguessin estalviat {} euros".format(paVenut, paVenut * estalvi))