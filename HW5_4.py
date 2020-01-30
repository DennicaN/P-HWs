rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_list = []
with open('Task4.txt', 'r') as task4:
    for el in task4:
        el = el.split(" ", 1)
        new_list.append(rus[el[0]] + " " + el[1])
    print(new_list)

with open('Task4.txt', 'w') as task_n_w:
    task_n_w.writelines(new_list)
