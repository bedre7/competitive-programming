from collections import defaultdict, Counter, deque

def runCase():
    n, m = map(int, input().split())
    visited = set()
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(x, y):
        stack = [(x, y)]
        depth = grid[x][y]

        while stack:
            c, d = stack.pop()
            for dx, dy in dirs:
                a, b = dx + c, dy + d
                if 0 <= a < n and 0 <= b < m and (a, b) not in visited and grid[a][b] != 0:
                    visited.add((a, b))
                    depth += grid[a][b]
                    stack.append((a, b))
    
        return depth
    
    maxDp = 0
    for i in range(n):
        for j in range(m):
            if (i, j) not in visited and grid[i][j] > 0:
                visited.add((i, j))
                maxDp = max(maxDp, bfs(i, j))
    
    print(maxDp)

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()
