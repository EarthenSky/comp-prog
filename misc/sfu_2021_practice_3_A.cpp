// SOLVED

// solving:
// from: 

//#include <vector>
#include <iostream>

int main() {
    int v1 = 0, v2 = 0;
    int t = 0, d = 0;

    std::cin >> v1 >> v2;
    std::cin >> t >> d;
    
    if (d == 0) {
        std::cout << v1 * t << "\n";
        return 0;
    }

    int speed = v1;
    int path_len = 0;
    
    int t1 = (d * t + v2 - v1) / (2 * d);
    int t2 = ((d * t + v2 - v1) % (2 * d)) == 0 ? t1 : t1 + 1;
    
    //std::cout << "p1 " << (d * (t) + v2 - v1) << "\n";
    //std::cout << "p2 " << 2*d << "\n";

    path_len += v1 * t1 + v2 * (t - t2);

    //std::cout << "pathlen " << path_len << "\n";

    path_len += ((t1 - 1) * t1 * d) / 2; 
    //std::cout << "pathlen " << path_len << "\n";

    path_len += (((t - t2) - 1) * (t - t2) * d) / 2; 
    //std::cout << "pathlen " << path_len << "\n";

    // do middle section
    if (t2 == t1 + 1) {
        if (v1 + (t1-1) * d > v2 + (t-t2-1) * d) {
            path_len += (v2 + (t-t2) * d);
        } else {
            path_len += (v1 + (t1) * d);
        }
    }

    /*
    for (int i = 0; i < t; i++) {
        path_len += speed;
        speed = std::min(v2, speed + d);
    }*/
    
    std::cout << path_len << "\n";

    return 0;
}