from templates import get_template
from logger import write_log

# Функция выводит решение на экран и логирует
def main(sign, values):
    value1, value2 = values
    result = definition_operation(sign, value1, value2)
    print(result)
    write_log(result)

# Функция определения и вызова операции
def definition_operation(sign, value1, value2):
    match sign:
        case '+':
            return get_sum(sign, value1, value2)
        case '-':
            return get_sub(sign, value1, value2)
        case '*':
            return get_mult(sign, value1, value2)
        case '/':
            return get_div(sign, value1, value2)

# Функция сложения
def get_sum(sign, value1, value2):
    return str(get_template(sign, value1, value2) + f'{value1 + value2}')

# Функция вычитания
def get_sub(sign, value1, value2):
    return str(get_template(sign, value1, value2) + f'{value1 - value2}')

# Функция умножения
def get_mult(sign, value1, value2):
    return str(get_template(sign, value1, value2) + f'{value1 * value2}')

# Функция деления
def get_div(sign, value1, value2):
    return str(get_template(sign, value1, value2) + f'{value1 / value2}')