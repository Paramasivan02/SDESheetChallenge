import heapq

class Solution:
    def mergeKSortedArrays(self, arr: list[list[int]], k: int) -> list[int]:
        min_heap = []
        
        for i in range(k):
            if len(arr[i]) > 0:
                heapq.heappush(min_heap, (arr[i][0], i, 0))
        
        result = []
        
        while min_heap:
            val, arr_idx, elem_idx = heapq.heappop(min_heap)
            result.append(val)
            
            if elem_idx + 1 < len(arr[arr_idx]):
                next_val = arr[arr_idx][elem_idx + 1]
                heapq.heappush(min_heap, (next_val, arr_idx, elem_idx + 1))
                
        return result