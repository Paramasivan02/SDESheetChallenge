class Solution:
    def findTwoElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        SN = (n * (n + 1)) // 2
        S2N = (n * (n + 1) * (2 * n + 1)) // 6
        
        S, S2 = 0, 0
        for num in nums:
            S += num
            S2 += num * num
            
        val1 = S - SN 
        
        val2 = S2 - S2N 
        
        val2 = val2 // val1 
        
        X = (val1 + val2) // 2
        Y = X - val1
        
        return [X, Y]