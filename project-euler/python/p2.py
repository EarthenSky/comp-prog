def even_fib(n):
    sum = 0
    last_two = (1, 1)
    while last_two[1] <= n:
        current = last_two[0] + last_two[1]
        last_two = (last_two[1], current)
        #print(current)
        if current % 2 == 0:
            sum += current
    return sum

print(even_fib(4 * 1000 * 1000))