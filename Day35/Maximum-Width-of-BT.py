from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root) -> int:
        if not root:
            return 0
            
        max_width = 0
        
        queue = deque([(root, 0)])
        
        while queue:
            level_length = len(queue)
            
            min_index = queue[0][1]
            
            first_index = 0
            last_index = 0
            
            for i in range(level_length):
                node, current_index = queue.popleft()
                
                normalized_index = current_index - min_index
                
                if i == 0:
                    first_index = normalized_index
                    
                if i == level_length - 1:
                    last_index = normalized_index
                    
                if node.left:
                    queue.append((node.left, 2 * normalized_index + 1))
                    
                if node.right:
                    queue.append((node.right, 2 * normalized_index + 2))
                    
            current_width = last_index - first_index + 1
            max_width = max(max_width, current_width)
            
        return max_width