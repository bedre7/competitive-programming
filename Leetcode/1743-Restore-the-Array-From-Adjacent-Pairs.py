class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for u, v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)
        start = None
        for num in adj:
            if len(adj[num]) == 1:
                start = num
                break
        array, visited = [], set()
        def dfs(curr):
            visited.add(curr)
            array.append(curr)
            for child in adj[curr]:
                if child not in visited:
                    dfs(child)
        
        dfs(start)
        return array