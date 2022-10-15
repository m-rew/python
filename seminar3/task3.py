# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

some_list = [1.1, 1.2, 3.1, 5, 10.01, 4]

for i, el in enumerate(some_list):
    if not ('.' in str(el)):
        some_list.pop(i)

for i, el in enumerate(some_list):
    some_list[i] = float('0.' + str(el).split('.')[1])

print(max(some_list) - min(some_list))