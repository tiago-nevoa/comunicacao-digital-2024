import math

# Import type 1
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))
from guia_pratico.python.symbol_frequency import symb_frequencies, prob_symb_freq

# Import type 2
#from ..guia_pratico.python.symbol_frequency import symb_frequencies, prob_symb_freq


def informational_value(symbol, probabilities):

    probability = probabilities[symbol]

    return -math.log2(probability)

def entropy(probabilities):

    entropy = 0

    for symbol, probability in probabilities.items():
        entropy += informational_value(symbol, probabilities) * probability
    return entropy


def get_probabilitites(file):
    with open(file, 'r', errors='ignore') as f:
        file_content = f.read()
        total_chars = len(file_content)
        
    frequencies = symb_frequencies(file_content)
    probabilities = prob_symb_freq(frequencies, total_chars)

    return probabilities


file1 = "guia_pratico/TestFiles/something.txt"
file2 = "modulo_1/TestFiles/CD/a.txt"
file3 = "modulo_1/TestFiles/CD/alice29.txt"
file4 = "modulo_1/TestFiles/CD/arrays.kt"
file5 = "modulo_1/TestFiles/CD/barries.jpg"

probabilities = get_probabilitites(file1)

print(get_probabilitites(file5))


print(entropy(probabilities))
print(entropy(get_probabilitites(file2)))
print(entropy(get_probabilitites(file3)))
print(entropy(get_probabilitites(file4)))
print(entropy(get_probabilitites(file5)))