from collections import defaultdict, Counter, deque
import sys
import threading
from functools import lru_cache
import heapq

def runCase():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    #num of childs -> freq
    children = Counter(list(map(len, graph.values())))
    print(children)
    filtered = sorted(children.items(), key=lambda x: x[1])
    print(filtered[0][0], filtered[1][0] - 1)

def main():
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()