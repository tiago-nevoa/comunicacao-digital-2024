# Exercise E
def symb_frequencies(content):
    
    if not isinstance(content, str):
        raise ValueError('Parameter has to be a string')

    frequencies = {}

    for char in content:
        frequencies[char] = frequencies.get(char, 0) + 1
        
    sorted_frequencies = dict(sorted(frequencies.items(), key=lambda item: item[0]))
    
    return sorted_frequencies

def symb_freq_filter(file, filter):

    with open(file, 'r', errors='ignore') as f:
        file_content = f.read()
        
    total_chars = len(file_content)
    frequencies = symb_frequencies(file_content)

    filter_frequencies = {key: value for key, value in frequencies.items() if value/total_chars*100 >= filter}

    return filter_frequencies