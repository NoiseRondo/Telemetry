import os

#dirs = ['dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5', 'dir_6', 'dir_7', 'dir_8', 'dir_9']

parent_dir = 'F:/Diplom/Telemetry/Zadanie_5'
def direc(dir):
    command = input('Введите команду: ')
    if command == "С":
        for i in range(dir):
            path = os.path.join(parent_dir, 'dir_' + str(i))
            os.mkdir(path)
            print("Directory '% s' created" % i)

    elif command == "У":
        for i in range(dir):
            path = os.path.join(parent_dir, 'dir_' + str(i))
            print(path)
            if os.path.exists(path):
                os.rmdir(path)
                print("Directory '% s' deleted" % i)
    elif command == "СУ":
        for i in range(dir):
            path = os.path.join(parent_dir, 'dir_' + str(i))
            os.mkdir(path)
            print("Directory '% s' created" % i)
        for i in range(dir):
            path = os.path.join(parent_dir, 'dir_' + str(i))
            print(path)
            if os.path.exists(path):
                os.rmdir(path)
                print("Directory '% s' deleted" % i)

direc(10)