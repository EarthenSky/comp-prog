// SOLVED

#include <iostream>
#include <vector>
#include <string>

#include <cstddef>

void assign_star(std::vector<bool>& touchedbmp, std::vector<char>& map, size_t inx, size_t iny, size_t w, size_t h) {
    std::vector<size_t> xstack;
    std::vector<size_t> ystack;

    xstack.push_back(inx);
    ystack.push_back(iny);

    while (xstack.size() != 0) {
        size_t curx = xstack.back();
        size_t cury = ystack.back();
        size_t current_index = curx + cury * w;

        xstack.pop_back(); 
        ystack.pop_back();

        touchedbmp[current_index] = true;

        size_t left = current_index - 1;
        size_t right = current_index + 1;
        size_t up = current_index - w;
        size_t down = current_index + w;

        // will consider all adjacent positions each iteration -> no skipping over the left or the right
        if (left < touchedbmp.size() && curx != 0 && touchedbmp[left] == false && map[left] == '-') {
            xstack.push_back(curx-1);
            ystack.push_back(cury);
        } 
        if (right < touchedbmp.size() && curx != w-1 && touchedbmp[right] == false && map[right] == '-') {
            xstack.push_back(curx+1);
            ystack.push_back(cury);
        } 
        if (up < touchedbmp.size() && cury != 0 && touchedbmp[up] == false && map[up] == '-') {
            xstack.push_back(curx);
            ystack.push_back(cury-1);
        } 
        if (down < touchedbmp.size() && cury != h-1 && touchedbmp[down] == false && map[down] == '-') {
            xstack.push_back(curx);
            ystack.push_back(cury+1);
        }
    }
}

void do_test(size_t w, size_t h) {
    size_t star_count = 0;
    std::vector<bool> touchedbmp(w * h, false);
    std::vector<char> map;
    
    // read to a map
    for (size_t y = 0; y < h; y++) {
        std::string line;
        std::cin >> line;

        for (size_t x = 0; x < w; x++) {
            char cur = line[x];
            map.push_back(cur);
        }
    }

    // go through all characters.
    for (size_t y = 0; y < h; y++) {
        for (size_t x = 0; x < w; x++) {
            size_t current_index = x + y * w;
            char cur = map[current_index];
            
            if (cur == '-' && touchedbmp[current_index] == false) {
                assign_star(touchedbmp, map, x, y, w, h);
                star_count += 1;
            }
        }
    }

    std::cout << star_count << std::endl;
}

// TODO: this
void do_test_2(size_t w, size_t h) {
    size_t star_count = 0;
    std::vector<bool> touchedbmp(w * h, false);
    std::vector<char> map;
    
    //std::vector<size_t> xspecial;
    //std::vector<size_t> yspecial;
    
    // read to a map
    for (size_t y = 0; y < h; y++) {
        std::string line;
        std::cin >> line;

        for (size_t x = 0; x < w; x++) {
            char cur = line[x];
            map.push_back(cur);
        }
    }

    // go through all characters. // TODO: only go through star characters to improve performance
    for (size_t y = 0; y < h; y++) {
        for (size_t x = 0; x < w; x++) {
            size_t current_index = x + y * w;
            char cur = map[current_index];
            
            if (cur == '-' && touchedbmp[current_index] == false) {
                assign_star(touchedbmp, map, x, y, w, h);
                star_count += 1;
            }
        }
    }

    std::cout << star_count << std::endl;
}

int main() {
    size_t casen = 1;
    size_t w, h;
    while(std::cin >> h >> w) {
        std::cout << "Case " << casen << ": ";
        do_test(w, h);
        casen += 1;
    }

    return 0;
}