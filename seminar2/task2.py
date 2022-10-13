# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число: '))

sum_list = []

for i in range(1, number+1):
    sum = 1
    for j in range(2, i+1):
        sum *= j
    sum_list.append(sum)

print(sum_list)