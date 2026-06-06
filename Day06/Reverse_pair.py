class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def mergeSort(low: int, high: int) -> int:
            if low >= high:
                return 0
            
            mid = (low + high) // 2
            
            inv_count = mergeSort(low, mid)
            inv_count += mergeSort(mid + 1, high)
            inv_count += countPairs(low, mid, high)
            
            merge(low, mid, high)
            
            return inv_count

        def countPairs(low: int, mid: int, high: int) -> int:
            count = 0
            right = mid + 1
            
            for i in range(low, mid + 1):
                while right <= high and nums[i] > 2 * nums[right]:
                    right += 1
                count += (right - (mid + 1))
                
            return count

        def merge(low: int, mid: int, high: int):
            temp = []
            left = low
            right = mid + 1

            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1

            while left <= mid:
                temp.append(nums[left])
                left += 1

            while right <= high:
                temp.append(nums[right])
                right += 1

            for i in range(low, high + 1):
                nums[i] = temp[i - low]

        return mergeSort(0, len(nums) - 1)