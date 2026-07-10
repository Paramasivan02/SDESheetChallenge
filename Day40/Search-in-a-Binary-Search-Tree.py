class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: 'TreeNode', val: int) -> 'TreeNode':
        curr = root
        
        while curr and curr.val != val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
                
        return curr