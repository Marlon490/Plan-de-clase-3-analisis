# Verificamos la contraseña
# Ejercicio 12 MRAG

contra = "contraseña"
password = input("Introduce la contraseña: ")
if contra == password.lower():
    print("La contraseña coincide")
else:
    print("La contraseña no coincide")