class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([[entrance[0], entrance[1], 0]])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n, EMPTY = len(maze), len(maze[0]), '.'
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while queue:
            x, y, steps = queue.popleft()
            if (x == 0 or y == 0 or x == m - 1 or y == n - 1) and [x, y] != entrance:
                return steps

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (0 <= nx < m and 0 <= ny < n 
                    and maze[nx][ny] == EMPTY and (nx, ny) not in visited):
                    queue.append([nx, ny, steps + 1])
                    visited.add((nx, ny))
        
        return -1