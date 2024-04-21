import random

def symbol_generator(length: int, symbol_probabilities: dict, use_spacing = False) -> str:
  
  string = ''
  
  for i in range(length):

    prob_sum = 0
    random_probability = random.random()

    for j, symbol in enumerate(symbol_probabilities):

      probability = symbol_probabilities[symbol]

      prob_sum += probability
      if random_probability < prob_sum:
        # 'and string' checked to avoid adding spaces as a first symbol of the string
        if use_spacing and string:
          string += ' '
        string += symbol
        break

  return string