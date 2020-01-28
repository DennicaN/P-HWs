from random import randint
start_list = [randint(1, 300) for el in range(20)]
print(start_list)
end_list = []

for el in range(1, len(start_list)):
    if start_list[el] > start_list[el - 1]:
        end_list.append(start_list[el])

print(end_list)