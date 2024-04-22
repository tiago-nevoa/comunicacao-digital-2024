from information_theory import *
import cv2
import numpy as np

import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))
from guia_pratico.python.symbol_frequency import get_symbol_probabilities


def main():
    
    image_types = ['png', 'jpg', 'jpeg', 'tif']

    directory = "modulo_1/TestFiles/CD/"

    for filename in os.listdir(directory):

        file = os.path.join(directory, filename)

        # Images
        if file[-3:] in image_types:
            image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
            hist, _ = np.histogram(image.ravel(), bins = 256, range = (0, 256))
            probabilities = hist / (image.size)
            probabilities[probabilities == 0] = 1e-9    # Handle log of zero
            file_entropy = -np.sum(probabilities * np.log2(probabilities))

        # Text
        else:
            with open(file, 'r', errors='ignore') as f:
                file_content = f.read()
                probabilities = get_symbol_probabilities(file_content)
                file_entropy = get_entropy(probabilities)
        
        print(f"{filename}: {file_entropy}")

    '''
    with open(file, 'r', errors='ignore') as f:
                file_content = f.read()
                print(file_content)
                probabilities = get_symbol_probabilities(file_content)
                file_entropy = get_entropy(probabilities)
                print(file_entropy)
    '''
    

if __name__ == '__main__':
    main()