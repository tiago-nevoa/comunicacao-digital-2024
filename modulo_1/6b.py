import random
binary_symetric_channel = __import__('6a').binary_symetric_channel


def get_errors(original: str, masked: str) -> int:
    errors = 0
    for i in range(len(original)):
            if original[i] != masked[i]:
                errors += 1
    return errors


def main():

    lengths = [1024, 10240, 102400, 1024000, 10240000]
     
    p = 0.60

    for length in lengths:
        sequence = ''
        for i in range(length):
            sequence += str(random.randint(0, 1))
        masked_sequence = binary_symetric_channel(sequence, p)

        errors = get_errors(sequence, masked_sequence)

        ber = errors / len(sequence)
        ratio = (p - ber) / p * 100
        print(f"Ratio for {length} bits: {ratio}% ({p} -> {ber})")





if __name__ == '__main__':
    main()