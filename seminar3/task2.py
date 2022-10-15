# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math

some_list = list(map(int, input().replace(',', '').split(' ')))
print(some_list, '=> ', end = '')
mult_list = []

for i in range(math.ceil(len(some_list) / 2)):
    mult_list.append(some_list[i] * some_list[-i - 1])

print(mult_list)