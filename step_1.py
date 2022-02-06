# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
# duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
seconds_in_minute = 60
seconds_in_hour = 60 * seconds_in_minute
seconds_in_day = 24 * seconds_in_hour

duration = int(input('duration = '))

days = 0
hours = 0
minutes = 0
seconds = 0
result = ''

if seconds_in_day < duration:
    days = int(duration / seconds_in_day)
    duration = duration - seconds_in_day * days
    result += str(days) + ' дн '

if seconds_in_hour < duration:
    hours = int(duration / seconds_in_hour)
    duration = duration - seconds_in_hour * hours
    result += str(hours) + ' час '

if seconds_in_minute < duration:
    minutes = int(duration / seconds_in_minute)
    duration = duration - seconds_in_minute * minutes
    result += str(minutes) + ' мин '

if duration > 0:
    result += str(duration) + ' сек '

print(result)

