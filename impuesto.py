ingreso=float(input("Ingrese el ingreso anual:"))

if ingreso < 85528.0 :
    impuesto = ingreso*0.18-556.2
elif ingreso > 85528.0:
    impuesto = 14839 + ((ingreso - 85528.0)*0.32)

if impuesto< 0 :
        impuesto = 0
impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")