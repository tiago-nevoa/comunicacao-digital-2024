import math

# Import type 1
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))
from guia_pratico.python.symbol_frequency import get_symbol_probabilities

# Import type 2
#from ..guia_pratico.python.symbol_frequency import symb_frequencies, prob_symb_freq


def informational_value(symbol: str, probabilities: dict) -> float:

    if symbol not in probabilities:
        raise ValueError(f"Symbol '{symbol}' not found in the list")

    probability = probabilities[symbol]

    return -math.log2(probability)

def entropy(probabilities: dict) -> float:

    entropy = 0

    for symbol, probability in probabilities.items():
        entropy += informational_value(symbol, probabilities) * probability
    return entropy


def main():

    files = ["guia_pratico/TestFiles/something.txt",
            "modulo_1/TestFiles/CD/a.txt",
            "modulo_1/TestFiles/CD/alice29.txt",
            "modulo_1/TestFiles/CD/arrays.kt",
            "modulo_1/TestFiles/CD/barries.jpg"]
    
    for file in files:
        with open(file, 'r', errors='ignore') as f:
            file_content = f.read()
            probabilities = get_symbol_probabilities(file_content)
            file_entropy = entropy(probabilities)
            print(file_entropy)
    

if __name__ == '__main__':
    main()