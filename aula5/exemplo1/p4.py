import math

# entrada
a = int(input("a? "))
b = int(input("b? "))
c = int(input("c? "))

# processamento
delta = b ** 2 - 4 * a * c

if delta >= 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

# saída
print(f"    a = {a:10.5f}")
print(f"    b = {b:10.5f}")
print(f"    c = {c:10.5f}")
print(f"delta = {delta:10.5f}")

if delta >= 0:
    print(f"   x1 = {x1:10.5f}")
    print(f"   x2 = {x2:10.5f}")
else:
    print("Equação sem raízes reais")
