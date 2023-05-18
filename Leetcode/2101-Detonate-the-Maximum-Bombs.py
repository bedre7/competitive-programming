from collections import defaultdict
import math
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        maxBombs = currBombs = 0
        graph = defaultdict(list)
        count = defaultdict(int)
        
        for x, y, r in bombs:
            count[(x, y)] += 1
        
        def distance(x1, y1, x2, y2):
            return math.sqrt(pow(x2 - x1, 2) + pow(y1 - y2, 2))

        for i in range(n):
            x1, y1, r1 = bombs[i]
           
            for j in range(i + 1, n):
                x2, y2, r2 = bombs[j]
                dist = distance(x1, y1, x2, y2)
                if dist <= r1: graph[(x1, y1)].append((x2, y2))
                if dist <= r2: graph[(x2, y2)].append((x1, y1))
        
        visited = set()
        def dfs(x, y):
            nonlocal visited, currBombs
            currBombs += count[x, y]

            for cx, cy in graph[(x, y)]:
                if (cx, cy) not in visited:
                    visited.add((cx, cy))
                    dfs(cx, cy)
                
        for x, y, r in bombs:
            visited.add((x, y))
            currBombs = 0
            dfs(x, y)
            maxBombs = max(maxBombs, currBombs)
            visited.clear()
            
        return maxBombs
            