with open('task5.txt', 'w') as task5:
    items = input('Введите пожалуйста цифры через пробел: ').split(',')
    task5.writelines(items)
with open('task5.txt', 'r') as task_r:
    summ = task_r.read().split()
    print(sum(map(int, summ)))