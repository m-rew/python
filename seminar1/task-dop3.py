# 3.Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

for i in range(1,101):
    if i >= 5 and i <= 19:
        print(f'{i} процентОВ')
    elif i % 10 == 1:
        print(f'{i} процент')
    elif (i % 10 >= 2 and i % 10 <= 4):
        print(f'{i} процентА')
    elif (i % 10 >= 5 and i % 10 <= 9) or i % 10 == 0:
        print(f'{i} процентОВ')