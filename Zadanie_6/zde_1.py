def summa(n1, n2, n3):
    result = 0
    try:
        result = n1 + n2 + n3
    except TypeError:
        result = f'{n1} или {n2} Переменная должна быть числом'
    except IOError:
        print('Неверные значения')
    return result


print(summa(1, 1, 5))