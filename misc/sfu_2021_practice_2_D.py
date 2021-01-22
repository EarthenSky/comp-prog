# SOLVED

# solving: https://vjudge.net/contest/418454#problem/D
# from: https://codeforces.com/problemset/problem/548/B

def get_info_current(grid, x, y, m):
    dist_r = 0
    hit = False
    if x % m != m-1:
        for i in range(x+1, m):
            if grid[i + y * m] != 1:
                dist_r = i - x - 1
                hit = True
                break
        if not hit: dist_r = m - x - 1

    dist_l = 0
    hit = False
    if x % m != 0:
        for i in range(x-1, -1, -1):
            if grid[i + y * m] != 1:
                dist_l = x - i - 1
                hit = True
                break
        if not hit: dist_l = x - (-1) - 1

    return (dist_r, dist_l)

def do_simulation(grid, n, m):
    # Do simulation
    max_val = 0
    current_run = 0
    for i in range(0, n*m):
        if i % m == 0:
            if current_run > max_val:
                max_val = current_run
            current_run = 0

        if grid[i] == 1:
            current_run += 1
        else:
            if current_run > max_val:
                max_val = current_run
            current_run = 0
        
    if current_run > max_val:
        max_val = current_run

    return max_val

def main():
    invalues = input().strip().split(" ")
    n, m, q = int(invalues[0]), int(invalues[1]), int(invalues[2])
    
    # init grid
    grid = [0 for _ in range(0, n * m)]
    for i in range(0, n):
        row = input().strip().split(" ")
        for x in range(0, m):
            grid[i * m + x] = int(row[x])

    max_val = do_simulation(grid, n, m)

    # apply rounds
    for round in range(0, q):
        invalues = input().strip().split(" ")
        x, y = int(invalues[1])-1, int(invalues[0])-1

        dist_r, dist_l = get_info_current(grid, x, y, m)

        #print("{}".format(grid))
        #print("{} {}".format(dist_l, dist_r))

        val = grid[x + y * m]
        if val == 1:
            grid[x + y * m] = 0
            if dist_r + dist_l + 1 == max_val:
                # NOTE: only need to simulate the current row if I have a matrix containing the saved lengths of runs in
                # each row. Then you can find max from a smaller matrix. -> BIG speed up...
                max_val = do_simulation(grid, n, m) 
        else:
            grid[x + y * m] = 1 
            if dist_r + dist_l + 1 > max_val:
                max_val = dist_r + dist_l + 1

        print("{}".format(max_val))

main()