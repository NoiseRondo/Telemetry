import random

def delenie():
    n1 = int(input('Введите значение первой переменной: '))
    n2 = int(input('Введите значение второй переменной'))
    rnd = int(random.uniform(n1, n2))
    if rnd == 0:
        print('Деление на ноль невозможно')
    if rnd !=0:
        res1 = n1 / rnd
        print('n1 / rnd = ', res1)
        res2 = n2 / rnd
        print('n2 / rnd = ', res2)

delenie()