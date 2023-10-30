import math

# oh cool! Since we're going in smallest order first, the last number will be the largest
def largest_prime_factor(x):
    #max_factor = 0
    i = 2
    while i < math.floor(math.sqrt(x)):
        if x % i == 0:
            print("x: {}, i: {}".format(x, i))
            #max_factor = max(max_factor, i)

            # reset loop
            x = x // i
            i = 2
        i += 1
    return x #max(max_factor, x)

print(largest_prime_factor(600851475143)) 