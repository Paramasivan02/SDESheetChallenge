class Solution:
    def mergeAndCount(self, arr: list[int], temp_arr: list[int], left: int, mid: int, right: int) -> int:
        i = left
        j = mid + 1
        k = left
        inv_count = 0

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1

        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1

        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        for loop_var in range(left, right + 1):
            arr[loop_var] = temp_arr[loop_var]

        return inv_count

    def mergeSortAndCount(self, arr: list[int], temp_arr: list[int], left: int, right: int) -> int:
        inv_count = 0
        if left < right:
            mid = (left + right) // 2

            inv_count += self.mergeSortAndCount(arr, temp_arr, left, mid)
            inv_count += self.mergeSortAndCount(arr, temp_arr, mid + 1, right)
            inv_count += self.mergeAndCount(arr, temp_arr, left, mid, right)

        return inv_count

    def inversionCount(self, arr: list[int]) -> int:
        n = len(arr)
        temp_arr = [0] * n
        return self.mergeSortAndCount(arr, temp_arr, 0, n - 1)