class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        if amount == 0:
            return 1

        coins.sort()

        @lru_cache(maxsize=None)
        def change_rec(curr_amount, ci):
            if curr_amount == 0:
                return 1
            elif ci == 0:
                return 0

            result = change_rec(curr_amount, ci-1)
            coin = coins[ci-1]
            if curr_amount >= coin:
                result += change_rec(curr_amount - coin, ci)

            return result

        return change_rec(amount, len(coins))

    def change_n_memory(self, amount: int, coins: list[int]) -> int:
        if amount == 0:
            return 1

        coins.sort()

        M = [0 for _ in range((amount+1) * 2)]
        M[amount+1] = 1

        for ci in range(1, len(coins)+1):
            M[:amount+1] = M[amount+1:]
            coin = coins[ci-1]
            for coin_offset in range(coin):
                running_val = 1 if coin_offset+1 == coin else 0
                for curr_amount in range(coin_offset+1, amount+1, coin):
                    running_val += M[curr_amount]
                    M[amount+1 + curr_amount] = running_val

        return M[-1]

    def change_cache_efficient(self, amount: int, coins: list[int]) -> int:
        M = [1] + [0 for _ in range(amount)]
        for coin in coins:
            for curr_amount in range(amount - coin + 1):
                M[curr_amount+coin] += M[curr_amount]
        return M[-1]