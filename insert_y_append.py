miLista = [] # creando una lista vacía

for i in range (5):
    miLista.append (i + 1)

print(miLista)

miLista = [] # creando una lista vacía

for i in range(5):
    miLista.insert(0, i + 1)

print(miLista)

miLista = [10, 1, 8, 3, 5]
suma = 0

for i in range(len(miLista)):
    suma += miLista[i]

print(suma)

variable1 = 1
variable2 = 2

auxiliar = variable1
variable1 = variable2
variable2 = auxiliar 
print(variable1,variable2)

variable1 = 1
variable2 = 2

variable1, variable2 = variable2, variable1 
print (variable1,variable2)

miLista = [10, 1, 8, 3, 5]
longitud = len(miLista)

for i in range (longitud // 2):
    miLista[i], miLista[longitud-i-1] = miLista[longitud-i-1], miLista[i]

print(miLista) 