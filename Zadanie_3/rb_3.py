def slozh():
    n1 = int(input('Введите первый аргумент: '))
    n2 = int(input('Введите второй аргумент: '))
    n3 = int(input('Введите третий аргумент: '))
    min_arg = min(n1, n2, n3)
    print('Наименьший аргумент', min_arg)
    arg_arr = [n1, n2, n3]
    arg_arr.remove(min_arg)
    res = arg_arr[0] + arg_arr[1]
    print('Результат сложения двух наибольших аргументов = ', res)


slozh()