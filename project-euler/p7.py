import math
import time

def is_prime(n):
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# TODO: can I use maths to continue optimizing this function?
#       can we find a recursive definition for primes? 
#       or maybe a quick definition?
#       what pattern do the prime steps aproach, & how to they appraoch it?
def nth_prime(n):
    if n == 1: return 2
    
    i, pth = 3, 1
    while pth < n:
        if is_prime(i):
            pth += 1

        i += 2

    return i - 2

start = time.time()
#print(nth_prime(6))
#print(nth_prime(2001))
print(nth_prime(10001))
print(time.time() - start)