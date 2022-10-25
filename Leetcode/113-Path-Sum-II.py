# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        stack = [(root, root.val, [root.val])]
        paths = []
        
        while stack:
            cur, total, path = stack.pop()
            if not cur.left and not cur.right:
                if total == targetSum:
                    paths.append(path)
                else:
                    path.pop()
                    total -= cur.val
            if cur.right:
                rightPath = path.copy()
                rightPath.append(cur.right.val)
                stack.append((cur.right, total + cur.right.val, rightPath))
            if cur.left:
                leftPath = path.copy()
                leftPath.append(cur.left.val)
                stack.append((cur.left, total + cur.left.val, leftPath))
                    
        return paths