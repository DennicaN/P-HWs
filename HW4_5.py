from functools import reduce

items = [el for el in range(100, 1000) if el % 2 == 0]

my_list = reduce(lambda x, y: x * y, items)

print(my_list)