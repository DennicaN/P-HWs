user_string = input('Введите несколько слов в строку, разделив их пробелами')
words = []
num = 1
for el in range(user_string.count(" ") + 1):
    words = user_string.split()
    if len(str(words)) <= 10:
        print(f'{num}, {words [el]}')
        num = num + 1
    else:
        print(f'{num}, {words [el] [:10]}')
        num = num + 1
