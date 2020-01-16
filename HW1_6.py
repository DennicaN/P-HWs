run_1 = int(input('Укажите сколько человек пробежал в первый день '))
run_result = int(input('Укажите сколько пробежал человек в финале '))
days = 1
while run_result >= run_1:
        days = days + 1
        run_1 = run_1 + run_1 / 10
print(f' Бегун достиг цели на: {days} день, Пройдено: {run_1:.1f} км')

