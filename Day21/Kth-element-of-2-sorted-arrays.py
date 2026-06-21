class Solution:
    def kthElement(self, a: list[int], b: list[int], k: int) -> int:
        if len(a) > len(b):
            a, b = b, a
            
        m, n = len(a), len(b)
        
        low = max(0, k - n)
        high = min(m, k)
        
        while low <= high:
            partition1 = (low + high) // 2
            
            partition2 = k - partition1
            
            maxLeft1 = float('-inf') if partition1 == 0 else a[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else a[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else b[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else b[partition2]
            
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                return max(maxLeft1, maxLeft2)
                
            elif maxLeft1 > minRight2:
                high = partition1 - 1
            else:
                low = partition1 + 1
                
        return -1