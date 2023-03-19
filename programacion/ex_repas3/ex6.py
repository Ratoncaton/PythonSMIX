entrada = int(input("Introdueix els segons: "))

hora_segons = round(entrada / 3600, 3)
minuts_segons = round(entrada / 60, 3)

print("{} serien {} hores i en minuts serien {}".format(entrada, hora_segons, minuts_segons))