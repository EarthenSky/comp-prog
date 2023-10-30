from utils import readint

def even_fib(n):
    sum = 0
    last_two = (1, 1)
    while last_two[1] <= n:
        current = last_two[0] + last_two[1]
        last_two = (last_two[1], current)
        if current % 2 == 0:
            sum += current
    return sum

n = readint("../input2")
print(even_fib(n))