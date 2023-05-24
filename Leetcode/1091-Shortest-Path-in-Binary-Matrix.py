from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1: return -1

        queue = deque([(0, 0)])
        prev = defaultdict(lambda : (-1, -1))
        dirs = [(0, 1),(1, 0),(-1, 0),(0, -1),(1, 1),(-1, -1),(1, -1),(-1, 1)]
        visited = set()
        visited.add((0, 0))
        
        def trace(x, y):
            count = 1
            while prev[(x, y)] != (-1, -1):
                x, y = prev[(x, y)]
                count += 1
            
            return count

        while queue:
            x, y = queue.popleft()
            if x == n - 1 and y == n - 1: return trace(x, y)
            for dx, dy in dirs:
                a, b = x + dx, y + dy
                if (0 <= a < n and 0 <= b < n and
                   (a, b) not in visited and grid[a][b] == 0):
                    prev[(a, b)] = (x, y)
                    queue.append((a, b))
                    visited.add((a, b))
        
        return -1
