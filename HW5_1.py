with open('Task1.txt', 'w') as task1:
    line = input("Введите строку\n")
    while line:
        task1.writelines(line + '\n')
        line = input("Введите строку \n")
        if not line:
            break

with open('Task1.txt', 'r') as task1:
    content = task1.readlines()
    print(content)