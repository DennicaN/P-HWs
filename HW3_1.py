def fun(*args):
    try:
        a = int(input('Set A number'))
        b = int(input('Set B number'))
        res = a / b
    except ValueError:
        return 'Value Error'
    except ZeroDivisionError:
        return 'Число не может быть нулевым'
    return res

print(f'result {fun()}')