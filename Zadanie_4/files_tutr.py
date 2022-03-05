# file_text = open('myfile.txt', 'w')
# file_text.writelines('This is the first string in my fyle\n')
# file_text.writelines('This is the second string in my fyle')


#with open('myfile.txt', 'r') as file:
#    data = file.readlines()
#    print(f'stroka 1 = {data[0]}')
#    print(f'stroka 2 = {data[1]}')
#    print(f'stroka 2 = {data[2]}')

# with open('myfile.txt', 'w') as file:
#    massive = ['This is the first string in my fyle\n', 'This is the second string in my fyle\n', 'hello world']
#    file.writelines(massive)


# try:
#    file = open('myfile2.txt') as file
#    for line in file:
#        print(line)

# except IOError:
#   print('Такого файла не существует')

# finally:
#    file.close


import os

os.rename('F:/Diplom/Telemetry/Zadanie_4/test2.txt', 'F:/Diplom/Telemetry/Zadanie_4/myfile_test.txt')
result = os.listdir('F:/Diplom/Telemetry/Zadanie_4')
print(result)

with open('myfile.txt', 'r') as file:
    data = file.read()
    print(file.tell())
    print(file.seek(8))
    data = file.read()

    print(f'content = {data}')