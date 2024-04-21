from information_theory import *

import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))
from guia_pratico.python.symbol_frequency import get_symbol_probabilities

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
            file_entropy = get_entropy(probabilities)
            print(file_entropy)
    

if __name__ == '__main__':
    main()