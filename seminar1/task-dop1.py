# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

# Примеры:
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек

duration = int(input('Введите кол-во секунд: '))

if duration >= 86400:
    # Кол-во дней
    day_str = str(duration / 86400)
    day = int(day_str[:day_str.find('.')])

    # Кол-во часов
    hour_str = str((duration - 86400 * day) / 3600)
    hour = int(hour_str[:hour_str.find('.')])

    # Кол-во минут
    minute_str = str((duration - 86400 * day - 3600 * hour) / 60)
    minute = int(minute_str[:minute_str.find('.')])

    # Кол-во секунд
    second = duration - 86400 * day - 3600 * hour - 60 * minute

    print(f'{day} дн. {hour} час. {minute} мин. {second} сек.')
elif duration >= 3600:
    # Кол-во часов
    hour_str = str(duration / 3600)
    hour = int(hour_str[:hour_str.find('.')])

    # Кол-во минут
    minute_str = str((duration - 3600 * hour) / 60)
    minute = int(minute_str[:minute_str.find('.')])

    # Кол-во секунд
    second = duration - 3600 * hour - 60 * minute

    print(f'{hour} час. {minute} мин. {second} сек.')
elif duration >= 60:
    # Кол-во минут
    minute_str = str(duration / 60)
    minute = int(minute_str[:minute_str.find('.')])

    # Кол-во секунд
    second = duration - 60 * minute

    print(f'{minute} мин. {second} сек.')
else:
    print(f'{duration} сек.')