# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число: ')) - 1
some_list1 = [0, 1]
some_list2 = [0, 1]

i = 2
nn = n
while nn > 0:
    some_list1.append(some_list1[i-1] + some_list1[i-2])
    nn -= 1
    i += 1

i = 2
nn = n
while nn > 0:
    some_list2.append(some_list2[i-2] - some_list2[i-1])
    nn -= 1
    i += 1

for _, el in enumerate(some_list2):
    some_list1.insert(0, el)

print(some_list1)