# COMPLETED !!!!!!!!!

# see c++ for faster solution

def distance(x0, y0, x1, y1):
    return ((x0 - x1) * (x0 - x1) + (y0 - y1) * (y0 - y1))**0.5

# returns the closest distance from a point in the line segment 1->2 to p.
def line_segment_point_closest_distance(px, py, x1, y1, x2, y2):
    minx = min(x1, x2)
    maxx = max(x1, x2)
    miny = min(y1, y2)
    maxy = max(y1, y2)
    
    if (x1 - x2) == 0: # case: line is vertical
        xint = x2
        yint = py
    elif (y1 - y2) == 0: # case: line is horizontal
        xint = px
        yint = y2
    else:
        m1 = (y1 - y2) / (x1 - x2) 
        m2 = -1 / m1

        xint = (-m2 * px + m1 * x1 + py - y1) / (m1 - m2)
        yint = m1 * (xint - x1) + y1

    if (xint <= maxx and xint >= minx and yint <= maxy and yint >= miny):
        return distance(px, py, xint, yint)
    elif distance(xint, yint, x1, y1) >= distance(xint, yint, x2, y2):
        return distance(px, py, x2, y2)
    else:
        return distance(px, py, x1, y1)

def main():
    invalues = input().strip().split(" ")
    n, px, py = int(invalues[0]), int(invalues[1]), int(invalues[2])

    invalues = input().strip().split(" ")
    fx, fy = int(invalues[0]), int(invalues[1])
    lx, ly = fx, fy

    min_n = distance(px, py, fx, fy)
    max_n = distance(px, py, fx, fy)
    for _ in range(1, n):
        invalues = input().strip().split(" ")
        ix, iy = int(invalues[0]), int(invalues[1])
        
        # checking for max
        dist = distance(px, py, ix, iy)
        max_n = max(max_n, dist)

        # check closest edge position
        dist = line_segment_point_closest_distance(px, py, lx, ly, ix, iy)
        min_n = min(min_n, dist)
        
        lx, ly = ix, iy

    # last edge check here
    dist = line_segment_point_closest_distance(px, py, lx, ly, fx, fy)
    min_n = min(min_n, dist)

    #print("minL ", min_n)
    #print("maxL ", max_n)

    pi = 3.141592653589793238462643383279502884
    print("{}".format(pi * (max_n ** 2 - min_n ** 2)))

main()
