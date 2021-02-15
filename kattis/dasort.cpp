// SOLVED

#include <vector>
#include <iostream>

void solve_test_solution_1() {
    int k, n;
    std::cin >> k >> n;

    // fill vector with items.
    // NOTE: in order to further optimize, take first min in this loop.
    std::vector<int> items;
    for (int i = 0; i < n; i++) {
        int cur;
        std::cin >> cur;
        items.push_back(cur);
    }

    int goodNodeCount = 0; // number of min nodes that are good

    int lastMinIndex = 0;
    int lastMinVal = 0;
    while (true) {
        // get smallest right of lastMinIndex
        int rightMin = 1000 * 1000 * 1000 + 1, rightIndex = 0, rightCount = 0;
        for(int i = lastMinIndex; i < items.size(); i++) {
            int el = items[i];
            if (el > lastMinVal && el < rightMin) {
                rightMin = el;
                rightIndex = i;
                rightCount = 1;
            } else if (el == rightMin) {
                rightCount += 1;
                rightIndex = i; // NOTE: rightIndex choses the rightmost of the min elements.
            }
        }

        // get smallest left of lastMinIndex
        int leftMin = 1000 * 1000 * 1000 + 1; //, leftIndex = 0, leftCount = 0;
        for(int i = 0; i < lastMinIndex; i++) {
            int el = items[i];
            if (el > lastMinVal && el < leftMin) {
                leftMin = el;
            }
        }

        // check conditions.
        if (leftMin == rightMin) {
            goodNodeCount += rightCount;
            break;
        } else if (leftMin < rightMin) {
            break;
        } else {
            goodNodeCount += rightCount;
            lastMinIndex = rightIndex;
            lastMinVal = rightMin;
        }
    }   

    std::cout << (n - goodNodeCount) << std::endl;

    // take min larger than a limit l until the index of the min is left of the last min.
}

int main () {
    int p;
    std::cin >> p;

    for (int i = 0; i < p; i++) {
        std::cout << i+1 << " ";
        solve_test_solution_1();
    }
}