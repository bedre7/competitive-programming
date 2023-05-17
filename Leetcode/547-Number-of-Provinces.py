class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        n = len(isConnected)
        visited = set()
        
        def dfs(current):
            nonlocal visited
            
            for child in range(n):
                if (isConnected[current][child] == 1 and
                    current != child and child not in visited):
                    visited.add(child)
                    dfs(child)
        
        for v in range(n):
            if v not in visited:
                provinces += 1
                dfs(v)
        
        return provinces
                