class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def bfs(queue):
            visited = set()
            
            while queue:
                x, y = queue.popleft()
                visited.add((x, y))

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < m and 0 <= ny < n and
                        (nx, ny) not in visited and heights[nx][ny] >= heights[x][y]):
                        queue.append((nx, ny))
            
            return visited
        
        pacq, atq = deque(), deque()
        for i in range(max(m, n)):
            if i < n: 
                pacq.append((0, i))
                atq.append((m - 1, i))
            if i < m: 
                pacq.append((i, 0))
                atq.append((i, n - 1))
        
        return bfs(pacq).intersection(bfs(atq))


        