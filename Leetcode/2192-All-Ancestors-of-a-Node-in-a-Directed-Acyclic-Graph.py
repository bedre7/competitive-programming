class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = defaultdict(set)
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)

        def dfs(curr):
            if curr not in ancestors:
                ancestors[curr].add(curr)
                for nei in graph[curr]:
                    ancestors[curr] |= dfs(nei)
            
            return ancestors[curr]
        
        for node in range(n):
            dfs(node)
        
        ans = []
        for node in range(n):
            ancestors[node].remove(node)
            ans.append(sorted(ancestors[node]))
        
        return ans