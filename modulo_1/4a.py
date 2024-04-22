from symbol_generator import *
from information_theory import *
from difference_ratio import *

import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))
from guia_pratico.python.symbol_frequency import *


def main():

    initial_probabilities = {'1': 0.50, '2': 0.30, '3': 0.14, '4': 0.06}
    lengths = [5, 50, 500, 5000]

    for length in lengths:

        generated_string = symbol_generator(length, initial_probabilities)
        new_probabilities = get_symbol_probabilities(generated_string)

        initial_entropy = get_entropy(initial_probabilities)
        new_entropy = get_entropy(new_probabilities)

        ratio = difference_ratio(initial_entropy, new_entropy)

        print(f"Length: {length} -> Ratio: {ratio}")


if __name__ == '__main__':
    main()