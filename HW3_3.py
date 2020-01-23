def my_func(per_1, per_2, per_3):
    fun_list = [per_1, per_2, per_3]
    maximum = [] #max_1
    max_1 = max(fun_list)
    maximum.append(max_1)
    fun_list.remove(max_1)
    max_2 = max(fun_list)
    maximum.append(max_2)
    print('Сумма двух максимальных числер равна: ', sum(maximum))

my_func(per_1=int(input('Укажите первое число - ')), per_2=int(input('Укажите второе число - ')), per_3= int(input('Укажите второе число - ')))

#    if per_1 >= per_3 and per_2 >= per_3:
#        return per_1,  per_2
#    elif per_1 > per_2 and per_1 < per_3:
#        return per_1, per_3
#    else:
#        return per_2, per_3

#print(my_func(per_1=input('Укажите перменную 1: '), per_2=input('Укажите перменную 2: '), per_3=input('Укажите перменную 3:')))
