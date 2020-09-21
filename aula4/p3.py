import sys
import math

# entrada
a = int(input("a? "))
b = int(input("b? "))
c = int(input("c? "))

# processamento
delta = b ** 2 - 4 * a * c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)

else:
    print(f"Ops! O delta é negativo:{delta}")
    sys.exit(1)

# saída
print(f"    a = {a:10.5f}")
print(f"    b = {b:10.5f}")
print(f"    c = {c:10.5f}")
print(f"delta = {delta:10.5f}")
print(f"   x1 = {x1:10.5f}")
