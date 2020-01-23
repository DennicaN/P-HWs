def fun(*args):
    try:
        a = int(input('Укажите число А'))
        b = int(input('Укажите число B'))
        res = a / b
    except ValueError:
        return 'Value Error'
    except ZeroDivisionError:
        return 'Число не может быть нулевым'
    return res

print(f'Результат:  {fun()}')