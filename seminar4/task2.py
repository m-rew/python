# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# !! Разложение числа на множители (неправильно понял задачу)
# number = int(input('Введите натуральное число: '))
# flag_prime = 0
# prime_factors_of_number = []
#
# # Проверяем на простое число
# for i in range(2, number+1):
#     if i != number:
#         if number % i == 0:
#             flag_prime = 1
#             break
#     else:
#         if number % i == 0:
#             flag_prime = 0
#
# if flag_prime == 1:
#     print(f'{number} - не является простым числом')
#     while number != 1:
#         for i in range(2, number):
#             for j in range(2, i+1):
#                 if i % j != 0:
#                     if i % j == 1: # Число не простое
#                         break
#                 else:
#                     if i % j == 0: # Число простое
#                         if number % j == 0:
#                             print(f'{number} делится нацело на {j}: {number} / {j} = {int(number / j)}')
#                             number = int(number / j)
#                             prime_factors_of_number.append(j)
#
#     print(f'Результат: {prime_factors_of_number}')
#
# else:
#     print(f'{number} - является простым числом')

number = int(input('Введите натуральное число: '))
prime_factors_of_number = []

for i in range(2, number+1):
    for j in range(2, i+1):
        if i != j:
            if i % j == 0: # Число i не простое
                break
        else:
            if i % j == 0: # Число i простое
                if number % i == 0:
                    prime_factors_of_number.append(i)

print(f'Простые множители числа {number}: {prime_factors_of_number}')