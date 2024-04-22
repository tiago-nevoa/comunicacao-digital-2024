import math

def text_to_binary(text: str) -> list:

    binary_text = []

    for char in text:
        binary_char = char_to_binary(char)
        binary_text.append(binary_char)
    
    return binary_text


def char_to_binary(char: str) -> str:

    if len(char) != 1:
        raise ValueError('Input must be a char')

    unicode = ord(char)

    return str(bin(unicode)[2:])

def binary_to_text(binary_sequences: list) -> str:
    text = ''

    for binary_sequence in binary_sequences:
        text += binary_to_char(binary_sequence)

    return text

def binary_to_char(binary_sequence: str) -> str:

    binary_sequence = int(binary_sequence)
    
    unicode = binary_to_unicode(binary_sequence)

    char = chr(unicode)

    return char

def binary_to_unicode(binary_sequence: int) -> int:
    unicode = 0
    if binary_sequence:
        length = int(math.log10(binary_sequence)) + 1
    else:
        length = 0
    for i in range(length):
        b = ((binary_sequence % 10) * (2 ** i))   
        binary_sequence //= 10
        unicode += b
    return unicode