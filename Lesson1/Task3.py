"""
Вы пользуетесь общественным транспортом? Вероятно,
вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.
Пример:
385916 -> yes
123456 -> no
"""
lucky_ticket = int(input('Введите 6-значный номер билета: '))
if 99999 < lucky_ticket < 1000000:
    if (lucky_ticket % 10 + int(lucky_ticket / 10 % 10) + int(lucky_ticket / 100 % 10)) == int(lucky_ticket / 1000 % 10 + int(lucky_ticket / 10000 % 10) + int(lucky_ticket / 100000 % 10)):
        print('Счастливый билет!!!!! Ура!')
    else:
        print('Билет обычный, увы')
else:
    print('Прочитай условие и попробуй еще раз!')
