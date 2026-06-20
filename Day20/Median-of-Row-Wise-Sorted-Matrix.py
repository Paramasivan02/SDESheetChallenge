from bisect import bisect_right

class Solution:
    def findMedian(self, matrix: list[list[int]]) -> int:
        M = len(matrix)
        N = len(matrix[0])
        
        low = min(matrix[i][0] for i in range(M))
        high = max(matrix[i][N - 1] for i in range(M))
        
        required_count = (M * N) // 2
        
        def count_less_equal(mid: int) -> int:
            count = 0
            for row in matrix:
                count += bisect_right(row, mid)
            return count

        while low <= high:
            mid = (low + high) // 2
            
            count = count_less_equal(mid)
            
            if count <= required_count:
                low = mid + 1
            else:
                high = mid - 1
                
        return low