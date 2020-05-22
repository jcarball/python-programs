#minutes = num % 60
#horas = (num -  minutes)/60

hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
# encuentra el número total de minutos)
Totalmin = (hora*60) + min + dura
# encuentra el número de horas ocultos en los minutos y actualiza las horas
HorasOcultas = Totalmin%60
horas = int((Totalmin - HorasOcultas)/60)
# corrige los minutos para que estén en un rango de (0..59)
# corrige las horas para que estén en un rango de (0..23) 
print(horas, ":", HorasOcultas, sep='')
