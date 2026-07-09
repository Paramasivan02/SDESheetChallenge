class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def changeTree(self, root: 'TreeNode') -> None:
        """
        Modifies the tree in-place to satisfy the Children Sum Property.
        Does not return anything.
        """
        if not root:
            return
            
        child_sum = 0
        if root.left:
            child_sum += root.left.val
        if root.right:
            child_sum += root.right.val
            
        if child_sum < root.val:
            if root.left:
                root.left.val = root.val
            if root.right:
                root.right.val = root.val
                
        self.changeTree(root.left)
        self.changeTree(root.right)
        
        total = 0
        if root.left:
            total += root.left.val
        if root.right:
            total += root.right.val
            
        if root.left or root.right:
            root.val = total