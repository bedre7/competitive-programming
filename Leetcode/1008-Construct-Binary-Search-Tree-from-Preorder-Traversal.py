# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def insert(node, val):
            if not node: return TreeNode(val)
            elif node.val < val:
                node.right = insert(node.right, val)
            elif node.val > val:
                node.left = insert(node.left, val)
            return node
        root = None
        for val in preorder:
            root = insert(root, val)
        
        return root