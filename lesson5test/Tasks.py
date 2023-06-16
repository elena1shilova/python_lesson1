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


# ////////////////////////////////////////////////
# Задача 28: Вводится десятичное число. Реализовать алгоритм его перевода в двоичную систему счисления 
# через рекурсию. Нельзя использовать функцию bin()
# *Пример:*
#     10
#     *Вывод:*
#     1010

# def decimal_to_binary(n):
#     if n == 0:
#         return ""
#     else:
#         return decimal_to_binary(n // 2) + str(n % 2)

# decimal_number = int(input("Введите десятичное число: "))

# binary_number = decimal_to_binary(decimal_number)

# print(f"Двоичное представление числа {decimal_number}: {binary_number}")
