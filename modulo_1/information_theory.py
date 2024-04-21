import math


def get_informational_value(symbol: str, probabilities: dict) -> float:

    if symbol not in probabilities:
        raise ValueError(f"Symbol '{symbol}' not found in the list")

    probability = probabilities[symbol]

    return -math.log2(probability)

def get_entropy(probabilities: dict) -> float:

    entropy = 0

    for symbol, probability in probabilities.items():
        entropy += get_informational_value(symbol, probabilities) * probability
    return entropy