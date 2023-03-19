entrada = input("Introdueix els dies, hores i minuts (dies,hores,minuts): ")

particio = entrada.split(",")

dies = int(particio[0])
hores = int(particio[1])
minuts = int(particio[2])

segons_dies = dies * 86400
segons_hores = hores * 3600
segons_minuts = minuts * 60

print(segons_dies + segons_hores + segons_minuts, "segons")