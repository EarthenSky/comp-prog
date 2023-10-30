#include <stdio.h>
#include <stdint.h>
#include <math.h>

#include "utils.h"

uint64_t floor_sqrt(uint64_t x) {
    return (uint64_t) floor(sqrt((double) x));
}

// NOTE: this function assumes no prime factor occurs more than once, as that
// could mess with the performance.
uint64_t largest_prime_factor(uint64_t x) {
    for (uint64_t i = 2; i < floor_sqrt(x); i++) {
        if (x % i == 0) {
            x = x / i;
            i = 2;
        }
    }
    return x;
}

int main() {
    uint64_t x = readu64("../input3");
    printf("%ld\n", largest_prime_factor(x));
}