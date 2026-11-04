
from math import *

#Лабораторная работа №5

def perestanovka(a, n):
    """Создаём копию исходной матрицы и меняем блоки крест-накрест"""
    b = [stroka[:] for stroka in a]
    for i in range(n):
        for j in range(n):
            b[i][j] = a[i + n][j + n]
            b[i][j + n] = a[i + n][j]
            b[i + n][j] = a[i][j + n]
            b[i + n][j + n] = a[i][j]
    return b

def proizv_blokov_to_str(a, n):
    """Находим произведение четырёх блоков матрицы и возвращаем в виде текста"""
    result_text = ""
    for x in range(0, 2 * n, n):
        for y in range(0, 2 * n, n):
            p = 1
            for i in range(x, x + n):
                for j in range(y, y + n):
                    p *= a[i][j]
            result_text += f"Произведение блока: {p}\n"
    return result_text

def main():
    import os
    
    # Автоматическое определение папки где лежит сам скрипт
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_in = os.path.join(current_dir, "input.txt")
    file_out = os.path.join(current_dir, "output.txt")
    
    # Безопасное чтение файла
    try:
        with open(file_in, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Ошибка! Не найден входной файл: {file_in}")
        return
    except Exception as err:
        print(f"Произошла ошибка при открытии файла: {err}")
        return

    # Проверяем минимальное количество строк
    if len(lines) < 5:
        print("Ошибка! В файле недостаточно строк для считывания всех условий.")
        return

    try:
        # Cмотрим Лабу 1 (строка 1)
        x_val = float(lines[0].strip())
        
        # Смотрим Лабу 4 (строка 2 и строка 4)
        y = float(lines[1].strip())
        n_l4 = int(lines[2].strip()) # берем n как размерность для матрицы, а для массива посчитаем по факту
        
        l4_array = []
        for val in lines[3].strip().split():
            l4_array.append(float(val))
            
        # Смотрим Лабу 5 (строка 3 для n и строки с 5-й до конца для матрицы)
        n_l5 = int(lines[2].strip())
        my_matrix = []
        for line in lines[4:]:
            cleaned = line.strip()
            if cleaned:
                row = list(map(int, cleaned.split()))
                my_matrix.append(row)
                
    except ValueError:
        print("Ошибка! В файле обнаружены некорректные символы вместо чисел.")
        return

    # ЛАБОРАТОРНАЯ РАБОТА №1
    # Удалены префиксы перед функциями так как импортировано через * (или оставлены стандартные вызовы)
    z1 = (tan(x_val - pi / 2) * cos(3 * pi / 2 + x_val) - sin(3.5 * pi - x_val)**3) / (cos(x_val - 0.5 * pi) * tan(1.5 * pi + x_val))
    z2 = sin(x_val)**2

    # ЛАБОРАТОРНАЯ РАБОТА №4
    # Сортируем массив по убыванию согласно условию исходной лабы
    l4_array.sort(reverse=True)
    len_a = len(l4_array)
    
    l4_error = None
    k = -1
    total_sum = 0
    after_elements = []

    if y >= l4_array[0] or y <= l4_array[len_a - 1]:
        l4_error = "Число y должно быть меньше первого и больше последнего элемента."
    else:
        for i in range(len_a - 1):
            if l4_array[i] > y and y > l4_array[i + 1]:
                k = i
                break
        if k == -1:
            l4_error = "Не удалось найти подходящие соседние элементы."
        else:
            after_elements = l4_array[k + 1:]
            total_sum = sum(after_elements)
            after_elements.sort(reverse=True)

    # ЛАБОРАТОРНАЯ РАБОТА №5
    if len(my_matrix) != 2 * n_l5:
        print(f"Предупреждение: Высота матрицы не соответствует размеру 2*n ({2*n_l5} строк).")
    
    matrix_b = perestanovka(my_matrix, n_l5)
    proizv_a = proizv_blokov_to_str(my_matrix, n_l5)
    proizv_b = proizv_blokov_to_str(matrix_b, n_l5)

    # Запись результатов в txt 
    try:
        with open(file_out, "w", encoding="utf-8") as out:
            out.write("ОТЧЕТ ПО КОМПЛЕКСНОЙ ЛАБОРАТОРНОЙ РАБОТЕ №6\n")
        
            # Раздел 1
            out.write(" 1. Результаты Лабораторной работы №1 \n")
            out.write(f"Входной параметр x = {x_val}\n")
            out.write(f"Результат z1 = {z1}\n")
            out.write(f"Результат z2 = {z2}\n\n")
            
            # Раздел 2
            out.write(" 2. Результаты Лабораторной работы №4 \n")
            out.write(f"Отсортированный исходный массив: {l4_array}\n")
            out.write(f"Параметр y = {y}\n")
            if l4_error:
                out.write(f"Результат вычислений: {l4_error}\n\n")
            else:
                out.write(f"Найденный индекс k = {k + 1}\n")
                out.write(f"Элемент a[k] = {l4_array[k]}\n")
                out.write(f"Сумма элементов после a[k]: {total_sum}\n")
                out.write(f"Элементы после a[k] по убыванию: {after_elements}\n\n")
                
            # Раздел 3
            out.write(" 3. Результаты Лабораторной работы №5 \n")
            out.write("Исходная матрица A:\n")
            for row in my_matrix:
                out.write(" ".join(map(str, row)) + "\n")
                
            out.write("\nНовая матрица B (после перестановки блоков):\n")
            for row in matrix_b:
                out.write(" ".join(map(str, row)) + "\n")
                
            out.write("\nПроизведения блоков исходной матрицы:\n")
            out.write(proizv_a)
            
            out.write("\nПроизведения блоков новой матрицы:\n")
            out.write(proizv_b)
           
            
        print(f"Все вычисления успешно сохранены в файл: {file_out}")
    except Exception as e:
        print(f"Ошибка при записи файла отчета: {e}")

if __name__ == "__main__":
    main()