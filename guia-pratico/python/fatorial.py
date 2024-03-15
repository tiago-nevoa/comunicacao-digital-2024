# Exercise B
def fatorial(a):

    if a < 0:
        raise ValueError('Not able to get factorial of a negative number')

    result = 1
    while(a > 1):
        result *= a
        a -= 1
    return result