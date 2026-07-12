class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallestLargest(self, root: 'TreeNode', k: int) -> list[int]:
        ans = [-1, -1]
        
        stack = []
        curr = root
        count = 0
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
                
            curr = stack.pop()
            count += 1
            
            if count == k:
                ans[0] = curr.val
                break
                
            curr = curr.right
            
            
        stack = []
        curr = root
        count = 0
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.right
                
            curr = stack.pop()
            count += 1
            
            if count == k:
                ans[1] = curr.val
                break
                
            curr = curr.left
            
        return ans