# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 
# def power_recursive(a, b):
#     if b == 0:
#         return 1
#     elif b < 0:
#         return 1 / power_recursive(a, -b)
#     elif b % 2 == 0:
#         half_power = power_recursive(a, b // 2)
#         return half_power * half_power
#     else:
#         return a * power_recursive(a, b - 1)

# A = 3
# B = 5
# result = power_recursive(A, B)
# print(f"{A} в степени {B} равно {result}")

# A = 2
# B = 3
# result = power_recursive(A, B)
# print(f"{A} в степени {B} равно {result}")


# ///////////////////////////////////////
# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

# def sum_recursive(a, b):
#     if a == 0:
#         return b
#     elif b == 0:
#         return a
#     elif a > 0:
#         return sum_recursive(a - 1, b + 1)
#     else:
#         return sum_recursive(a + 1, b - 1)

# a = 2
# b = 2
# result = sum_recursive(a, b)
# print(f"Сумма чисел {a} и {b} равна {result}")

# a = 4
# b = 7
# result = sum_recursive(a, b)
# print(f"Сумма чисел {a} и {b} равна {result}")
