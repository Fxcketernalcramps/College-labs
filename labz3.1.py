import math

x1 = float(input("Введите начальное значение x: "))
x2 = float(input("Введите конечное значение x: "))
dx = float(input("Введите шаг dx: "))

print("x        y")

x = x1

while x <= x2:
    if x <= -8:
        y = -3
    elif x <= -3:
        y = 3 * (x + 3) / 5
    elif x <= 3:
        y = -math.sqrt(9 - x**2)
    elif x < 5:
        y = 2 - math.sqrt(4 - (x - 3)**2)
    else:
        y = 3

    print(x, y)
    x = round(x + dx, 10)