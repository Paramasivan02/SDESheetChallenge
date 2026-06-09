class Solution:
    def maxLen(self, n: int, arr: list[int]) -> int:
        sum_map = {}
        max_length = 0
        prefix_sum = 0
        
        for i in range(n):
            prefix_sum += arr[i]
            
            if prefix_sum == 0:
                max_length = i + 1
                
            elif prefix_sum in sum_map:
                current_length = i - sum_map[prefix_sum]
                max_length = max(max_length, current_length)
                
            else:
                sum_map[prefix_sum] = i
                
        return max_length