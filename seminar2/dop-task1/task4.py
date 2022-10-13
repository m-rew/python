# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

file = open('file.txt', 'r')
file_list = [line.strip() for line in file]
file_list = list(map(int, file_list))
file.close()

num1 = int(input('Введите положительное число: '))
num2 = -num1

num_list = []
while num2 <= num1:
    num_list.append(num2)
    num2 += 1
print(f'Созданный лист: {num_list}')

print(f'Индексы для работы с листом: {file_list}')
sum = num_list[file_list[0]]
file_list.pop(0)

for i in range(len(file_list)):
    if file_list[i] < len(num_list):
        sum *= num_list[file_list[i]]

print(f'Произведение элементов: {sum}')