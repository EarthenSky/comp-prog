# solving: https://open.kattis.com/problems/diagonalcut
# from: https://vjudge.net/contest/417235#problem/A

import math

def all():
    in_values = input().split(" ")

    m = int(in_values[0])
    n = int(in_values[1])
    d = int(math.gcd(m, n))

    # Setting up variables

    if m > n:
        m,n = n,m # n is always bigger

    m //= d
    n //= d
    target = (n - m) // 2
    
    # Early exit conditions
    
    if (n - m) % 2 != 0:
        print("0")
        return 

    if m == n:
        print(d)
        return

    # NOTE: this solution was trying to determine if the target location is ever
    # intersected by using remainders in a factor like approach.
    '''
    while True:
        print(m, target, n)
        print( "{}*{}".format(target // m, m) ) 

        if target % m == 0:
            print(d) 
            return

        if n % m == 0:
            print("0") 
            return

        new_m = m - (n % m)
        new_target = target % m
        new_n = m

        m, target, n = new_m, new_target, new_n
    '''
    
    # NOTE: this solution works, however it is designed in such a way that if the 
    # early exit conditions are insufficient, then it will still produce valid output.
    # However, the early exit conditions are valid for all possible input values.
    '''
    i = m * (n // 2) # starts this loop right at the middle chocolate square
    while i % n != 0:
        if i % n == target:
            print(d)
            return
        i += m
    '''

    # NOTE: this works because the only position a chocolate square which can be 
    # cut in half could be is the center since the pattern before and after the 
    # divisible slice is symmetrical.
    if m * (n // 2) % n == target:
        print(d)
    else:
        print("0")
    
all()