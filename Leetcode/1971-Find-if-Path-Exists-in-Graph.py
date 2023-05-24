class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # visited = set()
        # def dfs(current):
        #     if current == destination:
        #         return True
            
        #     visited.add(current)
        #     for child in graph[current]:
        #         if child not in visited:
        #             if dfs(child): return True
            
        #     return False
        
        # return dfs(source)
        
        # TLE
        seen = [False] * n
        queue = deque([source])
        seen[source] = True
        while queue:
            child = queue.popleft()
            if child == destination:
                return True
            for c in graph[child]:
                if not seen[c]:
                    seen[c] = True
                    queue.append(c)
        
        return False