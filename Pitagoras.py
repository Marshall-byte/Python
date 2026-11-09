import math

print("Digite el primer cateto")
cateto1 = float(input())

print("Digite el segundo cateto")
cateto2 = float(input())

hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

print("la hipotenusa del triangulo rectangulo es: ", hipotenusa)