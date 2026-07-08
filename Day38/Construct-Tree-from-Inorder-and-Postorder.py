class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> 'TreeNode':
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(post_start: int, post_end: int, in_start: int, in_end: int) -> 'TreeNode':
            if post_start > post_end or in_start > in_end:
                return None
                
            root_val = postorder[post_end]
            root = TreeNode(root_val)
            
            in_root_idx = inorder_map[root_val]
            
            nums_left = in_root_idx - in_start
            
            root.left = build(post_start, post_start + nums_left - 1, in_start, in_root_idx - 1)
            
            root.right = build(post_start + nums_left, post_end - 1, in_root_idx + 1, in_end)
            
            return root
            
        return build(0, len(postorder) - 1, 0, len(inorder) - 1)