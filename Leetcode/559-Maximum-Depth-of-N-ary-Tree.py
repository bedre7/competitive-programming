"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        maxdepth = 0
        def dfs(current, depth=1):
            nonlocal maxdepth
            maxdepth = max(maxdepth, depth)
            
            for child in current.children:
                dfs(child, depth + 1)
            
        dfs(root)
        return maxdepth