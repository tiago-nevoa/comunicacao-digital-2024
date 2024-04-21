import random

def symbol_generator(length: int, symbol_probabilities: dict) -> str:
  
  string = ''
  
  for i in range(length):

    prob_sum = 0
    random_probability = random.random()

    for i, symbol in enumerate(symbol_probabilities):

      probability = symbol_probabilities[symbol]

      prob_sum += probability
      if random_probability < prob_sum:
        string += symbol
        break

  return string