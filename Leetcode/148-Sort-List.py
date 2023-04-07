# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMid(self, head):
        if not head or not head.next: return head
        slow = head
        fast = slow.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        first = head
        mid = self.getMid(head)
        second = mid.next
        mid.next = None
        
        first = self.sortList(first)
        second = self.sortList(second)
        
        return self.merge(first, second)

    def merge(self, first, second):
        merged = ListNode()
        tail = merged
        left = first
        right = second
        
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        if left: tail.next = left
        if right: tail.next = right
            
        return merged.next
        