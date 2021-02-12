// SOLVED

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    string in;
    cin >> in;

    unsigned int i;
    for(i = 1; i < in.size() + 1; i++) {
        if (in.size() % i == 0) {

            // check the string
            bool is_valid = true;
            unsigned int buf_i = i - 1;
            for (unsigned int cur = i; cur < in.size(); cur++) {
                if (in[buf_i] != in[cur]) {
                    is_valid = false;
                    break;
                }
                
                // case: last char in period.
                if (cur % i != i - 1) { 
                    buf_i += 1;
                    if (buf_i > i - 1) { // check for buffer overflow
                        buf_i = 0;
                    }
                }
            }
            
            if (is_valid) {
                break;
            }
        }
    }

    cout << i << endl;

    return 0;
}