number = int(input('Введите пожалуйста многозначное, положительное число '))
max_num = number % 10
number = number // 10
while number > 0:
    if number % 10 > max_num:
        max_num = number % 10
    number = number // 10
print(f'Максимальная цифра в указанном вами числе: {max_num}')