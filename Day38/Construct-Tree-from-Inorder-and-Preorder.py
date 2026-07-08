class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> 'TreeNode':
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(pre_start: int, pre_end: int, in_start: int, in_end: int) -> 'TreeNode':
            if pre_start > pre_end or in_start > in_end:
                return None
                
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            in_root_idx = inorder_map[root_val]
            
            nums_left = in_root_idx - in_start
            
            root.left = build(pre_start + 1, pre_start + nums_left, in_start, in_root_idx - 1)
            
            root.right = build(pre_start + nums_left + 1, pre_end, in_root_idx + 1, in_end)
            
            return root
            
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)