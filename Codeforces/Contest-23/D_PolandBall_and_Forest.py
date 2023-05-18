from collections import defaultdict, Counter, deque
import sys
import threading
from functools import lru_cache

def runCase():
    n = int(input())
    p = list(map(int, input().split()))

    graph = defaultdict(list)
    for i in range(n):
        if p[i] not in graph[i + 1]:
            graph[i + 1].append(p[i])
        if i + 1 not in graph[p[i]]:
            graph[p[i]].append(i + 1)
    
    visited = set()
    def dfs(curr):
        for edges in graph[curr]:
            if edges not in visited:
                visited.add(edges)
                dfs(edges)
    
    trees = 0
    for u in p:
        if u not in visited:
            trees += 1
            visited.add(u)
            dfs(u)

    print(trees)

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