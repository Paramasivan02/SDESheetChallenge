class Solution:
    def distinctNumbers(self, nums: list[int], k: int) -> list[int]:
        if not nums or k == 0:
            return []
            
        freq_map = {}
        ans = []
        
        for i in range(k):
            freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1
            
        ans.append(len(freq_map))
        
        for i in range(k, len(nums)):
            left_element = nums[i - k]
            freq_map[left_element] -= 1
            
            if freq_map[left_element] == 0:
                del freq_map[left_element]
                
            right_element = nums[i]
            freq_map[right_element] = freq_map.get(right_element, 0) + 1
            
            ans.append(len(freq_map))
            
        return ans