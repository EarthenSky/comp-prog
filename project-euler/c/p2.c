#include <stdio.h>
#include "utils.h"

int even_fib(int n) {
    int sum = 0;
    int fa = 1;
    int fb = 1;
    while (fb <= n) {
        int current = fa + fb;
        fa = fb;
        fb = current;
        if (current % 2 == 0) {
            sum += current;
        }
    }
    return sum;
}

int main() {
    int n = readint("../input2");
    printf("%d\n", even_fib(n));
}