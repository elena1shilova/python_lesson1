# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# a1 = int(input("Введите первый элемент прогрессии: "))
# d = int(input("Введите разность прогрессии: "))
# n = int(input("Введите количество элементов: "))

# progression = [a1 + (i * d) for i in range(n)]

# print("Массив элементов арифметической прогрессии:")
# for num in progression:
#     print(num)

# /////////////////////////////////////////////////////////
# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# def find_indices(array, minimum, maximum):
#     indices = []
#     for i in range(len(array)):
#         if minimum <= array[i] <= maximum:
#             indices.append(i)
#     return indices


# my_array = [1, 5, 3, 8, 2, 7, 4, 6]
# min_value = 3
# max_value = 6

# result = find_indices(my_array, min_value, max_value)
# print("Индексы элементов, значения которых находятся в диапазоне от", min_value, "до", max_value, ":")
# print(result)
