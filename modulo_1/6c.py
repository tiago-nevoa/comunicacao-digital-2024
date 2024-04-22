from string_binary_conversion import *
binary_symetric_channel = __import__('6a').binary_symetric_channel

def main():

    p = 0.0001

    file = "modulo_1/TestFiles/CD/a.txt"

    with open(file, 'r', errors='ignore') as f:
        file_content = f.read()

    binary_file = text_to_binary(file_content)
    
    masked_binary_file = []

    for sequence in binary_file:
        masked_sequence = binary_symetric_channel(sequence, p)
        masked_binary_file.append(masked_sequence)

    text = binary_to_text(masked_binary_file)

    print(text)


if __name__ == '__main__':
  main()