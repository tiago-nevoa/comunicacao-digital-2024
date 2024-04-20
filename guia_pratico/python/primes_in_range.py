# Exercise D
def is_prime(a) -> bool:

    if not isinstance(a, (int, float)):
        raise ValueError('Input must be an integer or float')

    if a <= 1:
        return False

    for number in range(2, a // 2 + 1):
        if a % number == 0:
            return False

    return True

def primes_in_range(left, right) -> list:

    if not any(isinstance(x, (int, float)) for x in (left, right)):
        raise ValueError('Input must be an integer or float')

    if left > right:
        raise ValueError('The right number has to be greater or equal than the left one')

    prime_list = []

    for i in range(left, right + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list