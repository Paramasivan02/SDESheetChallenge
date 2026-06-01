class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        if n <= 1:
            return

        break_point = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break_point = i
                break

        if break_point == -1:
            nums.reverse()
            return

        for i in range(n - 1, break_point, -1):
            if nums[i] > nums[break_point]:
                nums[break_point], nums[i] = nums[i], nums[break_point]
                break

        left, right = break_point + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1