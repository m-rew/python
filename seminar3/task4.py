# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = float(input('Введите число: '))
some_str = ''

while num != 0:
    some_str += str(int(num % 2))
    num = num // 2

some_str = res=''.join(reversed(some_str))

print(f'Десятичное число: {some_str}')