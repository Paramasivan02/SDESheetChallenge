# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, root, target: int) -> list[int]:
        path = []
        
        def getPath(node, target) -> bool:
            if not node:
                return False
                
            path.append(node.val)
            
            if node.val == target:
                return True
                
            if getPath(node.left, target) or getPath(node.right, target):
                return True
                
            path.pop()
            
            return False
            
        getPath(root, target)
        
        return path