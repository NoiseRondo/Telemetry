arr = [1, 3.14, True, False, "String time"]

arr.append(7)

print(arr[5])
print(len(arr))

print(arr)

arr[0] = 4

print(arr)

arr2 = [1,2,3,4,5]

print(arr[::-1])

arr3 = [1, 2, 3, 4]
arr3.append(1000)
my_tuple = (1, 2, 3, 4)
my_tuple2 = arr3

print(my_tuple)
print(my_tuple2)
print(len(my_tuple2))

my_set = {1, 3, 5, 6, 8}
my_set_2 = set(arr3)
my_set_3 = my_set - my_set_2

print(my_set)
print(my_set_2)
print(my_set_3)

print(hash("my_set_2"))
print(hash("my_set_2"))

my_set.add("my_set")
print(my_set)

my_voc = { 1 : 'value', 'printer' : 3, 'price': 400 }
my_voc['xerox'] = 55
my_voc['printer'] = 200

print(my_voc)
print(my_voc['printer'])

my_voc_2 = {5: 100, 'gruppa': 12}

my_voc.update(my_voc_2)
print(my_voc)
print(my_voc.get(1))