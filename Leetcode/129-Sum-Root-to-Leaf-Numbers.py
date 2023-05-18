# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        
        def dfs(current, path):
            nonlocal total
            if not current.left and not current.right:
                total += int(''.join(path))
                return
            
            if current.left:
                path.append(str(current.left.val))
                dfs(current.left, path)
                path.pop()
            if current.right:
                path.append(str(current.right.val))
                dfs(current.right, path)
                path.pop()
        
        dfs(root, [str(root.val)])
        return total

        #Iteratively
#         stack = [(root, [str(root.val)])]
#         total = 0
#         while stack:
#             node, path = stack.pop()
#             if node.left:
#                 leftPath = path.copy()
#                 leftPath.append(str(node.left.val))
#                 stack.append((node.left, leftPath))
#             if node.right:
#                 rightPath = path.copy()
#                 rightPath.append(str(node.right.val))
#                 stack.append((node.right, rightPath))
#             if not node.left and not node.right:
#                 total += int(''.join(path))
#                 path.pop()
        
#         return total