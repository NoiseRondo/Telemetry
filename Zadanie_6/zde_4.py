import threading
from time import sleep

# функция вызова потока
def mysum():
    # Глобальная переменная
    global num
    # добавка к сумме
    k = 1

    # вывод значений
    txt = str(num)
    while myevent.is_set():
        kor = k*k
        num += k*k
        txt += " + " + str(kor)
        # выводим текущее значение суммы:
        print(f'["{kor}"], {txt} = {num}')
        # следующая итерация
        k += 1
        # пауза потока :
        sleep(0.3)
print('Сумма целых чисел')
# Создание дочернего потока :
t = threading.Thread(target=mysum)
# начальное значение суммы
num=0
# Объект синхронизации потоков:
myevent = threading.Event()
# Установка флага :
myevent.set()
# запуск дочернего потока на выполнение :
t.start()
# Пауза в выполнении главного потока :
sleep(2)
# Отмена флага
myevent.clear()
# ожидание и завершение дочерних потоков :
if t.is_alive():
    t.join()

print(f'Результат: {num}')




