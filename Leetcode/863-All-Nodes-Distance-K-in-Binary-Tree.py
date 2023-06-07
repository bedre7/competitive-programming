# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def makeGraph(curr, parent):
            if not curr: return
            if parent:
                graph[curr.val].append(parent.val)
                graph[parent.val].append(curr.val)
            makeGraph(curr.left, curr)
            makeGraph(curr.right, curr)
        
        makeGraph(root, None)
        visited = set([target.val])
        output = []
        
        def dfs(curr, dist):
            if dist == k: 
                output.append(curr)
                return 
            
            for nei in graph[curr]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei, dist + 1)
        
        dfs(target.val, 0)
        return output