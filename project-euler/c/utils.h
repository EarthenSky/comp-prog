#ifndef UTILS
#define UTILS

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define MAX_CHARS_INT 64

int readint(char* filepath) {
    FILE *fptr = fopen(filepath, "r");
    char str[MAX_CHARS_INT];
    
    fgets(str, MAX_CHARS_INT, fptr);
    fclose(fptr);

    return atoi(str);
}

uint64_t readu64(char* filepath) {
    FILE *fptr = fopen(filepath, "r");
    char str[MAX_CHARS_INT];
    
    fgets(str, MAX_CHARS_INT, fptr);
    fclose(fptr);

    return (uint64_t) atoll(str);
}

#endif