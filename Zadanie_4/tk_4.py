rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
zapis = []
with open('nums.txt', 'r') as file_i:

    for i in file_i:
        i = i.split(' ', 1)
        zapis.append(rus[i[0]] + '  ' + i[1])
    print(zapis)

with open('nums_new.txt', 'w') as file_z:
    file_z.writelines(zapis)