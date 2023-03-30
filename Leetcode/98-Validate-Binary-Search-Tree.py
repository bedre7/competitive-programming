# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float('-inf'), float('inf'))
    def isValid(self, root, minimum, maximum):
        if not root: return True
        
        if root.val <= minimum or root.val >= maximum:
            return False
        
        leftIsValid = self.isValid(root.left, minimum, root.val)
        rightIsValid = self.isValid(root.right, root.val, maximum)
        
        return leftIsValid and rightIsValid