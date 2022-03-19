def dannie():
    first_n = input('Введите имя: ')
    last_n = input('Введите фамилию: ')
    birth = input('Введите год рождения: ')
    city = input('Введите город проживания: ')
    email = input('Введите email адрес: ')
    telef = input('Введите номер телефона: ')

    def vivod(n, f, b, c, e, t):
        print(n, f, b, c, e, t)

    vivod(n=first_n, f=last_n, b=birth, c=city, e=email, t=telef)

dannie()





