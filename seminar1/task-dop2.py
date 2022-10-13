# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

sum1 = 0
sum2 = 0

for i in range(1001):
    # Ищим нечетные числа
    if i % 2 != 0:
        # Возводим в куб
        number1 = i ** 3

        # Прибавляем 17 и заносим отдельно в переменную
        number2 = number1 + 17

        # Засываем каждую цифру числа number1 в лист digits_number_list1
        number1_tem = number1
        digits_number_list1 = [number1_tem % 10]
        while number1_tem >= 10:
            number1_tem //= 10
            digits_number_list1.append(number1_tem % 10)

        # Засываем каждую цифру числа number2 в лист digits_number_list2
        number2_tem = number2
        digits_number_list2 = [number2_tem % 10]
        while number2_tem >= 10:
            number2_tem //= 10
            digits_number_list2.append(number2_tem % 10)

        # Суммируем цифры odd_number_list1, если сумма цифр делится нацело на 7
        if sum(digits_number_list1) % 7 == 0:
            # Суммируем все подходящие числа
            sum1 += number1

        # Суммируем цифры odd_number_list2, если сумма цифр делится нацело на 7
        if sum(digits_number_list2) % 7 == 0:
            # Суммируем все подходящие числа
            sum2 += number2

print(f'Сумма первого варианта: {sum1}')
print(f'Сумма второго варианта: {sum2}')