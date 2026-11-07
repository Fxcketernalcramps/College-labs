import turtle

# Настройка экрана
screen = turtle.Screen()
screen.title("Задание 3: График функции через новый ряд (с полной разметкой)")
screen.setup(width=0.8, height=0.8)
screen.bgcolor("#ffffff")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Исходные данные на основе файла 6
a, b, h = -0.8, 0.8, 0.02
e = 10**-3  # Точность 10^-3 по заданию

# Масштабы осей (растягиваем сетку под интервал сходимости)
scale_x = screen.window_width() // 2.2
scale_y = screen.window_height() // 4

# --- РИСУЕМ КООРДИНАТНУЮ СЕТКУ И ЗАСЕЧКИ ---
t.color("#bdc3c7")
# Главные оси
t.goto(0, -2 * scale_y); t.pendown(); t.goto(0, 2 * scale_y); t.penup() # Ось Y
t.goto(-scale_x, 0); t.pendown(); t.goto(scale_x, 0); t.penup() # Ось X

t.color("#7f8c8d")
# Подробные засечки и числовые градации по оси X (шаг 0.2)
x_ticks = [-0.8, -0.6, -0.4, -0.2, 0.2, 0.4, 0.6, 0.8]
for x_val in x_ticks:
    t.goto(x_val * scale_x, -5)
    t.pendown()
    t.goto(x_val * scale_x, 5)
    t.penup()
    t.goto(x_val * scale_x, -20)
    t.write(f"{x_val:.1f}", align="center", font=("Arial", 9, "normal"))

# Подробные засечки и числовые градации по оси Y (шаг 0.5)
y_ticks = [-1.5, -1.0, -0.5, 0.5, 1.0, 1.5]
for y_val in y_ticks:
    t.goto(-5, y_val * scale_y)
    t.pendown()
    t.goto(5, y_val * scale_y)
    t.penup()
    t.goto(10, y_val * scale_y - 5)
    t.write(f"{y_val:.1f}", align="left", font=("Arial", 9, "normal"))

# Подписи названий самих осей
t.goto(scale_x - 15, -20); t.write("X", font=("Arial", 11, "bold"))
t.goto(15, 2 * scale_y - 20); t.write("Y", font=("Arial", 11, "bold"))

# Заголовок сверху
t.goto(0, screen.window_height() // 2 - 40)
t.color("#2c3e50")
t.write("График функции через ряд (Задание 3)", align="center", font=("Arial", 14, "bold"))

# --- РАСЧЕТ ЗНАЧЕНИЙ И ПОСТРОЕНИЕ ЛИНИИ ФУНКЦИИ ---
t.penup()
t.color("#9b59b6")
t.pensize(3)

x = a
first_point = True

while x <= b:
    # Инициализация переменных строго по файлу 6
    s = 1.0
    n = 0
    t_val = 1.0
    
    # Вложенный цикл подсчета суммы ряда с заданной точностью e
    while abs(t_val) >= e and n < 1000:
        n += 1
        t_val = t_val * (-(3 * n - 2) / (3 * n)) * x
        s += t_val
        
    # Перемещение пера turtle по вычисленным точкам
    if first_point:
        t.goto(x * scale_x, s * scale_y)
        t.pendown()
        first_point = False
    else:
        t.goto(x * scale_x, s * scale_y)
        
    x = round(x + h, 10)

screen.mainloop()
