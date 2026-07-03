# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root) -> list[int]:
        if not root:
            return []
            
        stack1 = [root]
        stack2 = []
        result = []
        
        while stack1:
            curr = stack1.pop()
            stack2.append(curr)
            
            if curr.left:
                stack1.append(curr.left)
            if curr.right:
                stack1.append(curr.right)
                
        while stack2:
            result.append(stack2.pop().val)
            
        return result
