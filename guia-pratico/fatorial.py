# Exercise B
def fatorial(a):
    result = 1
    while(a > 1):
        result *= a
        a -= 1
    return result

print(fatorial(4))