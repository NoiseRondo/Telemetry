def myfunc(n1, n2):
    res = n1 + n2
    return res

res1 = myfunc(2, 3)

print('res 1 = ', res1)



def myfunc2(n):
    res = 1
    for i in n:
        res *= i
    return res

nums = [1, 2, 3 ,4 ,5]
nums2 = [1, 2, 3, 4, 5]

res2 = myfunc2(nums)
print('res2 = ', res2)




user_digits = input('Введите числа, используя пробел').split(' ')
user_list = map(int, user_digits)
print(type(user_digits))
print(type(user_list))

res3 = myfunc2(user_list)
print('res3 = ', res3)

def myfunc3(n1, n2):
    res = 1
    for i in n1:
        res *= i

    for i in n2:
        res *=i
    return res

res4 = myfunc3(nums, n2 = nums)

print('res4 = ', res4)




def myfunc4(n1, n2 = 1):
    res = ' '.join(n1) * n2
    return res

str_nums = map(str, nums)

res5 = myfunc4(str_nums)

print('res5 = ', res5)





myfunc5 = lambda p1, p2 : p1 +p2

print('lambda_func = ', myfunc5(2, 3))




print('abs = ', abs(-10))
print('min = ', min(-10, -18))
print('max = ', max(-10, 10))
print('sum = ', sum([1, 2]))
print('pow = ', pow(16, 1/4))




for i in range(-11, 6, 2):
    print('i_range = ', i)




def myfunc6(n1, n2 = 1):
    """
    Author: Vladimir
    :param n1: число 1
    :param n2: число 2
    :return: возвращает строку n1 раз

    """
    res = ' '.join(n1) * n2
    return res

res6 = myfunc6(4, 2)
print('res6 = ', myfunc6())