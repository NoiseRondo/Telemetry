num = int(input('Введите целое положительное число: '))
num_arr = []

while num > 10:
    x = num_arr.append(num % 10)
    print(num % 10)
    num //= 10

max_num = max(num_arr)
print(max_num)