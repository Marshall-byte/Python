import math

print("digite el radio del cilindro")
radio = float(input())

print("digite la altura del cilindro")
altura = float(input())

volumen = math.pi * radio ** 2 * altura

print(f"El volumen del cilindro es: {volumen}")