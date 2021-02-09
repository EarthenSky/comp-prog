// SOLVED

#include <vector>
#include <iostream>
#include <sstream>
#include <string>

// Lessons:
//  - Read the initial testcase & understand how it works before writing a 100+ line solution. 

int rec_do_cut(std::vector<int>& hole_positions, int cur_i, int min_l, int k) {
    std::cout << "cur_i, min_l, k: " << cur_i << "," << min_l << "," << k << "\n";
    if (cur_i + 1 == hole_positions.size() - 2) { // This means we went too far. -> should never trigger.
        return -1;
    }

    if(k == 1) { // base-case: just return sum of elements in the last area.
        int sum = 0;
        for(int i = 0; i < hole_positions.size(); i++) {
            sum += hole_positions[i];
        }
        return sum;
    } else {
        int cur_v = 0; // the value of the current segment
        int max_best_l = min_l;

        do {
            std::cout << "loop, cur_v: " << cur_v << "\n";
            while (cur_i + 1 < hole_positions.size() - 2 && cur_v + hole_positions[cur_i + 1] <= max_best_l) {
                cur_v += hole_positions[cur_i];
                cur_i += 1;
            }

            if (cur_i + 1 == hole_positions.size() - 2) { // This means we went too far. -> should never trigger?
                return -1;
            }

            max_best_l = rec_do_cut(hole_positions, cur_i + 1, min_l, k - 1);
            
            // needs to report back smallest section, but section is represented by maximum.
            int max_current_iteration = std::max(max_best_l, cur_v);
            min_l = std::min(min_l, max_current_iteration);

            if(max_best_l == -1) 
                break;

        } while(cur_v + hole_positions[cur_i + 1] <= min_l); // gt here? -> change to normal while? -> i think do while is good.

        return min_l;
    }
}

void do_case() {
    std::cout << "case\n";

    int n, k;
    std::cin >> n >> k;

    int max = 0, sum = 0; // biggest single value.
    std::vector<int> hole_positions; // TODO: initialize vector size.
    
    int num, last;
    std::string line;
    
    //std::cin.ignore();
    std::getline(std::cin, line);
    std::getline(std::cin, line);
    std::cout << "line: " << line << "\n";
    std::istringstream stream(line);
    stream >> last;
    while (stream >> num) {
        int diff = num - last;
        sum += diff;
        max = std::max(max, diff);
        hole_positions.push_back(diff);
        last = num;
        std::cout << "num: " << diff << "\n";
    }

    std::cout << "rec start: max, sum " << max << "," << sum << "\n";

    // call recursive function, return max, memoize.
    int min_l = std::max(max, sum / n); // biggest of max & floor(mean).
    std::cout << rec_do_cut(hole_positions, 0, min_l, k)+1 << std::endl; // this +1 is probably okay here.
}

int main() {
    int t;
    std::cin >> t;

    // do cases
    for(int i = 0; i < t; i++) {
        do_case();
    }

    return 0;
}
