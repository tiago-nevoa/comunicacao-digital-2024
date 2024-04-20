# Exercise E
def file_symb_freq(file, filter) -> dict:
    with open(file, 'r', errors='ignore') as f:
        file_content = f.read()
        total_chars = len(file_content)
        
    frequencies = get_symbol_frequencies(file_content)
    filtered_frequencies = filter_frequencies(frequencies, total_chars, filter)
    sorted_frequencies = sort_frequencies(filtered_frequencies)

    return sorted_frequencies
    

## Frequencies

# Get frequencies
def get_symbol_frequencies(content: str) -> dict:
    
    if not isinstance(content, str):
        raise ValueError('Parameter has to be a string')

    frequencies = {}

    for char in content:
        frequencies[char] = frequencies.get(char, 0) + 1
    
    return frequencies

# Filter by threshold in percentage
def filter_frequencies(frequencies: dict, total_chars: int, threshold: int) -> dict:
    return {key: value for key, value in frequencies.items() if value / total_chars * 100 >= threshold}

# Sort by alphabetical order
def sort_frequencies(frequencies: dict) -> dict:
    return dict(sorted(frequencies.items(), key=lambda item: item[0]))


## Probabilities

# Get probabilitites
def get_symbol_probabilities(content: str, as_percentage = False) -> dict:

    if not isinstance(content, str):
        raise ValueError('Parameter has to be a string')

    total_chars = len(content)

    # Alternate between percentage and decimal
    percantage = 100 if as_percentage else 1

    frequencies = get_symbol_frequencies(content)
    probabilities = {key: value / total_chars * percantage for key, value in frequencies.items()}

    return probabilities

# Get the most probable symbols
def most_probable_symbols(probabilities: dict, num_symbols: int) -> list:
  sorted_probabilities = sort_probabilities(probabilities)
  return list(sorted_probabilities.keys())[:num_symbols]

# Sort by most probable
def sort_probabilities(probabilities: dict) -> dict:
    return dict(sorted(probabilities.items(), key=lambda item: item[1], reverse=True))