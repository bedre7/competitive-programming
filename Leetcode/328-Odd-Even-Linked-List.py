# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd = ListNode(0)
        oddTail = odd
        even = ListNode(0)
        evenTail = even
        isOdd = True
        temp = head
        
        while temp:
            if isOdd:
                oddTail.next = temp
                oddTail = oddTail.next
            else:
                evenTail.next = temp
                evenTail = evenTail.next

            isOdd = not isOdd
            temp = temp.next
            
        oddTail.next = even.next
        evenTail.next = None
            
        return odd.next