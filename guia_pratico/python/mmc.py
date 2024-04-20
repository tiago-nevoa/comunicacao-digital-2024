# Exercise C
def mdc(a, b):

    if not any(isinstance(x, (int, float)) for x in (a, b)):
        raise ValueError('Input must be an integer or float')

    if a < 0 or b < 0:
        raise ValueError('None of the numbers can be negative')

    # Euclidean Algorithm
    result = a % b

    while(result != 0):

        temp = b % result

        if(temp == 0):
            return result
        
        b = result
        result = temp

    if b < 0:
        b = abs(b)

    return b

def mmc(a, b):

    if not any(isinstance(x, (int, float)) for x in (a, b)):
        raise ValueError('Input must be an integer or float')

    # Inverts the signal if negative
    a = abs(a)
    b = abs(b)

    if a == 0 or b == 0:
        raise ValueError('None of the numbers can be zero')

    return a * b // mdc(a, b)