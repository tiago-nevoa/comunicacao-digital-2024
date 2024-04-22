import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))
from guia_pratico.python.symbol_frequency import *


def first_exercise(content: str) -> list:
    
    probabilities = get_symbol_probabilities(content, as_percentage = True)
    most_frequent_symbols = get_most_frequent_symbols(probabilities, 5)
    return most_frequent_symbols

def second_exercise(content: str) -> list:

    pairs = get_pair_frequencies(content)
    probabilities = get_pair_probabilities(pairs)
    most_frequent_pairs = get_most_frequent_symbols(probabilities, 5)

    return most_frequent_pairs


def get_pair_frequencies(content: str) -> dict:
    pairs = {}

    for line in content.splitlines():
        for i in range(len(line) - 1):

            char = line[i]
            next_char = line[i + 1]

            pair = char + next_char
            pairs[pair] = pairs.get(pair, 0) + 1

    return pairs

def get_pair_probabilities(pairs: dict) -> dict:
    total_pairs = sum(pairs.values())
    for pair, frequency in pairs.items():
        pairs[pair] = frequency / total_pairs * 100
    return pairs


def main():

    files = ["modulo_1/TestFiles/CD/ListaPalavrasEN.txt",
             "modulo_1/TestFiles/CD/ListaPalavrasPT.txt"]
    
    for file in files:
        with open(file, 'r', errors='ignore') as f:
            file_content = f.read()
            file_name = os.path.basename(f.name)

            char_probabilities = first_exercise(file_content)
            pair_probabilities = second_exercise(file_content)

            print(f"{file_name}:")
            print(f"- Most frequent symbols: {char_probabilities}")
            print(f"- Most frequent pairs of symbols: {pair_probabilities}")

    

if __name__ == '__main__':
    main()