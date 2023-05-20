class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        visited = set()
        n = len(graph)
        paths = []
        
        def dfs(current, path):
            if current == n - 1:
                visited.clear()
                paths.append(path.copy())
                return
            
            for v in graph[current]:
                if v not in visited:
                    visited.add(v)
                    path.append(v)
                    dfs(v, path)
                    path.pop()
        
        for u in graph[0]:
            path = [0, u]
            visited.add(u)
            dfs(u, path)
        
        return paths
        
