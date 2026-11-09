print("digite el valor de dinero ingresado")
cantidadDinero = float(input())

print("digite el periodo en dias")
peridoDias = float(input())

print("digite el porcentaje de interes")
porcentajeIntereses = float(input())

valorIntereses = (cantidadDinero * porcentajeIntereses * peridoDias) / 360
impuestos = valorIntereses * 0.07
totalPagar = cantidadDinero + valorIntereses - impuestos

print("el valor de los interes ganados es: ", valorIntereses)
print("el total a retirar es: ", totalPagar)