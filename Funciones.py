import math


print("Digite el numero a operar")
num = float(input())

seno = math.sin(num)
coseno = math.cos(num)
tangente = math.tan(num)
logaritmoNatural = math.log(num)
logaritmo10 = math.log(num) / math.log(10)
raizz = math.sqrt(num)

print("el seno del numero es: , ", seno)
print("el coseno del numero es: , ", coseno)
print("la tangente del numero es: , ", tangente)
print("el logaritmo natural del numero es: , ", logaritmoNatural)
print("el logaritmo10 del numero es: , ", logaritmo10)
print("la raizz del numero es: , ", raizz)