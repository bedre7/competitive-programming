# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return 0
        queue = collections.deque()
        queue.append([root, 0, 0])
        line = collections.defaultdict(list)
        maxWidth = 0
        
        while queue:
            node, x, y = queue.popleft()
            if node.left: queue.append([node.left, x - 1, y + 1])
            if node.right: queue.append([node.right, x + 1, y + 1])
            line[x].append([node.val, x, y])
        
        cols = collections.defaultdict(list)
        ans = []
        for k, v in sorted(line.items(), key=lambda x: x[0]):
            level = []
            for val, x, y in v:
                cols[(x, y)].append(val)
            for k, vz in sorted(cols.items(), key=lambda x: x[0]):
                level.append([c for c in sorted(vz)])
            cols.clear()
            ans.append(sum(level, []))
    
        return ans