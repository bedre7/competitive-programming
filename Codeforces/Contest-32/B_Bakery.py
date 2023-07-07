from collections import defaultdict, Counter, deque
import heapq

def runCase():
    n, m, k = map(int, input().split())
    if k == 0: return print(-1)
    graph = defaultdict(list)
    for _ in range(m):
        u, v, l = map(int, input().split())
        graph[u].append((l, v))
    
    possible = set([city for city in range(1, n + 1)])
    resource = list(map(int, input().split()))
    possible -= set(resource)
    heap = []
    for res in resource:
        for dist, city in graph[res]:
            if city in possible:
                heapq.heappush(heap, dist)
    if heap:  print(heap[0])
    else : print(-1)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()
