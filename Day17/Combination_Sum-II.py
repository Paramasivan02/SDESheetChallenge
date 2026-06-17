class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        n = len(candidates)
        
        def backtrack(index: int, current_target: int, current_combination: list[int]):
            if current_target == 0:
                result.append(list(current_combination))
                return
            
            for i in range(index, n):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > current_target:
                    break
                
                current_combination.append(candidates[i])
                
                backtrack(i + 1, current_target - candidates[i], current_combination)
                
                current_combination.pop()
                
        backtrack(0, target, [])
        return result       