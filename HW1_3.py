num = int(input('Укажите цельночисловое значение '))
num_2 = num * 10 + num
num_3 = num * 100 + num * 10 + num
answer = num + (num * 10 + num) + (num * 100 + num * 10 + num)
print(f'Вы указали число:  {num}. Считаем {num} + {num_2} + {num_3} = {answer}')