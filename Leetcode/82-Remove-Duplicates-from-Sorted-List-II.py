# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        newHead = ListNode(0)
        tail = newHead
        temp = head
        while temp:
            found = False
            while temp and temp.next and temp.val == temp.next.val:
                temp = temp.next
                found = True
            
            if not found:
                tail.next = temp
                tail = tail.next
                
            temp = temp.next
            
        tail.next = None
        
        return newHead.next