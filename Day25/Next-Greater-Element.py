class Solution:
    def nextGreaterElement(self, arr: list[int]) -> list[int]:
        n = len(arr)
        nge = [-1] * n  
        stack = [] 
        
        for i in range(n - 1, -1, -1):
            
            while stack and stack[-1] <= arr[i]:
                stack.pop()
                
            if stack:
                nge[i] = stack[-1]
                
            stack.append(arr[i])
            
        return nge