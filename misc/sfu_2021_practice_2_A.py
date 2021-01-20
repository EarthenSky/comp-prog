# SOLVED

# solving: https://vjudge.net/contest/418454#problem/A
# from: https://codeforces.com/problemset/problem/540/A

def difference_from_zero(x):
    return 10 - x if 10 - x < x else x

def main():
    disk_num = int(input())
    start = input()
    target = input()

    running_total = 0

    for i in range(0, disk_num):
        cs, ct = start[i], target[i]
        cs, ct = int(cs), int(ct)
        
        if abs(cs - ct) < difference_from_zero(ct) + difference_from_zero(cs):
            running_total += abs(cs - ct)
        else:
            running_total += difference_from_zero(ct) + difference_from_zero(cs)

    print( "{}".format(running_total) )

main()