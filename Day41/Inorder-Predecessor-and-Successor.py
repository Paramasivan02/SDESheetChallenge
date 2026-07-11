class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderPredecessorSuccessor(self, root: 'TreeNode', key: int) -> tuple['TreeNode', 'TreeNode']:
        predecessor = None
        successor = None
        
        curr = root
        while curr:
            if curr.val > key:
                successor = curr
                curr = curr.left
            else:
                curr = curr.right
                
        curr = root
        while curr:
            if curr.val < key:
                predecessor = curr
                curr = curr.right
            else:
                curr = curr.left
                
        return predecessor, successor