# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:      
        def merge(first, second):
            merged = tail = ListNode()
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
        
        def mergeK(left, right):
            if left > right: return None
            if left == right: return lists[left]
            mid = (left + right) // 2
            midNode = lists[mid]
            
            left = mergeK(left, mid - 1)
            right = mergeK(mid + 1, right)
            
            return merge(midNode, merge(left, right))
        
        return mergeK(0, len(lists) - 1)