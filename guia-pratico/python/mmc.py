# Exercise C
def mdc(a, b):

    # Euclidean Algorithm
    result = a % b

    while(result != 0):

        temp = b % result

        if(temp == 0):
            return result
        
        b = result
        result = temp

    return b

def mmc(a, b):
    return a * b / mdc(a, b)

print(mdc(12, 9))
print(mmc(11, 900))