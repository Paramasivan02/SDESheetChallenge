import heapq

class Solution:
    def solve(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        n = len(nums1)
        
        nums1.sort(reverse=True)
        nums2.sort(reverse=True)
        
        max_heap = []
        heapq.heappush(max_heap, (-(nums1[0] + nums2[0]), 0, 0))
        
        visited = set()
        visited.add((0, 0))
        
        result = []
        
        for _ in range(k):
            current_sum, i, j = heapq.heappop(max_heap)
            
            result.append(-current_sum)
            
            if i + 1 < n and (i + 1, j) not in visited:
                heapq.heappush(max_heap, (-(nums1[i + 1] + nums2[j]), i + 1, j))
                visited.add((i + 1, j))
                
            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(max_heap, (-(nums1[i] + nums2[j + 1]), i, j + 1))
                visited.add((i, j + 1))
                
        return result