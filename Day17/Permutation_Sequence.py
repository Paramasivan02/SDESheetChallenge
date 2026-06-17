class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = []
        fact = 1
        
        for i in range(1, n):
            fact *= i
            numbers.append(i)
        numbers.append(n)
        
        k -= 1
        result = []
        
        while True:
            idx = k // fact
            result.append(str(numbers[idx]))
            
            numbers.pop(idx)
            
            if not numbers:
                break
                
            k %= fact
            fact //= len(numbers)
            
        return "".join(result)