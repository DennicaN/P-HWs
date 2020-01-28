from random import randint

def random_list(new):
    result = [randint(1, 44) for el in range(new)]
    return result
rand_num = random_list(14)
print(rand_num)
new_list = []
for el in range(14):
    t = True
    for i in range(14):
        if rand_num[el] == rand_num[i] and el != i:
            t = False
            break
    if t == True:
        new_list.append(rand_num[el])

print(new_list)