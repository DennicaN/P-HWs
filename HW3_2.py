def info(f_name, s_name, b_date, c_city, email, phone):
    return ' '.join([f_name, s_name, b_date, c_city, email, phone])

print(info(f_name=input('Укажите ваше имя: '), s_name=input('Укажите вашу фамилию: '), b_date=input('Укажите дату вашего рождения: '), c_city=input('Город проживания :'), email=input('Ваш эллектронный ящик: '), phone=input('Укажите ваш номер телефона: ')))

#       f_name = input('Укажите имя')
#       s_name = input('Укажите фамилию')
#       b_date = input('Укажите дату рождения')
#       c_city = input('Укажите город проживания')
#       email = input('Укажите адресс электронной почты')
#       phone = input('Укажите Номер телефона')
#   return ' '.join(f_name, s_name, b_date, c_city, email, phone)
#
