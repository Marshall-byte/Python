import math

print("ingrese el radio del circulo")
r = float(input())

area = math.pi * r * r
perimetro = 2 * math.pi * r

print(f"su area es: {area}")
print(f"su perimetro es: {perimetro}")