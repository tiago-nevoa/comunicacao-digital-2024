import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))
from guia_pratico.python.symbol_frequency import *


def firstExercise(content):

    if not isinstance(content, str):
        raise ValueError('Parameter has to be a string')
    
    probabilities = get_symbol_probabilities(content, True)

    most_frequent_chars = most_probable_symbols(probabilities, 5)

    return most_frequent_chars

def secondExercise(content):

    if not isinstance(content, str):
        raise ValueError('Parameter has to be a string')
    
    pairs = {}

    for line in content.splitlines():
        for i in range(len(line) - 1):
            pair = line[i] + line[i + 1]
            pairs[pair] = pairs.get(pair, 0) + 1

    # Calcular a percentagem de frequência
    total_pairs = sum(pairs.values())
    for pair, frequency in pairs.items():
        pairs[pair] = round(frequency / total_pairs * 100, 2)

    most_frequent_pairs = most_probable_symbols(pairs, 5)

    return most_frequent_pairs


def main():

    files = ["modulo_1/TestFiles/CD/ListaPalavrasEN.txt",
             "modulo_1/TestFiles/CD/ListaPalavrasPT.txt"]
    
    for file in files:
        with open(file, 'r', errors='ignore') as f:
            file_content = f.read()
            charProbabilities = firstExercise(file_content)
            #print(charProbabilities)
            pairProbabilities = secondExercise(file_content)
            print(pairProbabilities)
            #print(entropy(probabilities))
    

if __name__ == '__main__':
    main()