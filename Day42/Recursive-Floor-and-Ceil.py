class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def floorAndCeil(self, root: 'TreeNode', key: int) -> list[int]:
        
        def get_floor(node: 'TreeNode', current_floor: int) -> int:
            if not node:
                return current_floor
                
            if node.val == key:
                return node.val
                
            if node.val > key:
                return get_floor(node.left, current_floor)
            else:
                return get_floor(node.right, node.val)

        def get_ceil(node: 'TreeNode', current_ceil: int) -> int:
            if not node:
                return current_ceil
                
            if node.val == key:
                return node.val
                
            if node.val < key:
                return get_ceil(node.right, current_ceil)
            else:
                return get_ceil(node.left, node.val)

        return [get_floor(root, -1), get_ceil(root, -1)]