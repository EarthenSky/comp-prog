# SOLVED

# solving: https://codeforces.com/problemset/problem/1008/B
# from: https://vjudge.net/contest/417235#problem/G

def main():
    rect_num = int(input())

    last = 10**9 + 1
    for i in range(0, rect_num):
        in_values = input().split(" ")
        w = int(in_values[0])
        h = int(in_values[1])

        if (w > last and h > last):
            print("NO")
            return

        if w > h:
            w, h = h, w # let h be largest

        last = w if h > last else h

    print("YES")

main()