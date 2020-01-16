profit = int(input('Укажите прибыль компании'))
costs = int(input('Укажите издержки компании'))
netprofit = profit - costs
if profit > costs:
    print(f'Фирма рентабельна потому что ее прибыль больше расходов')
    rent = netprofit / profit * 100
    print(f'Рентабельность компании составляет {rent:.2f} %')
    peoples = int(input('Укажите пожалуйста число работников компании, чтобы определить прибыль фирмы в расчете не одного работника '))
    per_unit = netprofit // peoples
    print(f'Прибыль фирмы в расчете не одного сотрудника составляет: {per_unit}')
if profit < costs:
    print(f'Ваша компания работает в убыток')