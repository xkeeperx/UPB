# tarifas de vehiculos peaje UPB
vehiculo = int(input("Ingrese la categoria: "))
if(vehiculo == 1):
    print("Vehiculo Ligeros  Tarifa : $/14.800")
elif(vehiculo == 2):
    print("Vehiculo Pesados **2 ejes  Tarifa : $/29.600")
elif(vehiculo == 3):
    print("Vehiculo Pesados **3 ejes  Tarifa : $/44.400")
elif(vehiculo == 4):
    print("Vehiculo Pesados **4 ejes  Tarifa : $/59.200")
elif(vehiculo == 5):
    print("Vehiculo Pesados **5 ejes  Tarifa : $/74.000")
elif(vehiculo == 6):
    print("Vehiculo Pesados **6 ejes  Tarifa : $/88.000")
elif(vehiculo == 7):
    print("Vehiculo Pesados **7 ejes  Tarifa : $/103.600")
else:
    print("Categoria invalida")
