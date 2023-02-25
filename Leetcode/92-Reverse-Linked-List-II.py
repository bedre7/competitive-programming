# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pre = None
        temp = head
        start = head
        post = start.next
        
        for _ in range(left - 1):
            if not pre: pre = head
            else:
                pre = pre.next
        start = pre.next if pre else head
        subHead = start
        post = start.next if start else None
        
        for _ in range(right - left):
            postNext = post.next if post else None
            if post: post.next = start
            start = post
            post = postNext

        if subHead: subHead.next = post if post else None
        if pre: pre.next = start
        
        return head if left != 1 else start