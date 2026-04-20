# Evaluador de seguridad de contraseñas
# Ejercicio 8 MRAG

contraseña = input("Ingresar una contraseña: ")
# Calculamos de cuantos caracteres es la contraseña
caracteres = len(contraseña)
# Verificamos si tiene algun numero
numeros = any(char.isdigit() for char in contraseña)
# verificamos si contiene mayusculas
mayusculas = any(char.isupper() for char in contraseña)

# Evaluamos la seguridad de la contraseña
if caracteres >= 12 and numeros and mayusculas:
    print("Contraseña fuerte")
elif caracteres >= 8 and (numeros or mayusculas):
    print("Contraseña moderada. Se recomienda mejorar")
else:
    print("Contraseña debil. Cambio inmediato")
# Mostramos los detalles
print("Longitud de la contraseña: ", caracteres)
print("¿Contiene numeros?: ", numeros)
print("¿Contiene mayusculas?: ", mayusculas)


