# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Задайте натуральную степень: ')) + 1
coff_list = []
some_list = []

for i in range(k):
    coff_list.append(random.randint(0, 100))
    if i == k-1 and coff_list[i] == 0:
        while coff_list[i] == 0:
            coff_list[i] = random.randint(0, 100)

while k >= 0:
    if k - 1 > 1:
        if coff_list[k-1] != 0:
            some_list.append(f'{coff_list[k-1]}*x^{k-1}')

    if k - 1 == 1:
        if coff_list[k-1] != 0:
            some_list.append(f'{coff_list[k-1]}*x')

    if k - 1 == 0:
        if coff_list[k-1] != 0:
            some_list.append(f'{coff_list[k-1]}')

    k -= 1

stt = ' + '.join(some_list) + ' = 0'

file = open("output.txt", "w+")
file.write(stt)
file.close()