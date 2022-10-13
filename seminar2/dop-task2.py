# Реализуйте алгоритм перемешивания списка

import random

some_list = input('Введите числа через пробел: ').split(' ')

print(f'Исходный список: {some_list}')

num_rnd = random.randint(10, 100)

for i in range(0, num_rnd + 1):
    rnd_index1 = random.randint(0, len(some_list) - 1)
    rnd_index2 = random.randint(0, len(some_list) - 1)
    some_list[rnd_index1], some_list[rnd_index2] = some_list[rnd_index2], some_list[rnd_index1]

print(f'Новый список: {some_list}')