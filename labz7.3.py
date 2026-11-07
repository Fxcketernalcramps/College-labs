import turtle
import math

# Настройка экрана
screen = turtle.Screen()
screen.title("Задание 1: График новой составной функции")
screen.setup(width=0.8, height=0.8)
screen.bgcolor("#ffffff")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Исходные данные из 3.3
x1, x2, dx = -9.0, 6.0, 0.05

# Масштабирование под размер экрана пользователя
scale = min(screen.window_width(), screen.window_height()) // 20

# Рисуем сетку и оси
t.color("#bdc3c7")
t.goto(0, -5 * scale); t.pendown(); t.goto(0, 5 * scale); t.penup() # Ось Y
t.goto(-10 * scale, 0); t.pendown(); t.goto(7 * scale, 0); t.penup() # Ось X

# Числовая градация по осям
t.color("#7f8c8d")
for x_val in range(int(x1) - 1, int(x2) + 2):
    if x_val != 0:
        t.goto(x_val * scale, -5); t.pendown(); t.goto(x_val * scale, 5); t.penup()
        t.goto(x_val * scale, -20); t.write(str(x_val), align="center", font=("Arial", 9))

# Заголовок
t.goto(0, screen.window_height() // 2 - 40)
t.color("#2c3e50")
t.write("График составной функции (Задание 1)", align="center", font=("Arial", 14, "bold"))

# Отрисовка графика
t.penup()
t.color("#e74c3c")
t.pensize(3)

x = x1
first_point = True

while x <= x2:
    # Логика ветвления 
    if x <= -8:
        y = -3.0
    elif x <= -3:
        y = 3 * (x + 3) / 5
    elif x <= 3:
        val = max(0.0, 9 - x**2)
        y = -math.sqrt(val)
    elif x < 5:
        val = max(0.0, 4 - (x - 3)**2)
        y = 2 - math.sqrt(val)
    else:
        y = 3.0
        
    if first_point:
        t.goto(x * scale, y * scale)
        t.pendown()
        first_point = False
    else:
        t.goto(x * scale, y * scale)
        
    x = round(x + dx, 10)

screen.mainloop()
