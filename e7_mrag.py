# Sistema de asignacion de proyectos para desarrolladores
# Ejercicio 7 MRAG

anios_experiencia = int(input("Introduce tus años de experiencia en programación:"))

tecnologia = input("¿Prefieres trabajar en (backend/frontend/fullstack)? ").lower()

if anios_experiencia >= 5:
    senior = True
else:
    senior = False
if tecnologia == "backend" and senior:
    print("Proyecto asignado: Microservicios para banca digital.")
elif tecnologia == "frontend" and senior:
    print("Proyecto asignado: Plataforma de ventas en tiempo real.")
elif tecnologia == "fullstack" and senior:
    print("Proyecto asignado: Sistema ERP completo.")
elif tecnologia == "backend" and not senior:
    print("Proyecto asignado: APIs básicas para e-commerce.")
elif tecnologia == "frontend" and not senior:
    print("Proyecto asignado: Diseno de landing pages.")
elif tecnologia == "fullstack" and not senior:
    print("Proyecto asignado: Módulo de autenticación de usuarios.")
else:
    print("Error: Tecnologia ingresada no reconocida.")
