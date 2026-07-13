class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: 'TreeNode'):
        self.stack = []
        self._push_all(root)
        
    def has_next(self) -> bool:
        return len(self.stack) > 0
        
    def peek(self) -> int:
        return self.stack[-1].val

    def next(self) -> int:
        node = self.stack.pop()
        self._push_all(node.right)
        return node.val
        
    def _push_all(self, node: 'TreeNode') -> None:
        while node:
            self.stack.append(node)
            node = node.left

class Solution:
    def merge(self, root1: 'TreeNode', root2: 'TreeNode') -> list[int]:
        iter1 = BSTIterator(root1)
        iter2 = BSTIterator(root2)
        
        result = []
        
        while iter1.has_next() and iter2.has_next():
            if iter1.peek() < iter2.peek():
                result.append(iter1.next())
            else:
                result.append(iter2.next())
                
        while iter1.has_next():
            result.append(iter1.next())
            
        while iter2.has_next():
            result.append(iter2.next())
            
        return result