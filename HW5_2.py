with open('Task1.txt', 'r') as task2:
    content = task2.read()
    print(f'Документ содержит: \n{content}')
    task2.seek(0)
    content = task2.readlines()
    print(f'Количество строк в документе: {len(content)}')
    task2.seek(0)
    line = 1
    while content:
        content = task2.readline().split()
        print(f'{line} строка содержит: {len(content)} слов')
        line = line + 1
        if not content:
            break
#    content = task2.readline().split()
#    print(content)

    task2.seek(0)
    content = task2.read().split()
    print(f'Документ содержит: {len(content)} слов')