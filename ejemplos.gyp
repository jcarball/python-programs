x = int(input("Ingresa un número: ")) #  el usuario ingresa un 2
print(x * "5")
print(123+0.0)
var = 0 # asignando 0 a var
print(var == 0)

var = 1 # asignando 1 a var
print(var == 0)
var = 0 # asignando 0 a var
print(var != 0)

var = 1 # asignando 1 a var
print(var != 0)
n = int(input("Ingresa un número: "))
# utiliza la función print() aquí.
print(n<100)
print(n>100)

#lee tres números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))
numero3 = int (input("Ingresa el tercer número:"))

#asumimos temporalmente que el primer número
#es el más grande
#lo verificaremos pronto
nmasGrande = numero1

#comprobamos si el segundo número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero2 > nmasGrande:
    nmasGrande = numero2

#comprobamos si el tercer número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero3 > nmasGrande:
    nmasGrande = numero3

#imprimir el resultado
print("El número más grande es:", nmasGrande)

Planta = input("Introduce el nombre de la planta: ")
if Planta == "espatifilo": 
    print("No,¡quiero un gran Espatifilo")
elif Planta == "pelargonio":
    print("!Espatifilo! ¡No pelargonio!")
elif Planta == "Espatifilo":
    print("Si, ¡El Espatifilo es la mejor planta de todos los tiempos")
else:
    print("No es ninguna de las plantas")