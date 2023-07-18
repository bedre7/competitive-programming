from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append([c for c in input()])
    
    def dist(a, b, c, d):
        return pow(a - c, 2) + pow(b - d, 2)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def bfs(x, y):
        visited = set([(x, y)])
        queue = deque([(x, y)])

        while queue:
            x, y = queue.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == '0':
                    grid[nx][ny] = '1'
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        
        return visited
    
    visited1, visited2 = bfs(r1 - 1, c1 - 1), bfs(r2 - 1, c2 - 1)
    if (r2, c2) in visited1: return print(0)
    cost = float("inf")
    for a, b in visited1:
        for c, d in visited2:
            cost = min(cost, dist(a, b, c, d))
    
    print(cost)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()