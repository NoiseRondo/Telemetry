
import random
import sys

spisok_1 = [1, 'Иволга', 88.8, 'Based', True, 237, '231', 666, 0]

spisok_2 = []

def spis(sp):
    if sp == []:
        print('None')
        sys.exit()
    print(random.choice(sp))
    sys.exit()

