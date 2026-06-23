import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        
        min_heap = []
        
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        result = [num for freq, num in min_heap]
        
        return result