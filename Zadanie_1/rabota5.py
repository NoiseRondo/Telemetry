net_gain = int(input('Количество выручки: '))
net_lose = int(input("Количество издержек: "))
sotrud = int(input("Количество сотрудников: "))

profit = net_gain - net_lose
rent = profit / net_gain
zarp = profit / sotrud

if profit > 0:
    print("Прибыль составила: ", profit)
    print("Рентабельность выручки: ", rent)
else:
    if profit == 0:
        print("Вышли в ноль")
    else:
        print("Убыток составил: ", profit)

print("Прибыль на сотрудника: ", zarp)

