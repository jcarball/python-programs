año = int(input("introduce el año: "))
if (año % 4 == 0) and (año%100 !=0 or año%400 == 0):
    print("año bisiesto")
else:
    if año < 1583 :
        print("No se encuentra dentro del periodo gregoriano") 
    print("año normal")