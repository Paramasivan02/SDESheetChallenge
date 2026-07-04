from collections import deque

class Solution:
    def topView(self, root) -> list[int]:
        if not root:
            return []
            
        hd_node_map = {}
        
        queue = deque([(root, 0)])
        
        min_hd = 0
        max_hd = 0
        
        while queue:
            node, hd = queue.popleft()
            
            if hd not in hd_node_map:
                hd_node_map[hd] = node.val
            
            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)
            
            if node.left:
                queue.append((node.left, hd - 1))
                
            if node.right:
                queue.append((node.right, hd + 1))
                
        result = [hd_node_map[hd] for hd in range(min_hd, max_hd + 1)]
        
        return result