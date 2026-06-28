import collections

class Solution:
    def maxSlidingWindow(self, arr: list[int], k: int) -> list[int]:
        if not arr or k == 0:
            return []
            
        n = len(arr)
        result = []
        
        dq = collections.deque()
        
        for i in range(n):
            if dq and dq[0] < i - k + 1:
                dq.popleft()
                
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
                
            dq.append(i)
            
            if i >= k - 1:
                result.append(arr[dq[0]])
                
        return result