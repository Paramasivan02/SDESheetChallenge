class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallestLargest(self, root: 'TreeNode', k: int) -> list[int]:
        ans = [-1, -1]
        
        count_small = [0]
        count_large = [0]
        
        def find_kth_smallest(node: 'TreeNode'):
            if not node or count_small[0] >= k:
                return
                
            find_kth_smallest(node.left)
            
            count_small[0] += 1
            if count_small[0] == k:
                ans[0] = node.val
                return  
                
            find_kth_smallest(node.right)
            
        def find_kth_largest(node: 'TreeNode'):
            if not node or count_large[0] >= k:
                return
                
            find_kth_largest(node.right)
            
            count_large[0] += 1
            if count_large[0] == k:
                ans[1] = node.val
                return  
                
            find_kth_largest(node.left)
            
        find_kth_smallest(root)
        find_kth_largest(root)
        
        return ans