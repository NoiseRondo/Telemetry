
import random
from Zadanie_5 import mod_spis
from mod_spis import spis

spisok_1 = [1, 'Иволга', 88.8, 'Based', True, 237, '231', 666, 0]

spisok_2 = []

inp = int(input('Введите номер списка: '))

if inp == 1:
    mod_spis.spis(spisok_1)
elif inp == 2:
    mod_spis.spis(spisok_2)


