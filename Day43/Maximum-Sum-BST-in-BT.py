class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSumBST(self, root: 'TreeNode') -> int:
        self.max_sum = 0
        
        def post_order_traverse(node: 'TreeNode') -> tuple:
            if not node:
                return (True, float('inf'), float('-inf'), 0)
                
            left_is_bst, left_min, left_max, left_sum = post_order_traverse(node.left)
            right_is_bst, right_min, right_max, right_sum = post_order_traverse(node.right)
            
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                
                current_sum = left_sum + right_sum + node.val
                
                self.max_sum = max(self.max_sum, current_sum)
                
                return (True, min(left_min, node.val), max(right_max, node.val), current_sum)
                
            return (False, float('-inf'), float('inf'), 0)
            
        post_order_traverse(root)
        
        return self.max_sum