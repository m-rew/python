# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#
# Пример:
#
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input('Введите число: '))

some_list = []
sum = 0

for i in range(1, number+1):
    sum += (1 + 1 / i) ** i
    result = int(((1 + 1 / i) ** i) * 100) / 100

    if result % 2 == 0:
        result = int(result)

    some_list.append(f'{i}: {result}')

print(f'Для n = {number}: {some_list}')
print(f'Сумма: {int(sum * 100) / 100}')