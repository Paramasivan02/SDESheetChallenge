class Solution:
    def solve(self, n: int, k: int, stalls: list[int]) -> int:
        stalls.sort()
        
        def can_place_cows(dist: int) -> bool:
            cows_placed = 1
            last_position = stalls[0]
            
            for i in range(1, n):
                if stalls[i] - last_position >= dist:
                    cows_placed += 1
                    last_position = stalls[i]
                    
                if cows_placed >= k:
                    return True
                    
            return False

        low = 1 
        high = stalls[-1] - stalls[0] 
        result = 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if can_place_cows(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return result