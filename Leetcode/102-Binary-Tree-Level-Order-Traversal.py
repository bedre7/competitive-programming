# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        
        queue = deque([root])
        levelorder = []
        
        while queue:
            curr_level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:   queue.append(curr.left)
                if curr.right:  queue.append(curr.right)
                curr_level.append(curr.val)
            levelorder.append(curr_level)
        
        return levelorder