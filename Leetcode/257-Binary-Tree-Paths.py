# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self.rootToLeafPaths(root, [], [])
        
    def rootToLeafPaths(self, root, paths, currPath):
        if root:
            currPath.append(str(root.val))
            paths = self.rootToLeafPaths(root.left, paths, currPath)
            paths = self.rootToLeafPaths(root.right, paths, currPath)
            
            if root.left == None and root.right == None:
                paths.append('->'.join(currPath))
                
            currPath.pop()
        
        return paths