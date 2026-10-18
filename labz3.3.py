a = float(input("a = "))
b = float(input("b = "))
h = float(input("шаг = "))
e = float(input("точность = "))

print("x\t y\t членов")

x = a
while x <= b:
    s = 1
    n = 0
    t = 1

    while abs(t) >= e:
        n += 1
        t = t * (-(3 * n - 2) / (3 * n)) * x
        s += t

    print(x, "\t", s, "\t", n)
    x += h