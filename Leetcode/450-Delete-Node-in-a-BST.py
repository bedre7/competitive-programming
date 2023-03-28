# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None: return root
        elif root.val == key:
            return self.remove(root)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
    
    def remove(self, root):
        if not root.right:
            return root.left
        if not root.left:
            return root.right
        if root.left and root.right:
            parent = rightChild = root.left
            while rightChild.right:
                parent = rightChild
                rightChild = rightChild.right
            root.val = rightChild.val
            if parent == rightChild:
                root.left = rightChild.left
            else:
                parent.right = self.remove(rightChild)
            
        return root