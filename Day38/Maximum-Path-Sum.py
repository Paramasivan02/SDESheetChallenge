class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: 'TreeNode') -> int:
        self.global_max_sum = float('-inf')
        
        def dfs(node: 'TreeNode') -> int:
            if not node:
                return 0
                
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))
            
            current_arch_sum = node.val + left_max + right_max
            
            self.global_max_sum = max(self.global_max_sum, current_arch_sum)
            
            return node.val + max(left_max, right_max)
            
        dfs(root)
        return self.global_max_sum