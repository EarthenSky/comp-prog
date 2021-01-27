// SOLVED

// solving:
// from: 

#include <vector>
#include <iostream>

int main() {
    int n, x0, y0;
    std::cin >> n >> x0 >> y0;

    std::vector<int> posx_list;
    std::vector<int> posy_list;

    // get all positions
    for(int i = 0; i < n; i++) {
        int x, y;
        std::cin >> x >> y;
        posx_list.push_back(x);
        posy_list.push_back(y);
    }

    unsigned int shots = 0;

    // each storm trooper casts a ray towards h and sees how many points it intersects.
    // if the ray hits no other points, then the trooper is immediately shot.
    while(!posx_list.empty()) {
        int x = posx_list.back();
        int y = posy_list.back();
        posx_list.pop_back(); posy_list.pop_back();

        std::vector<int> posx_list_new;
        std::vector<int> posy_list_new;

        // if the ray hits another point, then that point is also destroyed.
        for(int i = 0; i < posx_list.size(); i++) {
            int xi = posx_list[i];
            int yi = posy_list[i];
            if (x - x0 == 0) {
                if (xi == x0) { 
                    // pass
                    //std::cout << "did it!" << "\n";
                } else {
                    posx_list_new.push_back(xi);
                    posy_list_new.push_back(yi);
                }
            } else if (((y - y0) * (xi - x0) / (x - x0) + y0 == yi) && (((y - y0) * (xi - x0)) % (x - x0) == 0)) { // determines if the point is on the line
                // pass
                //std::cout << "did it!" << "\n";
            } else {
                posx_list_new.push_back(xi);
                posy_list_new.push_back(yi);
            }
        }
        
        // update lists
        posx_list = posx_list_new;
        posy_list = posy_list_new;

        //std::cout << posx_list.size() << "\n";

        shots += 1;
    }

    std::cout << shots << "\n";

    return 0;
}