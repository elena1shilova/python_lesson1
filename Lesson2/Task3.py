# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8
number = int(input('Введи число: '))
power_of_two = 1
while power_of_two <= number:
    print(power_of_two)
    power_of_two *= 2

