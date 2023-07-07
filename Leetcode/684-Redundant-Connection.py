class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union Find
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        def find(u):
            p = par[u]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv: return False
            if rank[pu] > rank[pv]:
                par[pv] = pu
                rank[pu] += rank[pv]
            else:
                par[pu] = pv
                rank[pv] += rank[pu]
            return True
        
        for u, v in edges:
            if not union(u, v): return [u, v]
        
        # DFS
        # visited = set()
        # graph = defaultdict(list)
        
        # def dfs(curr, target):
        #     if curr == target: return True
        #     visited.add(curr)

        #     for n in graph[curr]:
        #         if n not in visited:
        #             if dfs(n, target): return True
        #     return False
            
        # for u, v in edges:
        #     visited.clear()
        #     if dfs(u, v):
        #         return [u, v]
        #     graph[u].append(v)
        #     graph[v].append(u)