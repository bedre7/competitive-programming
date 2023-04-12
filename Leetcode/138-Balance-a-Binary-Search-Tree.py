# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        tree = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            tree.append(node.val)
            inorder(node.right)
            
        inorder(root)
        def makeTree(left, right):
            if left > right: return None
            mid = (left + right) // 2
            midNode = TreeNode(tree[mid])
            midNode.left = makeTree(left, mid - 1)
            midNode.right = makeTree(mid + 1, right)
            
            return midNode
        
        return makeTree(0, len(tree) - 1)