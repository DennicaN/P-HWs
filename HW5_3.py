with open('Task3.txt','r') as task3:
    not_grate = []
    terrible = []
    start_list = task3.read().split('\n')
    for el in start_list:
        el = el.split()
        if float(el[1]) > 20000:
            not_grate.append(el[1])
        else:
            terrible.append(el)

print(f'Оклад менее 20к имеют: {terrible}')
print(f'Средний оклад на сотрудника c зарплатой выше 20 тыр: {sum(map(float, not_grate)) / len(not_grate)}')