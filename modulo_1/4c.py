import random
from symbol_generator import *
password_generator = __import__('4b').third_exercise

import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))
from guia_pratico.python.symbol_frequency import *


def get_file_size(filepath) -> float:
    statinfo = os.stat(filepath)
    size = statinfo.st_size
    return size / 1024 # Return in KB

def main():

    filepath = "modulo_1/TestFiles/Generated/passwords.txt"
    count = 1000

    passwords = password_generator(count)

    with open(filepath, 'w') as file:
        for password in passwords:
            file.write(str(password) + "\n")

    compressed_filepath = "modulo_1/TestFiles/Generated/passwords.zip"


    original_size = get_file_size(filepath)
    compressed_size = get_file_size(compressed_filepath)

    print(f"{original_size} KB -> {compressed_size} KB")

    compression_ratio = (original_size - compressed_size) / original_size * 100

    print(f"Compression Ratio: {compression_ratio}%")


if __name__ == '__main__':
    main()