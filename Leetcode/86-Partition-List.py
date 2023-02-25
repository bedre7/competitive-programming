# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessers = None
        lessersLast = None
        greaters = None
        greatersLast = None
        temp = head
        
        while temp:
            if temp.val < x:
                if not lessers:
                    lessers = ListNode(temp.val)
                    lessersLast = lessers
                else:
                    lessersLast.next = ListNode(temp.val)
                    lessersLast = lessersLast.next
            else:
                if not greaters:
                    greaters = ListNode(temp.val)
                    greatersLast = greaters
                else:
                    greatersLast.next = ListNode(temp.val)
                    greatersLast = greatersLast.next
        
            temp = temp.next
        
        if lessersLast:
            lessersLast.next = greaters
        
        return lessers if lessers else greaters