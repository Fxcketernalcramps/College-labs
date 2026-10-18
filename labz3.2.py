import random

R = float(input("Введите радиус R: "))

for i in range(10):
    x = random.uniform(-R, R)
    y = random.uniform(-R, R)

    if x * x + y * y <= R * R:
        if (x >= 0 and y >= x) or (x <= 0 and y <= x):
            print("Выстрел", i + 1, "попал")
        else:
            print("Выстрел", i + 1, "не попал")
    else:
        print("Выстрел", i + 1, "не попал")

    print("Координаты:", x, y)