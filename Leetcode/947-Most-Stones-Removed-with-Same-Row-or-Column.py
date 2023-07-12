from collections import defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        DFS
        graph = defaultdict(list)
        for i in range(len(stones)):
            row, col = stones[i][0], stones[i][1]
            for j in range(i + 1, len(stones)):
                if stones[j][0] == row or stones[j][1] == col:
                    graph[(row, col)].append((stones[j][0], stones[j][1]))
                    graph[(stones[j][0], stones[j][1])].append((row, col))
            
        visited = set()
        def dfs(x, y):
            for cx, cy in graph[(x, y)]:
                if (cx, cy) not in visited:
                    visited.add((cx, cy))
                    dfs(cx, cy)
        
        for x, y in stones:
            if (x, y) not in visited:
                visited.add((x, y))
                dfs(x, y)
                visited.remove((x, y))
                
        return len(visited)