#Parcial John Fernando Farnco Franco

#Primer ejercicio
op = int(input("Si desea ingresar al programa ingrese 1"))
while op == 1:
 num = float(input("Ingrese un numero positivo al que desea el cuadrado"))

 if num >= 0:
    cu = num**2
    print("su numero es: ",cu)
 else:
    print("su numero es negativo")

 op = int(input("Si desea volver a ingresar al programa ingrese 1"))

    
