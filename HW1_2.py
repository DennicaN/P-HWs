time_sec = int(input('Укажите, пожалуйста время в секундах '))
hours = time_sec // 3600
minutes_all = time_sec % 3600
minutes = minutes_all // 60
seconds = minutes_all % 60

print(f'При конвертации времени получилось: {hours} часов : {minutes} минут : {seconds} секунд')