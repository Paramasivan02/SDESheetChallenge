# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preInPostTraversal(self, root) -> list[list[int]]:
        preorder = []
        inorder = []
        postorder = []
        
        if not root:
            return [preorder, inorder, postorder]
            
        stack = [[root, 1]]
        
        while stack:
            node, state = stack[-1]
            
            if state == 1:
                preorder.append(node.val)
                stack[-1][1] = 2
                if node.left:
                    stack.append([node.left, 1])
                    
            elif state == 2:
                inorder.append(node.val)
                stack[-1][1] = 3
                if node.right:
                    stack.append([node.right, 1])
                    
            else:
                postorder.append(node.val)
                stack.pop()
                
        return [preorder, inorder, postorder]