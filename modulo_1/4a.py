from symbol_generator import *
import information_theory

import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))
from guia_pratico.python.symbol_frequency import *


def main():
    initial_probabilities = {'O': 0.12, 'h': 0.31, 'b': 0.04, 'Q': 0.53}
    
    generated_string = symbol_generator(30, initial_probabilities)

    new_probabilities = get_symbol_probabilities(generated_string)

    initial_entropy = information_theory.get_entropy(initial_probabilities)
    new_entropy = information_theory.get_entropy(new_probabilities)
    diff = new_entropy - initial_entropy

    print(f"Entropy: {initial_entropy} -> {new_entropy}")
    print(f"Diference of {diff}")


if __name__ == '__main__':
    main()