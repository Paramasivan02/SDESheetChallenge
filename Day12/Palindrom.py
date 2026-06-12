# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head) -> bool:
        if not head or not head.next:
            return True
            
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        curr = slow.next
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        left = head
        right = prev  
        
        while right is not None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True     