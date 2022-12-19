from datetime import datetime

# Функция записывает полученные данные в файл
def write_log(data):
    time = datetime.now().strftime('%D:%H:%M')
    with open('log.txt', 'a') as file:
        file.write(f'{time}: {data}\n')