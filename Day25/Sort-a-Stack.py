class Solution:
    def sortStack(self, stack: list[int]) -> None:
        if not stack:
            return
            
        top_element = stack.pop()
        
        self.sortStack(stack)
        
        self.insertSorted(stack, top_element)
        
    def insertSorted(self, stack: list[int], element: int) -> None:
        if not stack or stack[-1] <= element:
            stack.append(element)
            return
            
        temp = stack.pop()
        
        self.insertSorted(stack, element)
        
        stack.append(temp)