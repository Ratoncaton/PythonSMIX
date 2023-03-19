#Convertidor de segons a segons minuts hores i dies.
#11/01/23 
#By Walid El ourfi

entry = int(input("Introdueixi els segons: "))

segons = entry % 60

minuts = entry // 60

hores = minuts // 60 

dies = hores // 24

# Es resten els minuts per les hores transformades en minuts per a tal que no surti els minuts convertit en hores 
minuts = minuts - (hores * 60)
hores = hores - (dies * 24)

print("Correspon a {} dies , {} hores, {} minuts i {} segons".format(dies, hores, minuts, segons))