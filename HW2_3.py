season_list = ['Зима', 'Весна', 'Лето', 'Осень']
season_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'осень'}
mouth = int(input('Пожалуйста, укажите месяц'))

if mouth == 1 or mouth == 2 or mouth == 3:
    print(season_list[0])
    print(season_dict.get(1))
elif mouth == 4 or mouth == 5 or mouth == 6:
    print(season_list[1])
    print(season_dict.get(2))
elif mouth == 7 or mouth == 8 or mouth == 9:
    print(season_list[2])
    print(season_dict.get(3))
elif mouth == 10 or mouth == 11 or mouth == 12:
    print(season_list[3])
    print(season_dict.get(4))
else:
    print('Месяца: ', mouth, 'не существует')