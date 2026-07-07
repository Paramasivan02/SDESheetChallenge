class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printBoundary(self, root: 'TreeNode') -> list[int]:
        if not root:
            return []
            
        res = []
        
        def isLeaf(node):
            return not node.left and not node.right
            
        if not isLeaf(root):
            res.append(root.val)
            
        def addLeftBoundary(node):
            curr = node.left
            while curr:
                if not isLeaf(curr):
                    res.append(curr.val)
                if curr.left:
                    curr = curr.left
                else:
                    curr = curr.right
                    
        def addRightBoundary(node):
            curr = node.right
            temp = []
            while curr:
                if not isLeaf(curr):
                    temp.append(curr.val)
                if curr.right:
                    curr = curr.right
                else:
                    curr = curr.left
            
            for i in range(len(temp) - 1, -1, -1):
                res.append(temp[i])
                
        def addLeaves(node):
            if not node:
                return
            if isLeaf(node):
                res.append(node.val)
                return
            addLeaves(node.left)
            addLeaves(node.right)
            
        addLeftBoundary(root)
        addLeaves(root)
        addRightBoundary(root)
        
        return res