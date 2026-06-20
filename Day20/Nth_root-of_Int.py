class Solution:
    def NthRoot(self, n: int, m: int) -> int:
        def check_power(mid: int, n: int, m: int) -> int:
            ans = 1
            for _ in range(n):
                ans *= mid
                if ans > m:
                    return 2
            
            if ans == m:
                return 1
            return 0

        low = 1
        high = m
        
        while low <= high:
            mid = (low + high) // 2
            
            val = check_power(mid, n, m)
            
            if val == 1:
                return mid  
            elif val == 0:
                low = mid + 1 
            else:
                high = mid - 1 
                
        
        return -1