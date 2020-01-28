from math import factorial


def gen():
    for i in range(1, 16):
        yield factorial(i)


for el in gen():
    print(el)