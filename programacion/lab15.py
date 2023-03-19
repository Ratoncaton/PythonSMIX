hora = int(input("Hora de inicio (horas): "))

min = int(input("Minuto de inicio (minutos): "))

dura = int(input("Duración del evento (minutos): "))


residu = (dura + min) % 60
cosien = (dura + min) / 60


while hora >= 24:
    hora -= 24

hora += int(cosien)

while hora >= 24:
    hora -= 24

print(hora, residu)
