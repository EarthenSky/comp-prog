#include <stdio.h>
#include <stdint.h>

int change(int amount, int* coins, int coinsSize) {
    uint64_t M[amount+1];
    memset(M, 0, (amount+1) * sizeof(uint64_t));
    M[0] = 1;
    for (size_t ci = 0; ci < coinsSize; ci++)
        for (size_t curr_amount = 0; curr_amount + coins[ci] < amount + 1; curr_amount++)
            M[curr_amount + coins[ci]] += M[curr_amount];
    return M[amount];
}

int change_old(int amount, int* coins, int coinsSize) {
    if (amount == 0)
        return 1;

    size_t amount_size = amount;
    size_t coinsSize_size = coinsSize;

    size_t M_SIZE = (coinsSize_size+1) * (amount_size+1);
    uint64_t M[M_SIZE];
    memset(M, 0, M_SIZE * sizeof(uint64_t));

    // 1 way to use n coins to get 0 dollars (use zero coins)
    for (size_t ci = 0; ci < coinsSize_size+1; ci++)
        M[0 + ci * (amount_size+1)] = 1;

    for (size_t ci = 1; ci < coinsSize_size+1; ci++) {
        size_t coin = (size_t) coins[ci-1];
        for (size_t curr_amount = 1; curr_amount < amount_size+1; curr_amount++) {
            if (curr_amount >= coin) {
                M[curr_amount + ci*(amount_size+1)] += M[curr_amount - coin + ci*(amount_size+1)];
            }
            M[curr_amount + ci*(amount_size+1)] += M[curr_amount + (ci-1)*(amount_size+1)];
        }
    }

    return M[M_SIZE - 1];
}
