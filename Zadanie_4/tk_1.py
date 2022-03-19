
sum = ''
while True:
    inp = input('Введите строку: ')
    sum = sum + '\n' + inp
    print(sum)
    if not inp:
        break

    try:
        with open('myfile.txt', 'w') as file:
            file.write(f'{sum}\n')
    except IOError as e:
        print(e)
        break
