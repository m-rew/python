# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите X: '))
y = int(input('Введите Y: '))

if x > 0 and y > 0:
    print('Точка находится на 1 четвери')
elif x < 0 and y > 0:
    print('Точка находится на 2 четвери')
elif x < 0 and y < 0:
    print('Точка находится на 3 четвери')
elif x > 0 and y < 0:
    print('Точка находится на 4 четвери')
else:
    print('Точка находится на начале координат')