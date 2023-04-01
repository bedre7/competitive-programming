# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        def dfs(root):
            if not root: return 0

            stack = [(root, root.val)]
            count = 0
            while stack:
                node, total = stack.pop()
                if node.right: stack.append((node.right, total + node.right.val))
                if node.left: stack.append((node.left, total + node.left.val))
                if total == targetSum:
                    count += 1
                    
            return count
        
        stack = [root]
        count = 0
        while stack:
            node = stack.pop()
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
            count += dfs(node)
        
        return count