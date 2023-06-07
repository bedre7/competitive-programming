class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n, visited = len(grid), set()

        def dfs(x, y):
            for dx, dy in dirs:
                a, b = dx + x, dy + y
                if 0 <= a< n and 0 <= b < n and (a, b) not in visited and grid[a][b]==1:
                    visited.add((a, b))
                    dfs(a, b)
        
        def bfs():
            queue = deque(visited)
            level = 0

            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    if grid[x][y] == 1 and level > 0: return level - 1
                    for dx, dy in dirs:
                        a, b = dx + x, dy + y
                        if 0 <= a < n and 0 <= b < n and (a, b) not in visited:
                            visited.add((a, b))
                            queue.append((a, b))
                level += 1
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    visited.add((i, j))
                    dfs(i, j)
                    return bfs()