# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = right = head
        prev = None
        
        gap = 0
        while gap < n and right:
            right = right.next
            gap += 1
            
        while right:
            right = right.next
            prev = left
            left = left.next
        
        if prev:
            prev.next = left.next
        else:
            return head.next
        
        return head