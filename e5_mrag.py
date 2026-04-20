# Menu interactivo de seleccion de bebidas
# Ejercicio 5

opcion = input("Elige una opcion de la cafeteria: ")

opcion1 = "Cafe"
opcion2 = "Te"
opcion3 = "Chocolate caliente"

if opcion1:
    print("El cafe esta caliente")
elif opcion2:
    print("El te esta servido")
elif opcion3:
    print("Chocolate caliente (:")
else:
    print("Opcion no valida")