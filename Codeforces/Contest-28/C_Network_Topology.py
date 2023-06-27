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

    ones = twos = 0
    other = 0
    for k, v in graph.items():
        if len(v) == 1: ones += 1
        elif len(v) == 2: twos += 1
        else: other += 1

    if ones == 2 and twos == n - 2:
        print("bus topology")
    elif ones == other == 0 and twos == m:
        print("ring topology")
    elif ones == m and other == 1:
        print("star topology")
    else:
        print("unknown topology")



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