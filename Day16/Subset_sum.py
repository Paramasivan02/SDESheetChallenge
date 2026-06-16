class Solution:
    def subsetSums(self, arr: list[int], N: int) -> list[int]:
        res = []
        
        def calculate_sum(ind: int, current_sum: int):
            if ind == N:
                res.append(current_sum)
                return
            
            calculate_sum(ind + 1, current_sum + arr[ind])
            
            calculate_sum(ind + 1, current_sum)
            
        calculate_sum(0, 0)
        res.sort()  
        return res


