# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head, k: int):
        if head is None or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        
        curr = head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
            
        prev = dummy
        curr = dummy
        next_node = dummy
        
        while count >= k:
            curr = prev.next       
            next_node = curr.next 
            
            for _ in range(1, k):
                curr.next = next_node.next     
                next_node.next = prev.next     
                prev.next = next_node          
                next_node = curr.next                         
            
            prev = curr
            count -= k
            
        return dummy.next