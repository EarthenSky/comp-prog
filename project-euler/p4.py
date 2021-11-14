import math
import time

def nth_digit(x, n):
    return math.floor(x / 10 ** n) % 10

def is_palindrome(x):
    top = math.ceil(math.log(x, 10))-1
    bot = 0
    while top > bot:
        end_digit = nth_digit(x, bot)
        start_digit = nth_digit(x, top)

        if start_digit != end_digit:
            return False
        else: 
            top -= 1
            bot += 1
    return True

# unfortunately this is faster ;-;
def is_palindrome_2(x):
    x = str(x)
    for i in range(0, len(x)//2):
        if x[i] != x[len(x)-1-i]:
            return False
    return True

def largest_palindromic_number(limit):
    largest = 0
    for i in range(1, limit):
        #if largest > (i * limit): continue
        for j in range(1, limit):
            if i * j > largest and is_palindrome_2(i * j):
                largest = i * j

    return largest

start = time.time()
print(largest_palindromic_number(1000))
print(time.time() - start, "s")