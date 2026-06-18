class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        n = len(nums)
        
        def backtrack(index: int):
            if index == n:
                result.append(list(nums))
                return
            
            for i in range(index, n):
                nums[index], nums[i] = nums[i], nums[index]
                
                backtrack(index + 1)
                
                nums[index], nums[i] = nums[i], nums[index]
                
        backtrack(0)
        return result