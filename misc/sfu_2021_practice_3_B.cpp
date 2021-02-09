// SOLVED

//#include <vector>
#include <iostream>
#include <cmath> // for sqrt
#include <math.h>
//#include <string>

// NOTE: when trying to optimize a function, consider the 

// NOTE: second two parameters are double, first two are not
double distance(long long x0, long long y0, double x1, double y1) {
    return std::sqrt((x0 - x1) * (x0 - x1) + (y0 - y1) * (y0 - y1));
}

// NOTE: second two parameters are double, first two are not
double distance_nosqrt(long long x0, long long y0, double x1, double y1) {
    return (x0 - x1) * (x0 - x1) + (y0 - y1) * (y0 - y1);
}

long long distance_nosqrt_ll(long long x0, long long y0, long long x1, long long y1) {
    return (x0 - x1) * (x0 - x1) + (y0 - y1) * (y0 - y1);
}

// returns the closest distance from a point in the line segment 1->2 to p.
double line_segment_point_closest_distance(long long px, long long py, long long x1, long long y1, long long x2, long long y2) {
    long long minx = std::min(x1, x2);
    long long maxx = std::max(x1, x2);
    long long miny = std::min(y1, y2);
    long long maxy = std::max(y1, y2);

    double xint, yint;
    
    if (x1 - x2 == 0) { // case: line is vertical
        xint = x2;
        yint = py;
    } else if (y1 - y2 == 0) { // case: line is horizontal
        xint = px;
        yint = y2;
    } else {
        double m1 = (y1 - y2) / static_cast<double>(x1 - x2); 
        //double m2 = -1 / m1;

        xint = (px + m1*m1 * x1 + (py - y1) * m1) / (m1*m1 + 1);
        //xint = (-m2 * px + m1 * x1 + py - y1) / (m1 - m2);
        yint = m1 * (xint - x1) + y1;
        
    }

    if (xint <= maxx and xint >= minx and yint <= maxy and yint >= miny) {
        return distance_nosqrt(px, py, xint, yint);
    } else if (distance_nosqrt(x1, y1, xint, yint) >= distance_nosqrt(x2, y2, xint, yint)) {
        return distance_nosqrt_ll(px, py, x2, y2);
    } else {
        return distance_nosqrt_ll(px, py, x1, y1);
    }
}

int main() {
    long long n, px, py;
    std::cin >> n >> px >> py;

    long long fx, fy, lx, ly;
    std::cin >> fx >> fy;
    lx = fx; 
    ly = fy; 

    double min = distance_nosqrt_ll(px, py, fx, fy);
    double max = min;
    for (long long i = 1; i < n; i++) {
        long long ix, iy;
        std::cin >> ix >> iy;
        
        // checking for max
        double dist = distance_nosqrt_ll(px, py, ix, iy);
        max = std::max(max, dist);

        // check closest edge position
        dist = line_segment_point_closest_distance(px, py, lx, ly, ix, iy);
        min = std::min(min, dist);
        
        lx = ix;
        ly = iy;
    }

    // last edge check here
    double dist = line_segment_point_closest_distance(px, py, lx, ly, fx, fy);
    min = std::min(min, dist);

    double pi = 3.14159265358979323846264338327950;

    std::cout.precision(16);
    std::cout << pi * (max - min) << "\n";

    return 0;
}