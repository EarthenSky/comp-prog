class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        if amount == 0:
            return 1
        
        @lru_cache(maxsize=None)
        def change_rec(curr_amount, ci):
            if curr_amount == 0:
                return 1
            elif ci == 0:
                return 0

            curr_index = curr_amount + ci*(amount+1)
            result = change_rec(curr_amount, ci-1)
            coin = coins[ci-1]
            if curr_amount >= coin:
                result += change_rec(curr_amount - coin, ci)

            return result

        return change_rec(amount, len(coins))