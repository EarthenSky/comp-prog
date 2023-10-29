// SOLVED

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    string in;
    while (cin >> in) {
        if(in == "0") { return 0; }
        
        // do one pass through each string
        // fill w vector with lower case letters 
        vector<string> w;

        // fill uppercase vector with upper letters
        vector<string> u;

        // fill N containing vector with N
        vector<string> n;

        // data input
        for (unsigned int i = 0; i < in.size(); i++) {
            if(in[i] == 'p' || in[i] == 'q' || in[i] == 'r' || in[i] == 's' || in[i] == 't') {
                w.push_back(string(1, in[i]));
            } else if (in[i] == 'N') {
                n.push_back(string(1, in[i]));
            } else {
                u.push_back(string(1, in[i]));
            }
        }

        // case 1: if nm is empty and w is empty: 
        if (w.empty()) {
            cout << "no WFF possible" << endl;
        // case 2: if nm is empty and w is not empty: print(w[0])
        } else if (u.size() + n.size() == 0  && !w.empty()) {
            cout << w[1] << endl;
        } else {
            while (
                !(u.size() + n.size() == 0) and 
                !(n.size() == 0 and w.size() == 1) //and !w.empty()
            ) {
                if (n.size() > 0) {
                    string N = n[n.size()-1];
                    n.pop_back();

                    string p = w[w.size()-1];
                    w.pop_back();

                    string new_string = (N + p);
                    w.push_back(new_string);
                } else {
                    string U = u[u.size()-1];
                    u.pop_back();

                    string p1 = w[w.size()-1];
                    string p2 = w[w.size()-2];
                    w.pop_back();
                    w.pop_back();

                    string new_string = (U + p1 + p2);
                    w.push_back(new_string);
                }
            }

            cout << w[w.size()-1] << endl;
        }
    }

    return 0;
}