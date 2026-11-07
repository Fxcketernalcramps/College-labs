import turtle
import math
import random

# Настройка экрана
screen = turtle.Screen()
screen.title("Задание 2: Метод Монте-Карло (Новая фигура)")
screen.setup(width=0.8, height=0.8)
screen.bgcolor("#ffffff")

# Отключаем пошаговую трассировку для мгновенного рендеринга 10000 точек
screen.tracer(0, 0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Данные на основе лабы 3.2
R = 4.0
N = 10000  # До 10 000 испытаний по заданию
scale = min(screen.window_width(), screen.window_height()) // (R * 2.5)

# Отрисовка осей координат
t.color("#bdc3c7")
t.goto(0, -int(R+1)*scale); t.pendown(); t.goto(0, int(R+1)*scale); t.penup()
t.goto(-int(R+1)*scale, 0); t.pendown(); t.goto(int(R+1)*scale, 0); t.penup()

# Градация осей
t.color("#7f8c8d")
for val in [-int(R), int(R)]:
    t.goto(val * scale, -5); t.pendown(); t.goto(val * scale, 5); t.penup()
    t.goto(val * scale, -20); t.write(f"{val}(R)", align="center", font=("Arial", 9))

hits = 0
# Прямоугольная область генерации точек вокруг круга
x_min, x_max = -R, R
y_min, y_max = -R, R
S_rect = (x_max - x_min) * (y_max - y_min)

# Моделирование 10 000 выстрелов
for _ in range(N):
    x = random.uniform(x_min, x_max)
    y = random.uniform(y_min, y_max)
    
    # Вложенная проверка попадания 
    is_hit = False
    if x * x + y * y <= R * R:
        if (x >= 0 and y >= x) or (x <= 0 and y <= x):
            is_hit = True
            
    t.penup()
    t.goto(x * scale, y * scale)
    if is_hit:
        hits += 1
        t.dot(3, "#2ecc71")  # Зелёный пиксель — попал
    else:
        t.dot(2, "#dfe6e9")  # Серый пиксель — мимо

# Расчёт экспериментальной площади по Монте-Карло
S_calc = (hits / N) * S_rect

# Точная геометрическая площадь:
# Условия (y >= x при x >= 0) и (y <= x при x <= 0) вырезают два противоположных сектора по 45 градусов.
# Итого: 45° + 45° = 90° (это ровно 1/4 часть круга радиуса R).
S_real = (math.pi * (R**2)) / 4
error_pct = abs(S_calc - S_real) / S_real * 100

# Вывод результатов текстом в левый нижний угол экрана
t.penup()
t.goto(-screen.window_width() // 2 + 40, -screen.window_height() // 2 + 40)
t.color("#2c3e50")
t.write(f"Реальная площадь фигуры: {S_real:.4f}\n"
        f"Площадь по Монте-Карло: {S_calc:.4f}\n"
        f"Оценка погрешности: {error_pct:.2f}%", 
        font=("Arial", 11, "bold"))

# Однократное обновление экрана для вывода результата
screen.update()
screen.mainloop()
