class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: 'TreeNode', is_reverse: bool):
        self.stack = []
        self.reverse = is_reverse
        self._push_all(root)
        
    def next(self) -> int:
        node = self.stack.pop()
        
        if not self.reverse:
            self._push_all(node.right)
        else:
            self._push_all(node.left)
            
        return node.val
        
    def _push_all(self, node: 'TreeNode') -> None:
        while node:
            self.stack.append(node)
            if not self.reverse:
                node = node.left
            else:
                node = node.right

class Solution:
    def findTarget(self, root: 'TreeNode', k: int) -> bool:
        if not root:
            return False
            
        left_iter = BSTIterator(root, False) 
        right_iter = BSTIterator(root, True)  
        
        i = left_iter.next()
        j = right_iter.next()
        
        while i < j:
            current_sum = i + j
            
            if current_sum == k:
                return True
            elif current_sum < k:
                i = left_iter.next()
            else:
                j = right_iter.next()
                
        return False