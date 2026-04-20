# Diagnostico basico de computadora en Soporte Tecnico
# Ejercicio 6 MRAG

enciende = input("¿La computadora enciende correctamente? si/no: ")

pitidos =  input("¿Escucha algun pitido al encender la maquina? si/no: ")

monitor = input("¿El monitor muestra alguna imagen? si/no: ")
print("\n")
if enciende == "no":
    print("Fallo en la conexion electrica")
elif pitidos == "no":
    print("Fallo en el hardware")
elif monitor == "no":
    print("Fallo en monitor o tarjeta grafica")
else:
    print("Todo funciona perfectamente")
