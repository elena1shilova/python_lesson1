# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
from random import randint
number_coin = int(input('Введи кол-во монеток: '))
count_coin0 = 0 #будет герб
count_coin1 = 0 #будет решка
for i in range(1, number_coin + 1):
    side_coin = randint(0, 1)
    print(side_coin)
    if side_coin == 0: count_coin0 += 1
    else: count_coin1 += 1
if count_coin0 > count_coin1: print(f'Из {number_coin} монет -> {count_coin1} монет(ы) с решкой, переверни их')
elif count_coin0 < count_coin1: print(f'Из {number_coin} монет -> {count_coin0} монет(ы) с гербом, переверни их')
else: print('Смотри сам, кол-во монет с решкой и гербом равно')

