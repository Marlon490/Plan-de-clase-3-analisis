# Clasificacion de tickets de soporte tecnico
# Ejercicio 9 MRAG

area = input("¿En qué área es el problema? (software/hardware/red): ")

gravedad = input("¿Qué tan grave es el problema? (alta/media/baja): ")

if area == "software" and gravedad == "alta":
    print("Ticket: Prioridad critica. Escalar a desarrolladores senior.")
elif area == "software" and gravedad == "media":
    print("Ticket: Prioridad alta. Resolver en menos de 24 horas.")
elif area == "hardware" and gravedad == "alta":
    print("Ticket: Prioridad critica. Enviar equipo de reparación.")
elif area == "hardware" and gravedad == "media":
    print("Ticket: Prioridad alta. Evaluacion remota.")
elif area == "red" and gravedad == "alta":
    print("Ticket: Prioridad critica. Escalar a administradores de red.")

elif area == "red" and gravedad == "media":
    print("Ticket: Prioridad alta. Diagnóstico inmediato.")
else:
    print("Ticket: Prioridad normal. Programar revisión en 48 horas.")