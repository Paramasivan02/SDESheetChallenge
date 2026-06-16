class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        
        def backtrack(index: int, current_subset: list[int]):
            result.append(list(current_subset))
            
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                
                current_subset.append(nums[i])
                
                backtrack(i + 1, current_subset)
                
                current_subset.pop()
                
        backtrack(0, [])
        return result