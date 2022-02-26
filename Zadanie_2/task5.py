
my_list = [7, 5, 3, 3, 2]
print(f"Изначальный рейтинг: {my_list}")
num = int(input('Введите значения или напишите 0 для остановки:'))
end = 0
while num != 0:
    for x in range(len(my_list)):
        if my_list[x] == num:
            my_list.insert(x + 1, num)
            break
        elif my_list[0] < num:
            my_list.insert(0, num)
        elif my_list[-1] > num:
            my_list.append(num)
        elif my_list[x] > num and my_list[x + 1] < num:
            my_list.insert(x + 1, num)
    print(f"Рейтинг - {my_list}")
    num = int(input("Введите значение или напишите 0 для остановки "))