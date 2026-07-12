class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def floorAndCeil(self, root: 'TreeNode', key: int) -> list[int]:
        floor_val = -1
        ceil_val = -1
        
        curr = root
        while curr:
            if curr.val == key:
                floor_val = curr.val
                break  
            elif curr.val > key:
                curr = curr.left
            else:
                floor_val = curr.val
                curr = curr.right
                
        curr = root
        while curr:
            if curr.val == key:
                ceil_val = curr.val
                break  
            elif curr.val < key:
                curr = curr.right
            else:
                ceil_val = curr.val
                curr = curr.left
                
        return [floor_val, ceil_val]