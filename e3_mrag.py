# Calculadora de descuentos en supermercado
# Ejercicio 3 MRAG

monto = float(input("Ingrese el monto de compra y veremos si hay descuento: "))

if monto >= 500:
    descuento = monto * 0.20
elif monto >= 300 and 500:
    descuento = monto * 0.15
elif monto >= 100 and 299:
    descuento = monto * 0.10
else:
    descuento = 0

total_pagar = monto - descuento

print("Total antes del descuento: Q", monto)
print("Descuento aplicado: Q", descuento)
print("Total a pagar: Q", total_pagar)
