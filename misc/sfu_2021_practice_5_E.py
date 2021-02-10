# SOLVED

# solving: https://vjudge.net/contest/421568#problem/E
# from: https://codeforces.com/problemset/problem/285/C

# NOTE: I don't 100% understand why this works.

def main2():
    n = int(input())
    p_list = list(map(int, input().split(" ")))

    running_total = 0

    p_list.sort()
    for i in range(0, n):
        running_total += abs(i+1 - p_list[i])

    print(running_total)

main2()