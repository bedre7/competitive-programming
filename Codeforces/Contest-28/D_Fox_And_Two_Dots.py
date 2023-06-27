from collections import defaultdict, Counter, deque
import sys
import threading
from functools import lru_cache

def runCase():
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append([c for c in input()])
    
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    def dfs(x, y, px, py, ID, c):
        grid[x][y] = ID
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if nx != px and ny != py and grid[nx][ny] == ID: return True
            if grid[nx][ny] == c and dfs(nx, ny, x, y, ID, c):
                return True

        return False
        
    ID = 0
    for i in range(n):
        for j in range(m):
            if not grid[i][j].isdigit():
                if dfs(i, j, -1, -1, str(ID), grid[i][j]): return print("Yes")
                ID += 1
    
    print("No")

def main():
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()