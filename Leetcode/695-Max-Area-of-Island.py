class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        currArea = 0
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def dfs(i, j):
            nonlocal currArea
            currArea += 1

            for dx, dy in dirs:
                r, c = i + dx, j + dy
                if 0 <= r < m and 0 <= c < n:
                    if grid[r][c] == 1:
                        grid[r][c] = 0
                        dfs(r, c)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    currArea = 0
                    grid[i][j] = 0
                    dfs(i, j)
                    maxArea = max(maxArea, currArea)
        
        return maxArea