day_a = int(input("Результат км дня a: "))
km_res = int(input("Результат км на день b:"))

x=0+day_a
x_rost = 0+day_a
day_b = 0

while x_rost <= km_res:
    x = x + x*(1/10)
    x_rost = x_rost + x
    day_b += 1
    print("Показатель увеличения: ", x)
    print("Показатель пробега: ", x_rost)
    print("День пробега: ", day_b)

print("Дней для преодоления b км: ", day_b)
