# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

some_list = list(map(int, input('Задайте последовательность чисел через запятую: ').split(',')))

i = 0
j = 0
while i < len(some_list):
    j = i + 1
    while j < len(some_list):
        if some_list[i] == some_list[j]:
            some_list.pop(j)
        else:
            j += 1
    i += 1

print(some_list)