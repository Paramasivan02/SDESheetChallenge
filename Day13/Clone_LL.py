from pyparsing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
         self.val = int(x)
         self.next = next
         self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        curr = head
        while curr:
            cloned_node = Node(curr.val, curr.next)
            curr.next = cloned_node
            curr = cloned_node.next 
            
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next 
            
        curr = head
        pseudo_head = Node(0)
        clone_curr = pseudo_head
        
        while curr:
            
            clone_curr.next = curr.next
            clone_curr = clone_curr.next
            curr.next = curr.next.next
            curr = curr.next
            
        return pseudo_head.next        