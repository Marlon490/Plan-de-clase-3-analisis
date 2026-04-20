# Sistema de clasificacion de temperatura
# Ejercicio 1 MRAG

temperatura = float(input("Introduce la temperatura actual en grados Celsius: "))

if temperatura > 35:
    print("Alerta: Calor extremo")
elif temperatura >= 26 and 35:
    print("Hace calor")
elif temperatura >= 16 and 25:
    print("Clima agradable")
elif temperatura >= 6 and 15:
    print("Hace frio")
elif temperatura <= 5:
    print("Alerta: Frio extremo")
else:
    print("Incorrecto")