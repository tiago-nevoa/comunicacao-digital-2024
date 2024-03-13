# Exercise D
def is_prime(a):
    if a <= 1:
        return False

    for number in range(2, a // 2 + 1):
        if a % number == 0:
            return False

    return True

def primes_in_range(left, right):
    for i in range(left, right + 1):
        if(is_prime(i)):
            print(i)

print(is_prime(6))
print(primes_in_range(0, 50))