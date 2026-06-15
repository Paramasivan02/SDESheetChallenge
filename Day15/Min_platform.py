class Solution:
    def findPlatform(self, n: int, arr: list[int], dep: list[int]) -> int:
        arr.sort()
        dep.sort()
        
        i = 1  
        j = 0
        
        platforms_needed = 1
        max_platforms = 1
        
        while i < n and j < n:
            if arr[i] <= dep[j]:
                platforms_needed += 1  
                i += 1
            else:
                platforms_needed -= 1  
                j += 1
                
            if platforms_needed > max_platforms:
                max_platforms = platforms_needed
                
        return max_platforms