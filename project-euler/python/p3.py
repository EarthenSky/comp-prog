import math
from utils import readint

# oh cool! Since we're going in smallest order first, the last number will be the largest
def largest_prime_factor(x):
    i = 2
    while i < math.floor(math.sqrt(x)):
        if x % i == 0:
            print("x: {}, i: {}".format(x, i))
            x = x // i
            i = 2
        i += 1
    return x

x = readint("../input3")
print(largest_prime_factor(x)) 