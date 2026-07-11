class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> 'TreeNode':
        i = [0]
        
        def build(upper_bound: float) -> 'TreeNode':
            if i[0] == len(preorder):
                return None
                
            if preorder[i[0]] > upper_bound:
                return None
                
            root_val = preorder[i[0]]
            root = TreeNode(root_val)
            
            i[0] += 1
            
            root.left = build(root_val)
            
            root.right = build(upper_bound)
            
            return root
            
        return build(float('inf'))