goods = int(input('Укажите количество товара'))
number = 0
my_list = []
my_dict = []
my_analytics = {}
while number < goods:
    my_dict = dict({'Название' : input('Укажите название'), 'Цена' : input('Укажите цену'), 'Количество' : input('Укажите количество'), 'Еденицы' : input('Укажите еденицу измерения')})
    my_list.append((number, my_dict))
    number += 1
    my_analytics = dict({'Название' : my_dict.get('Название'), 'Цена' : my_dict.get('Цена'), 'Количество' : my_dict.get('Количество'), 'Еденицы' : my_dict.get('Еденицы')})

print(my_list)
#print(my_analytics)