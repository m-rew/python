import operations

def main():
    selection_operation()

# Функция выводит на экран доступные оперции для пользователя
def display_operations():
    print(f'+ Сложение'
          f'\n- Вычитание'
          f'\n* Умножение'
          f'\n/ Деление')

# Функция выводит доступные операции и предлагает пользователю ввести знак операции и запоминает его
def selection_operation():
    display_operations()
    validation_operation(input('Введите знак операции: '))

# Функция проверят введенный знак операции
def validation_operation(sign):
    if not (sign in ['+', '-', '*', '/']):
        print('Вы ввели несуществующую команду! Попробуйте еще раз\n')
        selection_operation()
    else:
        operations.main(sign, write_values())

# Функция просит ввести числа
def write_values():
    return [int(input('Введите 1ое значение: ')), int(input('Введите 2ое значение: '))]