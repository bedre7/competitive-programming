# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(current):
            if not current:
                return ''
            
            currentStr = str(current.val)
            if current.left:
                currentStr += '(' + dfs(current.left) + ')'
            if not current.left and current.right: currentStr += '()'
            if current.right:
                currentStr += '(' + dfs(current.right) + ')'
            
            return currentStr
        
        return dfs(root)