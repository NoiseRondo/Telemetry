
def index_arr():
    arr = []
    x = 0
    while x != 'end':
        x = input('введите значения или напишите end для остановки:')
        if x == 'end':
            break
        arr.append(x)
        print(x)
        print(arr)
    arr_len = len(arr)
    print(arr_len)
    print(range(arr_len))
    print('Полученный массив', arr)
    ind = 0

    while ind in range(arr_len):
        n = arr[ind]
        if ind+1 == arr_len:
            break
        print(n)
        arr[ind] = arr[ind+1]
        arr[ind+1] = n
        ind += 2
        print('индекс', ind)

    print('обмен соседних элементов', arr)

index_arr()


#my_list = [1, 2, 3, 4, 5, 6]
#def my_type(el):
    #for el in range(len(my_list)):
        #print(type(my_list[el]))
    #return
#my_type(my_list)

