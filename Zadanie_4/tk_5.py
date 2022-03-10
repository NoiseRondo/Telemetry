numbers = "21.2 55 1 112.7 555 0 7.1 0 11.7"

sum= 0

try:
    with open('chisla.txt', 'w') as file_w:
        file_w.write(numbers)

    with open('chisla.txt', 'r') as file_r:
        data = file_r.read()

    for x in data.split():
        sum += float(x)
except IOError as e:
    print(e)
except ValueError:
    print("Неконсистентные данные")

print('Сумма чисел: ', sum)
