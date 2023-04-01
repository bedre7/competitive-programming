# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def countAndSum(root, summ, count):
            if not root: return [0, count]
            leftSum = rightSum = 0
            if root.left:
                leftSum, count = countAndSum(root.left, summ + root.left.val, count + 1)
            if root.right:
                rightSum, count = countAndSum(root.right, summ + root.right.val, count + 1)
            
            return [leftSum + rightSum + root.val, count]
        
        stack = [root]
        equals = 0
        while stack:
            node = stack.pop()
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
            summ, count = countAndSum(node, node.val, 1)
            if summ // count == node.val:
                equals += 1
        
        return equals