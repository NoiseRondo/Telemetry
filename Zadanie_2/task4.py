my_str = str(input("Введите несколько слов: "))
spl = my_str.split()
print(spl)

num = 1
for ind in spl:
    print(num, ind[:10])
    num += 1