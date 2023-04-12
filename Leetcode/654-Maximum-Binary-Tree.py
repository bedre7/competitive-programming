# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def makeMaxTree(left, right):
            if left > right: return None
            root = max(nums[left:right + 1])
            rootIndex = nums.index(root)
            rootNode = TreeNode(root)
            
            rootNode.left = makeMaxTree(left, rootIndex - 1)
            rootNode.right = makeMaxTree(rootIndex + 1, right)
            
            return rootNode
        
        return makeMaxTree(0, len(nums) - 1)