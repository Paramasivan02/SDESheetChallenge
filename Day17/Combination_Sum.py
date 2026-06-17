class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        n = len(candidates)
        
        def backtrack(index: int, current_target: int, current_combination: list[int]):
            if current_target == 0:
                result.append(list(current_combination))
                return
            if index == n:
                return
            
            if candidates[index] <= current_target:
                current_combination.append(candidates[index])
                backtrack(index, current_target - candidates[index], current_combination)
                current_combination.pop()  
            
            backtrack(index + 1, current_target, current_combination)

        backtrack(0, target, [])
        return result