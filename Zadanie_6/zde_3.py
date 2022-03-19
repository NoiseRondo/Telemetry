import numpy as np
import sys
import math
import matplotlib.pyplot as plt

inp1 = (input('Введите первое значение: '))
inp2 = (input('Введите второе значение: '))
inp3 = (input('Введите третье значение: '))

try:

    n1 = int(inp1)
    n2 = int(inp2)
    n3 = int(inp3)
except TypeError:
    print(f'{inp1} или {inp2} или {inp3 }Переменная должна быть числом')
    sys.exit()

def urav():
    global a
    a = n1
    global b
    b = n2
    global c
    c = n3
    global x
    try:
        d = b**2 - 4*a*c
        if d < 0:
            print('Корней нет')
            x = 'null'
        elif d == 0:
            x1 = -b/(2 * a)
            print('D = 0')

            x = np.linspace(0, x1, 50)
        elif d > 0:
            print('D > 0')
            x1 = (-b + math.sqrt(d)) / (2 * a)
            print('x1 = ', x1)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            print('x2= ', x2)
            x = np.linspace(x1, x2, 50)

    except ValueError:
        print('Неверные значения')
        sys.exit()

urav()

try:
    y = a*x**2 + b*x + c
    fig, ax = plt.subplots(figsize=(6, 6))

    ax.set_title('Задание 3')
    ax.set_xlabel('x', fontsize=14)
    ax.set_ylabel('y', fontsize=14)

    ax.grid(which='major', linewidth=1.2)
    ax.grid(which='minor', linestyle='--', color='gray')
    plt.plot(x, y, 'b-')

    plt.show()

except TypeError:
    print('Неподходящие значения')



