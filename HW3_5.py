def calc():

    fin_res = 0
    e = True
    while e == True:
        num = input('Укажите цифы через пробел. Чтобы выйте из цикла введите "E"').split()
        res = 0
        for el in range(len(num)):
            if num[el] == "e" or num[el] == "E":
                e = True
                break
            else:
                res = res + int(num[el])
        fin_res = fin_res + res
        print(f'Текущий результат это {fin_res}')
    print(f'Ваш финальный результат это {fin_res}')

calc()