def stroka():
    i = 1
    while i != '*':
        user_digits = input('Введите строки, используя пробел: ').split(' ')
        if "*" in user_digits:
            user_digits.remove('*')
            user_list = map(str, user_digits)
            s = ' '.join(user_list)
            res = s.title()
            print('Полученная строка', res)
            break
        user_list = map(str, user_digits)
        s = ' '.join(user_list)
        res = s.title()
        print('Полученная строка', res)

stroka()
