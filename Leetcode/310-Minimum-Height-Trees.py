class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        level = deque()
        for node in range(n):
            if degree[node] == 1: level.append(node)
        
        nodes = set([node for node in range(n)])
        while len(nodes) > 2:
            nodes -= nodes.intersection(set(level))
            nextLevel = deque()
            for curr in level:
                for node in adj[curr]:
                    if node in nodes:
                        degree[node] -= 1
                        if degree[node] == 1:
                            nextLevel.append(node)
            level = nextLevel
        
        return nodes