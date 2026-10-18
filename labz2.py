import math

x = float(input("Введите x: "))

if -5 <= x <= -4:
    y = -3
elif -4 < x < -3:
    y = 3 * x + 9
elif -3 <= x <= 3:
    y = math.sqrt(9 - x**2)
elif 3 < x < 8:
    y = 3 * (x - 3) / 5
elif 8 <= x <= 10:
    y = 3
else:
    y = "не задано"

print("y =", y)