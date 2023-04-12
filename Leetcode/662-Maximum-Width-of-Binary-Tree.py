# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = collections.deque()
        queue.append([root, 0])
        maxWidth = 0
        
        while queue:
            maxIndex = float('-inf')
            minIndex = float('inf')
            for _ in range(len(queue)):
                node, index = queue.popleft()
                maxIndex = max(maxIndex, index)
                minIndex = min(minIndex, index)
                maxWidth = max(maxWidth, maxIndex - minIndex + 1)
                if node.left: queue.append([node.left, 2 * index + 1])
                if node.right: queue.append([node.right, 2 * index + 2])
            
        return maxWidth
