print("ingrese el sueldo del empleado")
sueldo = float(input())

salud = sueldo * 0.04
pension = sueldo * 0.04
descuento = salud + pension
totalPagar = sueldo - descuento

print(f"El sueldo total a pagar al empleado es: {totalPagar}")