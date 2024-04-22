import random

def binary_symetric_channel(binary_sequence: str, p: float) -> str:

    masked_sequence = ''

    for bit in binary_sequence:
        random_probability = random.random()

        if random_probability < p:
            masked_sequence += "1" if bit == "0" else "0"
        else:
            masked_sequence += bit

    return masked_sequence

def main():
    binary_sequence = "0110010110010"
    p = 0.1
    
    new_binary_sequence = binary_symetric_channel(binary_sequence, p)
    print(f"{binary_sequence} -> {new_binary_sequence}")


if __name__ == '__main__':
    main()