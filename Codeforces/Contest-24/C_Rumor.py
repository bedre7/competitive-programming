from collections import defaultdict, Counter, deque
import sys
import threading
from functools import lru_cache

def runCase():
    n, m = map(int, input().split())
    cost = {i + 1: v for i, v in enumerate(list(map(int, input().split())))}
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    visited = set()
    minCost = float('inf') 
    def dfs(curr):
        nonlocal minCost, visited
        for f in graph[curr]:
            if f not in visited:
                minCost = min(cost[f], minCost)
                visited.add(f)
                dfs(f)

    totalCost = 0
    for i in range(1, n + 1):
        if i not in visited:
            minCost = cost[i]
            visited.add(i)
            dfs(i)
            totalCost += minCost

    print(totalCost)
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