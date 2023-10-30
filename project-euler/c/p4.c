#include <stdio.h>
#include <stdbool.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

#include "utils.h"

bool is_palindrome(int x) {
    char str[MAX_CHARS_INT];
    sprintf(str, "%d", x);

    int len = strlen(str);
    for (int i = 0; i < len / 2; i++) {
        if (str[i] != str[len - 1 - i]) {
            return false;
        }
    }
    return true;
} 

int largest_palindromic_number(int limit) {
    int largest = 0;
    for (int i = 1; i < limit; i++) {
        for (int j = i+1; j < limit; j++)  {
            if ((i * j > largest) && is_palindrome(i * j)) {
                largest = i * j;
            }
        }
    }
    return largest;
}

int main() {
    int limit = readint("../input4");
    printf("%d\n", largest_palindromic_number(limit * 30));
}