from collections import defaultdict, Counter, deque
import sys
import threading
from functools import lru_cache

def runCase():
    n = int(input())
    m = 2
    grid = []
    for _ in range(2):
        grid.append([int(i) for i in input()])
    
    dirs = [(0, 1),(1, 0),(-1, 0),(0, -1),(1, 1),(-1, -1),(1, -1),(-1, 1)]
    queue = deque()
    visited = set()
    queue.append((0, 0))
    visited.add((0, 0))

    while queue:
        x, y = queue.popleft()
        if x == 1 and y == n - 1: return print("YES")
        for dx, dy in dirs:
            a, b = dx + x, dy + y
            if 0 <= a < m and 0 <= b < n and (a, b) not in visited and grid[a][b] != 1:
                queue.append((a, b))
                visited.add((a, b))

    return print("NO")

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()