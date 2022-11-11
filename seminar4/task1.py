# Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

number = float(input('Введите вещественное число: '))
pattern = float(input('Задайте паттерн (пример: 0.01): '))

if pattern <= (10 ** -1) and pattern >= (10 ** -10):
    pattern = str(pattern)
    number = str(number)

    if len(pattern) < len(number):
        print(number[0:len(pattern)])
    else:
        print(number)
else:
    print('Паттерн должен быть от 0.1 до 0.0000000001')