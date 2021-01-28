// SOLVED

// solving:
// from: 

#include <vector>
#include <iostream>
#include <string>

// NOTE: this function could be optimized into a constant time operation rather than a O(26*2) operation
// UPDATE: this optimization didn't affect anything either !!!???!?! -> praise compilers.
int array_sum(int a[], unsigned int size) {
    int sum = 0;
    for(unsigned int i = 0; i < size; i++) {
        sum += a[i];
    }
    return sum;
}

int pkm_to_i(char c) {
    return c <= 'Z' ? (c - 'A') + 26 : c - 'a';
}

int main() {
    int n;
    std::cin >> n;

    std::string s;
    std::cin >> s;

    int char_map[26 * 2];
    std::fill(std::begin(char_map), std::end(char_map), 0); // WHY DO YOU LIE ABOUT ZERO INITIALIZATION G++, WHYYY!!
    for (char &c : s) {
        char_map[pkm_to_i(c)] = 1;
    }

    int num_unique_chars = array_sum(char_map, 26 * 2);
    //std::cout << num_unique_chars << "\n";

    std::fill(std::begin(char_map), std::end(char_map), 0);
    int char_count_map[26 * 2];
    std::fill(std::begin(char_count_map), std::end(char_count_map), 0);

    int running_array_sum = 0;

    int min_num = 100 * 1000; // max n
    int i = 0, ci = 0;
    while (i < s.size()) {
        if (/*array_sum(char_map, 26 * 2)*/ running_array_sum == num_unique_chars) {
            min_num = std::min(min_num, i - ci);

            char sc = s[ci];
            char_count_map[pkm_to_i(sc)] -= 1;
            
            // optimization here => inc ci until a char is removed from char_map.
            // UPDATE: it didn't change performance ;<
            if (char_count_map[pkm_to_i(sc)] == 0) {
                char_map[pkm_to_i(sc)] = 0;
                running_array_sum -= 1;
            }

            ci += 1; // move up next starting char
            
        } else {
            char c = s[i];
            
            running_array_sum += char_map[pkm_to_i(c)] == 0;
            char_map[pkm_to_i(c)] = 1;
            char_count_map[pkm_to_i(c)] += 1;
            
            i += 1; // move up next end char
        }

        //std::cout << "i:" << i << "\n";
    }

    while (ci < s.size()) {
        if (running_array_sum == num_unique_chars) {
            min_num = std::min(min_num, i - ci);

            char sc = s[ci];
            char_count_map[pkm_to_i(sc)] -= 1;
            
            // optimization here => inc ci until a char is removed from char_map.
            // UPDATE: it didn't change performance ;<
            if (char_count_map[pkm_to_i(sc)] == 0) {
                char_map[pkm_to_i(sc)] = 0;
                running_array_sum -= 1;
            }

            ci += 1; // move up next starting char
        } else {
            break;
        }

        //std::cout << "ci:" << ci << "\n";
    }

    std::cout << min_num << "\n";

    return 0;
}