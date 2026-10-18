import math
x = float(input("Введите x: "))
z1 = (math.tan(x - math.pi / 2) * math.cos(3 * math.pi / 2 + x) - math.sin(3.5 * math.pi - x)**3) / (math.cos(x - 0.5 * math.pi) * math.tan(1.5 * math.pi + x))
z2 = math.sin(x)**2
print("z1 =", z1)
print("z2 =", z2)
