class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
            
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
                
        actual_count1 = 0
        actual_count2 = 0
        
        for num in nums:
            if num == cand1:
                actual_count1 += 1
            elif num == cand2:
                actual_count2 += 1
                
        result = []
        n = len(nums)
        
        if actual_count1 > n // 3:
            result.append(cand1)
        if actual_count2 > n // 3:
            result.append(cand2)
            
        return result