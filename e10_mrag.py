# Validacion de elegibilidad para bono de desempeño
# Ejercicio 10 MRAG

nombre = input("Introduce tu nombre: ")
proyectos = int(input("¿Cuantos proyectos completaste este año?"))
cursos = int(input("¿Cuantos cursos de formación completaste este año? "))
reconocimiento = input("¿Recibiste un reconocimiento oficial? (si/no): ")

if proyectos >= 5 and cursos >= 3 and reconocimiento == "si":
    print(nombre, ", Felicidades Eres elegible para el bono maximo.")
elif proyectos >= 3 and cursos >= 2:
    print(nombre, ", Eres elegible para un bono estándar.")
elif proyectos >= 1:
    print(nombre, ", Recibirás un bono de participación.")
else:
    print(nombre, ", No calificas para bono este año. ¡Ánimo para la próxima!")