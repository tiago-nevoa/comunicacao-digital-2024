import random
from symbol_generator import *

import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))
from guia_pratico.python.symbol_frequency import *

def get_number_probabilities(start, end):

    length = end - start + 1

    probability = 1 / length
    
    return {str(num): probability for num in range(start, end + 1)}

def first_exercise(count):
    pins = []

    numbers = get_number_probabilities(0, 9)

    for i in range(count):
        length = random.randint(4, 6)
        generated_string = symbol_generator(length, numbers)
        pins.append(generated_string)

    return pins

def second_exercise(count):
    keys = []

    numbers = get_number_probabilities(1, 50)
    stars = get_number_probabilities(1, 12)

    for i in range(count):
        generated_numbers = symbol_generator(5, numbers, True)
        generated_stars = symbol_generator(2, stars, True)
        keys.append(f"{generated_numbers} {generated_stars}")

    return keys

def third_exercise(count):
    passwords = []

    chars = '!"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_abcdefghijklmnopqrstuvwxyz{|}~'

    probabilities = get_symbol_probabilities(chars)

    for i in range(count):
        length = random.randint(8, 12)
        generated_string = symbol_generator(length, probabilities)
        passwords.append(generated_string)

    return passwords

def main():

    count = 10

    pins = first_exercise(count)
    print(f"PINs: {pins}")

    keys = second_exercise(count)
    print(f"Keys: {keys}")

    passwords = third_exercise(count)
    print(f"Passwords: {passwords}")


if __name__ == '__main__':
    main()