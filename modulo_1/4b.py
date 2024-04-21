import random
from symbol_generator import *

import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))
from guia_pratico.python.symbol_frequency import *


def main():
    numbers = {'0': 0.1, '1': 0.1, '2': 0.1, '3': 0.1, '4': 0.1, '5': 0.1, '6': 0.1, '7': 0.1, '8': 0.1, '9': 0.1}

    for i in range(10):
        length = random.randint(4, 6)
        generated_string = symbol_generator(length, numbers)
        print(generated_string)




if __name__ == '__main__':
    main()