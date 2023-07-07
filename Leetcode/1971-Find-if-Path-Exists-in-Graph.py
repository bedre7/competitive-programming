class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Union find
        par = [i for i in range(n)]
        rank = [1] * n
        def find(v):
            p = par[v]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
            
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv: return
            if rank[pu] > rank[pv]:
                par[pv] = pu
                rank[pu] += rank[pv]
            else:
                par[pu] = pv
                rank[pv] += rank[pu]
        
        for u, v in edges:
            union(u, v)
        
        return find(source) == find(destination)

        # graph = collections.defaultdict(list)
        # for u, v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)
        
        # visited = set()
        # DFS
        # def dfs(current):
        #     nonlocal visited, found
        #     if current == destination:
        #         return True
            
        #     visited.add(current)
        #     for child in graph[current]:
        #         if child not in visited:
        #             if dfs(child): return True
            
        #     return False
        
        # return dfs(source)
        # return found
        
        # TLE
        # seen = [False] * n
        # queue = collections.deque([source])
        # seen[source] = True
        # while queue:
        #     child = queue.popleft()
        #     if child == destination:
        #         return True
        #     for c in graph[child]:
        #         if not seen[c]:
        #             seen[c] = True
        #             queue.append(c)
        
        # return False