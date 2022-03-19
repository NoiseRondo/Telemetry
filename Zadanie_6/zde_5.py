from threading import Thread, Semaphore
import random
from time import sleep

main_arr = []
semph = Semaphore(6)


def spisok(num):


    for n in range(num):
        vnutr_arr = []

        def vnutr_list(limit):
            semph.acquire()
            for i in range(limit):
                x = round(random.uniform(1, 10))
                vnutr_arr.append(x)
                i += 1
                print(i)
                print(vnutr_arr)
                sleep(0.3)
            semph.release()
        #Для одного аргумента используем args = [number], для нескольких args = (number)
        potok1 = Thread(target=vnutr_list, args=[5])
        potok1.start()

        if potok1.is_alive():
            potok1.join()


        main_arr.append(vnutr_arr)
        n += 1
        print(n)
        print(main_arr)
        sleep(0.3)

spisok(5)
