from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root: 'TreeNode') -> str:
        if not root:
            return ""
            
        result = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("#")
                
        return ",".join(result)

    def deserialize(self, data: str) -> 'TreeNode':
        if not data:
            return None
            
        values = data.split(",")
        
        root = TreeNode(int(values[0]))
        queue = deque([root])
        
        i = 1
        
        while queue and i < len(values):
            parent = queue.popleft()
            
            if values[i] != "#":
                left_child = TreeNode(int(values[i]))
                parent.left = left_child
                queue.append(left_child)
            i += 1
            
            if i < len(values) and values[i] != "#":
                right_child = TreeNode(int(values[i]))
                parent.right = right_child
                queue.append(right_child)
            i += 1
            
        return root