entrada = 2500
asseg_medica = 50
trienni = 12//3 * 48.9
paga_extra = 80 #%

 #Sortida son els diners totals que pagarem 
sortida = (entrada*paga_extra/100) + entrada
sortida += trienni
#Com el IRPF descompta ficarem directament el percentatge que ens quedara per tal de no fer passos extra
sortida = sortida*82/100
sortida -= asseg_medica

print("{}€".format(round(sortida, 2)))
