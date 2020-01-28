from itertools import count, cycle

some_list = list(input('Укажите 5 слов для списка через пробел: ').split())
iteration = cycle(some_list) #бесконечная итерация
for num in count():
    if num > 15:
        break
    else:
        print(f"{num} - {next(iteration)}")