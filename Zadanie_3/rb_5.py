def stroka():
    i = 1
    res = 0
    while i != '*':
        user_digits = input('Введите числа, используя пробел: ').split(' ')
        if "*" in user_digits:
            user_digits.remove('*')
            user_list = map(int, user_digits)
            s = (sum(user_list))
            res += s
            print('Прибавляемые значения', user_digits)
            print('Финальный результат', res)
            break
        user_list = map(int, user_digits)
        s = (sum(user_list))
        res += s
        print('Прибавляемые значения', user_digits)
        print('Общий результат', res)

stroka()

