#include <stdio.h>
#include "utils.h"

// note: taking steps of size 5 & 3 would speed up the alg, as long as you take 
// account for any double counting.
int sum_of_multiples(int top) {
    int sum = 0;
    for (int i = 1; i < top; i++) {
        if (i % 5 == 0 || i % 3 == 0) {
            sum += i;
        }
    }
    return sum;
}

int main() {
    int top = readint("../input1");
    printf("%d\n", sum_of_multiples(top));
}