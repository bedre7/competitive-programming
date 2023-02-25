# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left = list1
        right = list2
        
        mergedHead = mergedTail = None
        
        while left and right:
            toAppend = None
            if left.val <= right.val:
                toAppend = left.val
                left = left.next
            else:
                toAppend = right.val
                right = right.next

            if mergedTail:
                mergedTail.next = ListNode(toAppend)
                mergedTail = mergedTail.next
            else:
                mergedHead = ListNode(toAppend)
                mergedTail = mergedHead
        
        while left:
            if mergedTail:
                mergedTail.next = ListNode(left.val)
                mergedTail = mergedTail.next
            else:
                mergedHead = ListNode(left.val)
                mergedTail = mergedHead
            left = left.next
        
        while right:
            if mergedTail:
                mergedTail.next = ListNode(right.val)
                mergedTail = mergedTail.next
            else:
                mergedHead = ListNode(right.val)
                mergedTail = mergedHead
            right = right.next
    
        return mergedHead
            