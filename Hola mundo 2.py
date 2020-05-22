print("Me gusta \"Monty Python\"")
print('I\'m Monty Python.')
print("I'm Monty Python.")
print('"Estoy""aprendiendo"""""Python"""')
print('"Estoy"\n""aprendiendo""\n"""Python"""')

print(9 % 6 % 2)

kilometros = 12.25
millas = 7.38

millas_a_kilometros = millas*1.61
kilometros_a_millas = kilometros/1.61

print(millas, " millas son ", round(millas_a_kilometros, 2), " kilómetros ")
print(kilometros, " kilómetros son ", round(kilometros_a_millas, 2), " millas ")

Dolar = 5000
Colones = 128000
DolarUS = 0.0018
DolarCR = 567.64

Dolar_a_colones = DolarUS*Dolar
Colones_a_dolares = Colones/DolarCR

print(Colones, "colones a dolares son ", round(Dolar_a_colones, 2), "dolares")
print(Dolar,  "dolares a colones son ", round(Colones_a_dolares, 2), "colones")

real = 0.56e-3
print (real, type(real))

nom = input("¿Me puedes dar tu nombre por favor? ")
ape = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias.")
print("\nTu nombre es " + nom + " " + ape + ".")

cateto_a = float(input("Inserta la longitud del primer cateto: "))
cateto_b = float(input("Inserta la longitud del segundo cateto "))
hipo = (cateto_a**2 + cateto_b**2) ** .5
print("La longitud de la hipotenusa es: ", hipo)

cateto_a = float(input("Ingresa la longitud del primer cateto: "))
cateto_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es: " + str((cateto_a**2 + cateto_b**2) ** .5))

x = float(input("Ingresa el valor para x: "))

# coloca tu código aquí
y = 1/(x +(1/(x+(1/(x +(1/x))))))
print("y =", y)
