# Exercise E
def file_symb_freq(file, filter):
    with open(file, 'r', errors='ignore') as f:
        file_content = f.read()
        total_chars = len(file_content)
        
    frequencies = symb_frequencies(file_content)
    filtered_frequencies = filter_symb_freq(frequencies, total_chars, filter)
    sorted_frequencies = sort_symb_freq(filtered_frequencies)

    return sorted_frequencies
    

def symb_frequencies(content):
    
    if not isinstance(content, str):
        raise ValueError('Parameter has to be a string')

    frequencies = {}

    for char in content:
        frequencies[char] = frequencies.get(char, 0) + 1
    
    return frequencies


def filter_symb_freq(frequencies, total_chars, filter):
    return {key: value for key, value in frequencies.items() if value/total_chars*100 >= filter}

def prob_symb_freq(frequencies, total_chars):
    return {key: value / total_chars * 100 for key, value in frequencies.items()}

def sort_symb_freq(frequencies):
    return dict(sorted(frequencies.items(), key=lambda item: item[0]))