class Solution:

    def coinChangeSpace(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        prev = [float('inf')] * (amount + 1)
        
        for target in range(amount + 1):
            if target % coins[0] == 0:
                prev[target] = target // coins[0]
                
        for ind in range(1, n):
            curr = [float('inf')] * (amount + 1)
            for target in range(amount + 1):
                not_take = prev[target]
                take = float('inf')
                if coins[ind] <= target:
                    res = curr[target - coins[ind]]
                    if res != float('inf'):
                        take = 1 + res
                curr[target] = min(take, not_take)
            prev = curr
            
        ans = prev[amount]
        return ans if ans != float('inf') else -1