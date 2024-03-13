# Exercise A
# Term = u + (n-1) * r
def arithmetic_progression(N, u, r):
    for i in range(N):
        if( i == 0 ):
            term = u
        else:
            term = u+(i)*r
        print(term)

arithmetic_progression(10, 1, 2)