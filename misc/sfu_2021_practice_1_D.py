# SOLVED

# solving: https://codeforces.com/problemset/problem/80/B
# from: https://vjudge.net/contest/417235#problem/D

def main():
    inlist = input().split(":")
    hh, mm = int(inlist[0]), int(inlist[1])

    deg_per_h = 360/12
    deg_per_m = 360/60

    hours = ((hh+mm/60) * deg_per_h) % 360
    mins = (mm * deg_per_m) % 360

    if hours % 1 == 0: hours = int(hours)
    if mins % 1 == 0: mins = int(mins)

    print( "{} {}".format(hours, mins) )

main()