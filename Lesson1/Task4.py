# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no
chocolate_length = int(input('Введи длину шоколадки: '))
chocolate_width = int(input('Введи ширину шоколадки: '))
chocolate_slices = int(input('Введи сколько долек хочешь: '))
if chocolate_slices % chocolate_length == 0 or chocolate_slices % chocolate_width == 0:
    print('yes')
else:
    print('no')

