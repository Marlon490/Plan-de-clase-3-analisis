# Sistema de validacion de acceso a parque de diversiones
# Ejercicio 4 MRAG

altura = float(input("Ingresa tu altura: "))

if altura >= 1.30:
    print("Puedes entrar a la montaña rusa")
elif altura >=  1.20 and 1.29:
    print("Debes entrar con acompañante")
elif altura < 1.20:
    print("No puedes entrar")