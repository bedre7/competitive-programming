from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        neighbors = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        
        minutes = fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j, 0))    
        
        while queue:
            x, y, mins = queue.popleft()         
            minutes = mins
            for nx, ny in neighbors:
                a, b = x + nx, y + ny
                if 0 <= a < m and 0 <= b < n and grid[a][b] == 1:
                    queue.append((a, b, mins + 1))
                    grid[a][b] = 2
                    fresh -= 1

        return minutes if fresh == 0 else -1