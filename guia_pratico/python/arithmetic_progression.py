# Exercise A
# Term = u + (n-1) * r
# u - first term
# r - common difference
def arithmetic_progression(N, u, r) -> list:
    
    if not any(isinstance(x, (int, float)) for x in (N, u, r)):
        raise ValueError('Input must be an integer or float')

    if N <= 0:
        raise ValueError('N has to be a positive number')

    progression = []

    for i in range(1, N+1):
        if( i == 1 ):
            term = u
        else:
            term = u + (i-1) * r
        progression.append(term)
        
    return progression