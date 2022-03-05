def array_diff(a, b):
    for i in a:
        for x in b:
            if i == x:
                print('match')
                a.remove(x)

    print(a)
array_diff([1,2,2,2], [2])