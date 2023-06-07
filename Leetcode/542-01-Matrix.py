class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        updated = [[-1 for _ in range(n)] for _ in range(m)]
        queue = deque()

        def bfs():
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            while queue:
                x, y = queue.popleft()
                
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and updated[nx][ny] == -1:
                        queue.append((nx, ny))
                        updated[nx][ny] = updated[x][y] + 1


        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    updated[i][j] = 0
                    
        bfs(i, j)
        return updated
