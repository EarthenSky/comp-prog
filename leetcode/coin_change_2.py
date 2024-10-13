class Solution:
    # TODO can we do this top down, instead of bottom up, to possibly save some performance?
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        
        M = [0 for i in range( (len(coins)+1) * (amount+1) )]

        # 1 way to use n coins to get 0 dollars (use zero coins)
        for ci in range(len(coins)+1):
            M[ci * (amount+1)] = 1

        for ci in range(1, len(coins)+1):
            coin = coins[ci-1]
            for curr_amount in range(1, amount+1):
                if (curr_amount - coin) == 0:
                    M[curr_amount + ci*(amount+1)] += (
                        M[curr_amount - coin + ci*(amount+1)]
                    )
                elif (curr_amount - coin) > 0:
                    M[curr_amount + ci*(amount+1)] += (
                        M[curr_amount - coin + ci*(amount+1)]
                    )

                M[curr_amount + ci*(amount+1)] += M[curr_amount + (ci-1)*(amount+1)]

        return M[-1]