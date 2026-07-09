class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: 'TreeNode') -> bool:
        if not root:
            return True
            
        def isMirror(left_node: 'TreeNode', right_node: 'TreeNode') -> bool:
            if not left_node and not right_node:
                return True
                
            if not left_node or not right_node:
                return False
                
            if left_node.val != right_node.val:
                return False
                
            return isMirror(left_node.left, right_node.right) and \
                   isMirror(left_node.right, right_node.left)
                   
        return isMirror(root.left, root.right)