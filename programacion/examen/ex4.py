from datetime import datetime
now = datetime.now()

nom = "Manolo Centellas"
data_naix_input = "23/11/1958"

data_naix = data_naix_input.split("/")

dia_act = now.day
mes_act= now.month
any_act = now.year

dia_naix = data_naix[0]
mes_naix = data_naix[1]
any_naix = data_naix[2]

any = any_act - int(any_naix)
mes = mes_act - int(mes_naix)
dia = dia_act - int(dia_naix)

if mes == 0 and dia == 0:
    any += 1
    print ("Felicitats {} avui fas {} anys!".format(nom, any))

elif mes < 0 or dia < 0:
    mes_new = str(mes).replace("-", "")
    dia_new = str(dia).replace("-", "")
    any_new = any - 1 
    print("Hola {}, tens {} anys, et falten {} mesos i {} dies per tindre {} anys.".format(nom, any_new, mes_new, dia_new, any))

else:
    print("Hola {}, tens {} anys {} mesos i {} dies.".format(nom, any, mes, dia))


