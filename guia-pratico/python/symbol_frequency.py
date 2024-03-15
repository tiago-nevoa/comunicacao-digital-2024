# Exercise E
import os

def symb_frequencies(content):
    frequencies = {}
    for char in content:
        frequencies[char] = frequencies.get(char, 0) + 1
    sorted_frequencies = dict(sorted(frequencies.items(), key=lambda item: item[0]))
    return sorted_frequencies

def symb_freq_filter(file, filter):

    with open(file, 'r', errors='ignore') as f:
        content = f.read()
        total_chars = len(content)

    frequencies = symb_frequencies(content)
    filter_frequency = {key: value for key, value in frequencies.items() if value/total_chars*100 > filter}

    return filter_frequency