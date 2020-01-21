my_list = [7, 5, 3, 3, 2]
print(f'Текущий набор натуральных чисел:  {my_list}' )
num = int(input('Укажите пожалуйста какое число в рейтинг вы хотели бы добавить'))

for el in range(len(my_list)):
    if my_list[el] == num:
        my_list.insert(el + 1, num)
        break
    elif my_list[0] < num:
        my_list.insert(0, num)
        break
    elif my_list[-1] < num:
        my_list.append(num)
        break
    elif my_list[el] > num and my_list[el + 1] < num:
        my_list.insert(el + 1, num)
        break
print(f'Итоговый рейтинг: {my_list}')
