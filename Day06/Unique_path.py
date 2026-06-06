class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total_steps = m + n - 2
        
        r = m - 1
        
        res = 1
        for i in range(1, r + 1):
            res = res * (total_steps - r + i) // i
            
        return res