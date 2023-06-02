from collections import defaultdict, Counter, deque
import sys
import threading
from functools import lru_cache

def runCase():
    n, m = map(int, input().split())
    visited = set()
    graph = defaultdict(set)
    if m + 1 != n: return print("no")

    def dfs(b):
        nonlocal visited
        for c in graph[b]:
            if c not in visited:
                visited.add(c)
                dfs(c)
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)
    
    visited.add(1)
    dfs(1)
    if len(visited) != n:
        print("no")
    else:
        print("yes")

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