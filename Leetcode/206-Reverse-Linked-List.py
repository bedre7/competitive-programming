# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prevGuy = None
        
        while curr:
            nextGuy = curr.next
            curr.next = prevGuy
            prevGuy = curr
            curr = nextGuy
        
        return prevGuy