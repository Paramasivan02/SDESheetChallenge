# Definition for a Node.
# class Node:
#     def __init__(self, val=0, next=None, child=None):
#         self.val = val
#         self.next = next
#         self.child = child

from yaml import Node


class Solution:
    def flatten(self, head):
        if head is None or head.next is None:
            return head
            
        flattened_right = self.flatten(head.next)
        
        head = self.merge(head, flattened_right)
        
        return head
        
    def merge(self, l1, l2):
        dummy = Node(-1)
        current = dummy
        
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                current.child = l1
                l1 = l1.child
            else:
                current.child = l2
                l2 = l2.child
            current = current.child
            
        if l1 is not None:
            current.child = l1
        else:
            current.child = l2
            
        merged_head = dummy.child
        merged_head.next = None
        
        return merged_head